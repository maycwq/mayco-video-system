#!/usr/bin/env python3
"""mapa entre tempo final (o que quem assiste vê) e tempo da fonte (o que foi gravado).

serve para edições com pausas inseridas: a fonte para, entra uma música, um clipe ou uma imagem,
e a fonte volta de onde parou. overlays não mexem no tempo; pausas mexem.

o plano é um arquivo toml:

    duracao_fonte = 47.6

    [[insercao]]
    rotulo = "river"
    na_fonte = 8.9          # instante da fonte em que a fonte congela
    duracao = 2.0           # quanto tempo a inserção ocupa no tempo final
    audio = "musica"        # musica | silencio | fonte-continua
    tipo = "pausa"          # pausa (alonga o tempo) | overlay (não alonga)

uso:
  python3 tools/timeline_map.py plano.toml --tabela
  python3 tools/timeline_map.py plano.toml --final 12.3     # que instante da fonte está na tela?
  python3 tools/timeline_map.py plano.toml --fonte 20.0     # quando esse instante da fonte aparece?
  python3 tools/timeline_map.py plano.toml --legendas srt_da_fonte.srt > srt_final.srt

regra que o mapa impõe: legenda, keyframe ou corte ancorado na fala precisa ser convertido
para tempo final antes de entrar na timeline. ancorar no tempo da fonte é o erro mais comum.
"""
from __future__ import annotations

import argparse
import re
import sys
import tomllib
from dataclasses import dataclass

AUDIOS = {"musica", "silencio", "fonte-continua"}
TIPOS = {"pausa", "overlay"}


@dataclass
class Insercao:
    rotulo: str
    na_fonte: float
    duracao: float
    audio: str = "musica"
    tipo: str = "pausa"


@dataclass
class Plano:
    duracao_fonte: float
    insercoes: list[Insercao]

    @property
    def pausas(self) -> list[Insercao]:
        return [i for i in self.insercoes if i.tipo == "pausa"]

    @property
    def duracao_final(self) -> float:
        return round(self.duracao_fonte + sum(i.duracao for i in self.pausas), 3)


def carregar(caminho: str) -> Plano:
    with open(caminho, "rb") as f:
        dados = tomllib.load(f)
    ins = [Insercao(**i) for i in dados.get("insercao", [])]
    plano = Plano(float(dados["duracao_fonte"]), sorted(ins, key=lambda i: i.na_fonte))
    validar(plano)
    return plano


def validar(plano: Plano) -> None:
    erros = []
    for i in plano.insercoes:
        if i.audio not in AUDIOS:
            erros.append(f"{i.rotulo}: audio inválido '{i.audio}'")
        if i.tipo not in TIPOS:
            erros.append(f"{i.rotulo}: tipo inválido '{i.tipo}'")
        if not 0 <= i.na_fonte <= plano.duracao_fonte:
            erros.append(f"{i.rotulo}: na_fonte {i.na_fonte} fora da fonte (0 a {plano.duracao_fonte})")
        if i.duracao < 0:
            erros.append(f"{i.rotulo}: duração negativa")
        if i.tipo == "pausa" and i.audio == "fonte-continua":
            erros.append(f"{i.rotulo}: pausa com áudio da fonte contínuo é contraditório; use overlay")
    pausas = plano.pausas
    for a, b in zip(pausas, pausas[1:]):
        if a.na_fonte == b.na_fonte:
            erros.append(f"{a.rotulo} e {b.rotulo} começam no mesmo instante da fonte; junte em uma pausa")
    if erros:
        raise ValueError("; ".join(erros))


def segmentos(plano: Plano) -> list[tuple[float, float, str, float | None]]:
    """(inicio_final, fim_final, descricao, inicio_fonte_ou_None)."""
    out = []
    t_final = 0.0
    t_fonte = 0.0
    for p in plano.pausas:
        if p.na_fonte > t_fonte:
            dur = p.na_fonte - t_fonte
            out.append((t_final, t_final + dur, "fonte", t_fonte))
            t_final += dur
            t_fonte = p.na_fonte
        out.append((t_final, t_final + p.duracao, f"pausa:{p.rotulo} ({p.audio})", None))
        t_final += p.duracao
    if t_fonte < plano.duracao_fonte:
        out.append((t_final, t_final + plano.duracao_fonte - t_fonte, "fonte", t_fonte))
    return [(round(a, 3), round(b, 3), d, None if f is None else round(f, 3)) for a, b, d, f in out]


def final_para_fonte(plano: Plano, t: float) -> tuple[float | None, str]:
    for a, b, desc, f in segmentos(plano):
        if a <= t < b or (t == b == plano.duracao_final):
            if f is None:
                return None, desc
            return round(f + (t - a), 3), "fonte"
    raise ValueError(f"{t} fora do tempo final (0 a {plano.duracao_final})")


def fonte_para_final(plano: Plano, t: float) -> float:
    if not 0 <= t <= plano.duracao_fonte:
        raise ValueError(f"{t} fora da fonte (0 a {plano.duracao_fonte})")
    deslocamento = sum(p.duracao for p in plano.pausas if p.na_fonte <= t)
    # um instante exatamente no ponto da pausa aparece depois da pausa: a fonte congela antes dele
    return round(t + deslocamento, 3)


def converter_srt(plano: Plano, texto: str) -> str:
    def conv(m):
        h, mi, s, ms = (int(x) for x in m.groups())
        t = fonte_para_final(plano, h * 3600 + mi * 60 + s + ms / 1000)
        h2, resto = divmod(t, 3600)
        mi2, s2 = divmod(resto, 60)
        return f"{int(h2):02d}:{int(mi2):02d}:{int(s2):02d},{int(round((s2 - int(s2)) * 1000)):03d}"

    return re.sub(r"(\d{2}):(\d{2}):(\d{2}),(\d{3})", conv, texto)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("plano")
    ap.add_argument("--tabela", action="store_true")
    ap.add_argument("--final", type=float)
    ap.add_argument("--fonte", type=float)
    ap.add_argument("--legendas")
    args = ap.parse_args(argv)
    try:
        plano = carregar(args.plano)
    except (ValueError, KeyError, TypeError) as e:
        print(f"plano inválido: {e}", file=sys.stderr)
        return 1
    print(f"fonte {plano.duracao_fonte} s + pausas {round(plano.duracao_final - plano.duracao_fonte, 3)} s = final {plano.duracao_final} s", file=sys.stderr)
    if args.tabela:
        print("final_inicio\tfinal_fim\tconteudo\tfonte_inicio")
        for a, b, d, f in segmentos(plano):
            print(f"{a:.3f}\t{b:.3f}\t{d}\t{'' if f is None else f'{f:.3f}'}")
    if args.final is not None:
        f, desc = final_para_fonte(plano, args.final)
        print(f"final {args.final} s -> " + (f"fonte {f} s" if f is not None else desc))
    if args.fonte is not None:
        print(f"fonte {args.fonte} s -> final {fonte_para_final(plano, args.fonte)} s")
    if args.legendas:
        with open(args.legendas, encoding="utf-8") as f:
            sys.stdout.write(converter_srt(plano, f.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
