#!/usr/bin/env python3
"""qa de render: inspeciona um vídeo exportado e compara com o que a timeline promete.

nasceu de problemas reais do acervo: preto depois de um ponto da timeline, duração diferente
da fonte, áudio que some ou que fica alto demais nas inserções, preto intencional confundido
com defeito. depende só de ffprobe e ffmpeg no PATH.

exemplos:
  python3 tools/render_qa.py render.mp4 --expect-size 1440x1080 --expect-fps 30 \\
      --expect-duration 31.667 --duration-tolerance 0.1 --expect-audio
  python3 tools/render_qa.py render.mp4 --allow-black 18.9-19.9   # placa preta intencional
  python3 tools/render_qa.py master.mp4 --segment fala:0.2-4.8 --segment musica:9.0-10.8
  python3 tools/render_qa.py render.mp4 --sheet folha.png --sheet-fps 1 --json

saída: relatório legível (ou json com --json). código 1 se alguma expectativa falhar
ou se houver preto fora dos intervalos permitidos.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass, field


@dataclass
class Intervalo:
    inicio: float
    fim: float
    rotulo: str = ""

    @property
    def duracao(self) -> float:
        return round(self.fim - self.inicio, 3)


@dataclass
class Relatorio:
    arquivo: str
    video: dict = field(default_factory=dict)
    audio: dict | None = None
    duracao_container: float | None = None
    pretos: list[dict] = field(default_factory=list)
    congelamentos: list[dict] = field(default_factory=list)
    silencios: list[dict] = field(default_factory=list)
    loudness_lufs: float | None = None
    segmentos: list[dict] = field(default_factory=list)
    falhas: list[str] = field(default_factory=list)
    observacoes: list[str] = field(default_factory=list)


def rodar(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True)


def exigir_ferramentas() -> None:
    faltando = [f for f in ("ffprobe", "ffmpeg") if shutil.which(f) is None]
    if faltando:
        sys.exit(f"faltam ferramentas no PATH: {', '.join(faltando)}")


def probe(arquivo: str) -> dict:
    r = rodar(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", arquivo])
    if r.returncode != 0:
        sys.exit(f"ffprobe falhou: {r.stderr.strip()}")
    return json.loads(r.stdout)


def fps(valor: str) -> float:
    num, _, den = valor.partition("/")
    try:
        return round(float(num) / float(den or 1), 3)
    except (ValueError, ZeroDivisionError):
        return 0.0


def detectar(arquivo: str, pix_th: float, black_min: float, freeze_min: float, silence_db: float, silence_min: float):
    filtro_v = f"blackdetect=d={black_min}:pix_th={pix_th},freezedetect=n=0.003:d={freeze_min}"
    filtro_a = f"silencedetect=n={silence_db}dB:d={silence_min},ebur128"
    r = rodar(["ffmpeg", "-hide_banner", "-nostats", "-i", arquivo, "-vf", filtro_v, "-af", filtro_a, "-f", "null", "-"])
    log = r.stderr
    if "does not contain any stream" in log or "matches no streams" in log:
        r = rodar(["ffmpeg", "-hide_banner", "-nostats", "-i", arquivo, "-vf", filtro_v, "-an", "-f", "null", "-"])
        log = r.stderr
    pretos = [Intervalo(float(a), float(b)) for a, b in re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", log)]
    inicios = [float(x) for x in re.findall(r"freeze_start: ([\d.]+)", log)]
    fins = [float(x) for x in re.findall(r"freeze_end: ([\d.]+)", log)]
    congel = [Intervalo(a, b) for a, b in zip(inicios, fins)]
    s_ini = [float(x) for x in re.findall(r"silence_start: (-?[\d.]+)", log)]
    s_fim = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
    silencios = [Intervalo(max(a, 0.0), b) for a, b in zip(s_ini, s_fim)]
    if len(s_ini) > len(s_fim):
        silencios.append(Intervalo(s_ini[-1], -1.0, "até o fim"))
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", log)
    lufs = float(m[-1]) if m else None
    return pretos, congel, silencios, lufs


def nivel_segmento(arquivo: str, inicio: float, fim: float) -> tuple[float | None, float | None]:
    r = rodar([
        "ffmpeg", "-hide_banner", "-nostats", "-ss", str(inicio), "-t", str(fim - inicio), "-i", arquivo, "-vn",
        "-af", "astats=metadata=0:measure_overall=RMS_level+Peak_level:measure_perchannel=none", "-f", "null", "-",
    ])
    rms = re.findall(r"RMS level dB: (-?[\d.]+|-inf)", r.stderr)
    pico = re.findall(r"Peak level dB: (-?[\d.]+|-inf)", r.stderr)
    conv = lambda v: None if not v or v[-1] == "-inf" else round(float(v[-1]), 1)
    return conv(rms), conv(pico)


def folha_de_contato(arquivo: str, saida: str, taxa: float, largura: int = 320, colunas: int = 6) -> None:
    filtro = f"fps={taxa},scale={largura}:-2,tile={colunas}x{colunas}"
    r = rodar(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", arquivo, "-vf", filtro, "-frames:v", "1", saida])
    if r.returncode != 0:
        print(f"aviso: folha de contato não gerada: {r.stderr.strip()}", file=sys.stderr)


def parse_intervalo(texto: str) -> Intervalo:
    rotulo, _, faixa = texto.rpartition(":") if ":" in texto else ("", "", texto)
    a, _, b = faixa.partition("-")
    return Intervalo(float(a), float(b), rotulo)


def dentro(i: Intervalo, permitidos: list[Intervalo], folga: float = 0.15) -> bool:
    return any(i.inicio >= p.inicio - folga and i.fim <= p.fim + folga for p in permitidos)


def analisar(args) -> Relatorio:
    exigir_ferramentas()
    info = probe(args.arquivo)
    rel = Relatorio(arquivo=args.arquivo)
    v = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    rel.duracao_container = round(float(info["format"].get("duration", 0)), 3)
    if v:
        rel.video = {
            "codec": v.get("codec_name"),
            "largura": v.get("width"),
            "altura": v.get("height"),
            "fps": fps(v.get("r_frame_rate", "0/1")),
            "duracao": round(float(v.get("duration", rel.duracao_container)), 3),
        }
    if a:
        rel.audio = {
            "codec": a.get("codec_name"),
            "taxa": int(a.get("sample_rate", 0)),
            "canais": a.get("channels"),
            "duracao": round(float(a.get("duration", rel.duracao_container)), 3),
        }

    pretos, congel, silencios, lufs = detectar(
        args.arquivo, args.black_threshold, args.black_min, args.freeze_min, args.silence_db, args.silence_min
    )
    permitidos = [parse_intervalo(x) for x in args.allow_black]
    for p in pretos:
        intencional = dentro(p, permitidos)
        rel.pretos.append({**asdict(p), "duracao": p.duracao, "intencional": intencional})
        if not intencional:
            rel.falhas.append(f"preto não previsto entre {p.inicio:.2f} e {p.fim:.2f} s")
    rel.congelamentos = [{**asdict(c), "duracao": c.duracao} for c in congel]
    rel.silencios = [{**asdict(s), "duracao": s.duracao} for s in silencios]
    rel.loudness_lufs = lufs

    for texto in args.segment:
        seg = parse_intervalo(texto)
        rms, pico = nivel_segmento(args.arquivo, seg.inicio, seg.fim)
        rel.segmentos.append({**asdict(seg), "rms_db": rms, "pico_db": pico})
    rotulados: dict[str, list[float]] = {}
    for s in rel.segmentos:
        if s["rms_db"] is not None and s["rotulo"]:
            rotulados.setdefault(s["rotulo"], []).append(s["rms_db"])
    if len(rotulados) >= 2:
        medias = {k: sum(v) / len(v) for k, v in rotulados.items()}
        maior, menor = max(medias, key=medias.get), min(medias, key=medias.get)
        dif = round(medias[maior] - medias[menor], 1)
        rel.observacoes.append(f"'{maior}' está {dif} dB acima de '{menor}' em RMS médio")
        if args.max_level_gap is not None and dif > args.max_level_gap:
            rel.falhas.append(f"diferença de nível {dif} dB maior que o limite {args.max_level_gap} dB")

    # expectativas
    if args.expect_size and v:
        w, h = (int(x) for x in args.expect_size.lower().split("x"))
        if (v.get("width"), v.get("height")) != (w, h):
            rel.falhas.append(f"tamanho {v.get('width')}x{v.get('height')} diferente do esperado {w}x{h}")
    if args.expect_fps and v and abs(rel.video["fps"] - args.expect_fps) > 0.01:
        rel.falhas.append(f"fps {rel.video['fps']} diferente do esperado {args.expect_fps}")
    if args.expect_duration is not None:
        base = rel.video.get("duracao", rel.duracao_container) if v else rel.duracao_container
        if abs(base - args.expect_duration) > args.duration_tolerance:
            rel.falhas.append(
                f"duração {base:.3f} s difere de {args.expect_duration:.3f} s além da tolerância {args.duration_tolerance} s"
            )
    if args.expect_audio and not a:
        rel.falhas.append("sem trilha de áudio")
    if a and v:
        dif = abs(rel.audio["duracao"] - rel.video["duracao"])
        if dif > args.av_tolerance:
            rel.falhas.append(f"áudio e vídeo com durações diferentes ({rel.audio['duracao']} x {rel.video['duracao']} s)")
        elif dif > 0:
            rel.observacoes.append(f"áudio e vídeo diferem {dif:.3f} s (dentro da tolerância)")
    for s in rel.silencios:
        if s["fim"] == -1.0:
            rel.falhas.append(f"silêncio a partir de {s['inicio']:.2f} s até o fim do arquivo")

    if args.sheet:
        folha_de_contato(args.arquivo, args.sheet, args.sheet_fps)
        rel.observacoes.append(f"folha de contato em {args.sheet}")
    return rel


def imprimir(rel: Relatorio) -> None:
    print(f"arquivo: {rel.arquivo}")
    if rel.video:
        v = rel.video
        print(f"vídeo: {v['codec']} {v['largura']}x{v['altura']} {v['fps']} fps, {v['duracao']} s")
    print(f"áudio: {rel.audio['codec']} {rel.audio['taxa']} Hz, {rel.audio['duracao']} s" if rel.audio else "áudio: nenhum")
    print(f"loudness integrado: {rel.loudness_lufs} LUFS" if rel.loudness_lufs is not None else "loudness: n/d")
    for titulo, itens in (("pretos", rel.pretos), ("congelamentos", rel.congelamentos), ("silêncios", rel.silencios)):
        if itens:
            print(f"{titulo}:")
            for i in itens:
                extra = " (intencional)" if i.get("intencional") else ""
                fim = "fim" if i["fim"] == -1.0 else f"{i['fim']:.2f}"
                print(f"  {i['inicio']:.2f} a {fim} s{extra}")
    for s in rel.segmentos:
        print(f"segmento {s['rotulo'] or '?'} {s['inicio']}-{s['fim']} s: RMS {s['rms_db']} dB, pico {s['pico_db']} dB")
    for o in rel.observacoes:
        print(f"obs: {o}")
    for f in rel.falhas:
        print(f"FALHA: {f}")
    print("ok" if not rel.falhas else f"{len(rel.falhas)} falha(s)")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("arquivo")
    ap.add_argument("--expect-size")
    ap.add_argument("--expect-fps", type=float)
    ap.add_argument("--expect-duration", type=float)
    ap.add_argument("--duration-tolerance", type=float, default=0.1)
    ap.add_argument("--expect-audio", action="store_true")
    ap.add_argument("--av-tolerance", type=float, default=0.1, help="diferença máxima entre durações de áudio e vídeo")
    ap.add_argument("--allow-black", action="append", default=[], help="intervalo de preto intencional, ex. 18.9-19.9")
    ap.add_argument("--black-threshold", type=float, default=0.10)
    ap.add_argument("--black-min", type=float, default=0.1)
    ap.add_argument("--freeze-min", type=float, default=1.0)
    ap.add_argument("--silence-db", type=float, default=-45)
    ap.add_argument("--silence-min", type=float, default=0.4)
    ap.add_argument("--segment", action="append", default=[], help="rotulo:inicio-fim para medir nível, ex. fala:0.2-4.8")
    ap.add_argument("--max-level-gap", type=float, help="falha se a diferença de RMS entre rótulos passar disso (dB)")
    ap.add_argument("--sheet")
    ap.add_argument("--sheet-fps", type=float, default=1.0)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    rel = analisar(args)
    if args.json:
        print(json.dumps(asdict(rel), ensure_ascii=False, indent=2))
    else:
        imprimir(rel)
    return 1 if rel.falhas else 0


if __name__ == "__main__":
    sys.exit(main())
