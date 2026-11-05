#!/usr/bin/env python3
"""valida a base de conhecimento do mayco-video-system.

checa, sem dependências fora da biblioteca padrão (python 3.11+):
  1. registros em data/ (fontes, evidências, decisões): campos, classes, ids únicos, referências
  2. citações nos markdown: todo EV-, DEC-, FAL- e S- citado existe
  3. links relativos e âncoras dos markdown
  4. documentos órfãos: todo .md em docs/ precisa ser alcançável a partir do README
  5. afirmações sem evidência: blocos com medidas (s, px, dB, LUFS, fps) ou node ids nos estudos e na gramática precisam citar evidência
  6. estudos de falha: cada FAL tem os doze campos
  7. escrita: travessão, maiúscula em início de frase, termos que o manual de voz evita, exclamação
  8. auditoria de publicação: mídia, fontes tipográficas, arquivos grandes, urls assinadas, tokens, e-mails

uso:
  python3 tools/validate.py            # valida o repositório
  python3 tools/validate.py --root DIR # valida outra árvore (usado nos testes)
  python3 tools/validate.py --report   # mostra também estatísticas e evidências não citadas
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import tomllib
import unicodedata
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path

CLASSES = {
    "fato-observado",
    "resultado-verificado",
    "instrucao-explicita",
    "implementacao-relatada",
    "interpretacao",
    "hipotese",
    "decisao-nova",
}
CONFIANCA = {"alta", "media", "baixa"}
ACESSO = {"acessada", "parcial", "inacessivel"}
PUBLICAVEL = {"metadados", "trechos", "nada"}
APROVACAO = {"verificada", "publicada", "nao-verificavel", "pendente", "nao-se-aplica"}
ORIGEM = {"recuperada", "nova"}

ID_EV = re.compile(r"\bEV-[A-Z0-9]+-\d+\b")
ID_DEC = re.compile(r"\bDEC-\d+\b")
ID_FAL = re.compile(r"\bFAL-\d+\b")
ID_S = re.compile(r"\bS-[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*\b")

# campos obrigatórios de cada estudo de falha (rótulos em negrito no markdown)
FAL_CAMPOS = [
    "intenção",
    "implementação",
    "resultado observado",
    "crítica",
    "hipótese de causa",
    "evidência da causa",
    "correção proposta",
    "alteração realizada",
    "resultado depois",
    "aprovação",
    "princípio",
    "limites",
]

# documentos onde números e node ids precisam vir acompanhados de evidência
PASTAS_COM_EVIDENCIA = ("docs/estudos", "docs/gramatica", "docs/metodo/ambiente.md")
MEDIDA = re.compile(
    r"(\b\d+[,.]\d+\s?s\b|\b\d+\s?px\b|\b-?\d+[,.]?\d*\s?dB\b|\bLUFS\b|\b\d{2,4}:\d{3,5}\b)"
)

# termos que o manual de voz pede para evitar (comparação sem acento e em minúsculas)
TERMOS_EVITAR = [
    "incrivel",
    "revolucionario",
    "transformador",
    "inovador",
    "inovadora",
    "apaixonado",
    "memoravel",
    "cases",
    "stakeholders",
    "acionavel",
    "escalavel",
    "impactante",
    "somos especialistas",
    "nossa missao",
    "acreditamos que",
    "entregamos resultados",
    "experiencias unicas",
    "qualquer duvida estou a disposicao",
]

# palavras comuns que denunciam frase começando com maiúscula
INICIO_MAIUSCULO = {
    "O", "A", "Os", "As", "Um", "Uma", "Não", "Se", "Quando", "Para", "Em", "É", "Isso",
    "Este", "Esta", "Esse", "Essa", "No", "Na", "Nos", "Nas", "Do", "Da", "De", "Com",
    "Por", "Mas", "E", "Cada", "Todo", "Toda", "Como", "Onde", "Aqui", "Ele", "Ela",
    "Também", "Antes", "Depois", "Sem", "Use", "Usar", "Veja", "Leia", "Nunca", "Sempre",
    "Há", "Ao", "Às", "Pelo", "Pela", "Que", "Qual", "Quais", "Isto", "Então", "Assim",
}

EXT_PROIBIDAS = {
    ".mp4", ".mov", ".m4v", ".webm", ".mkv", ".m4a", ".mp3", ".wav", ".aac", ".flac",
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".heic", ".psd",
    ".otf", ".ttf", ".woff", ".woff2", ".pdf", ".fig", ".zip",
}
LIMITE_BYTES = 1_000_000
SEGREDOS = [
    (re.compile(r"X-Amz-Signature"), "url assinada (S3)"),
    (re.compile(r"figma\.com/api/mcp/asset"), "url temporária de asset do Figma"),
    (re.compile(r"figma\.com/blobs/"), "url temporária de export do Figma"),
    (re.compile(r"AKIA[0-9A-Z]{16}"), "chave de acesso AWS"),
    (re.compile(r"ghp_[A-Za-z0-9]{20,}"), "token GitHub"),
    (re.compile(r"\bsk-[A-Za-z0-9]{20,}"), "chave de API"),
    (re.compile(r"xox[abpr]-[A-Za-z0-9-]{10,}"), "token Slack"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "chave privada"),
    (re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9.-]+"), "endereço de e-mail"),
]
IGNORAR_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules"}


@dataclass
class Relatorio:
    erros: list[str] = field(default_factory=list)
    avisos: list[str] = field(default_factory=list)

    def erro(self, onde: str, msg: str) -> None:
        self.erros.append(f"ERRO   {onde}: {msg}")

    def aviso(self, onde: str, msg: str) -> None:
        self.avisos.append(f"AVISO  {onde}: {msg}")


def sem_acento(texto: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")


def tirar_codigo(linha: str) -> str:
    """remove trechos entre crases para que identificadores não disparem regras de escrita."""
    return re.sub(r"`[^`]*`", "``", linha)


# ------------------------------------------------------------------ registros
def carregar(root: Path, rel: str, chave: str, rep: Relatorio) -> list[dict]:
    caminho = root / rel
    if not caminho.exists():
        rep.erro(rel, "arquivo de registro ausente")
        return []
    try:
        with caminho.open("rb") as f:
            dados = tomllib.load(f)
    except tomllib.TOMLDecodeError as e:
        rep.erro(rel, f"toml inválido: {e}")
        return []
    itens = dados.get(chave, [])
    if not isinstance(itens, list):
        rep.erro(rel, f"[[{chave}]] precisa ser uma lista de tabelas")
        return []
    return itens


def checar_texto_registro(onde: str, texto: str, rep: Relatorio) -> None:
    limpo = tirar_codigo(texto)
    if "—" in limpo:
        rep.erro(onde, "travessão (—) fora de identificador")


def validar_registros(root: Path, rep: Relatorio) -> tuple[dict, dict, dict]:
    fontes = {}
    for i, f in enumerate(carregar(root, "data/fontes.toml", "fonte", rep)):
        onde = f"data/fontes.toml#{f.get('id', i)}"
        for campo in ("id", "tipo", "titulo", "localizador", "acesso", "coletada_em", "publicavel"):
            if not f.get(campo):
                rep.erro(onde, f"campo obrigatório ausente: {campo}")
        if f.get("acesso") and f["acesso"] not in ACESSO:
            rep.erro(onde, f"acesso inválido: {f['acesso']}")
        if f.get("publicavel") and f["publicavel"] not in PUBLICAVEL:
            rep.erro(onde, f"publicavel inválido: {f['publicavel']}")
        if f.get("id") in fontes:
            rep.erro(onde, "id duplicado")
        for campo in ("titulo", "notas"):
            if f.get(campo):
                checar_texto_registro(onde, f[campo], rep)
        fontes[f.get("id")] = f

    evid = {}
    brutas = carregar(root, "data/evidencias.toml", "evidencia", rep)
    for i, e in enumerate(brutas):
        onde = f"data/evidencias.toml#{e.get('id', i)}"
        for campo in ("id", "classe", "fonte", "localizador", "afirmacao", "confianca", "escopo"):
            if not e.get(campo):
                rep.erro(onde, f"campo obrigatório ausente: {campo}")
        if e.get("id") and not ID_EV.fullmatch(e["id"]):
            rep.erro(onde, "id fora do padrão EV-<escopo>-<n>")
        if e.get("classe") and e["classe"] not in CLASSES:
            rep.erro(onde, f"classe inválida: {e['classe']}")
        if e.get("confianca") and e["confianca"] not in CONFIANCA:
            rep.erro(onde, f"confiança inválida: {e['confianca']}")
        if e.get("fonte") and e["fonte"] not in fontes:
            rep.erro(onde, f"fonte inexistente: {e['fonte']}")
        if e.get("classe") == "interpretacao" and not e.get("relacionadas"):
            rep.erro(onde, "interpretação precisa listar as evidências em que se apoia (relacionadas)")
        if e.get("id") in evid:
            rep.erro(onde, "id duplicado")
        for campo in ("afirmacao", "notas"):
            if e.get(campo):
                checar_texto_registro(onde, e[campo], rep)
        evid[e.get("id")] = e
    for eid, e in evid.items():
        for campo in ("relacionadas", "contradiz"):
            for ref in e.get(campo, []):
                if ref not in evid:
                    rep.erro(f"data/evidencias.toml#{eid}", f"{campo} aponta para evidência inexistente: {ref}")

    decs = {}
    for i, d in enumerate(carregar(root, "data/decisoes.toml", "decisao", rep)):
        onde = f"data/decisoes.toml#{d.get('id', i)}"
        for campo in ("id", "enunciado", "origem", "direcao", "implementacao", "resultado", "evidencias", "escopo", "limites"):
            if d.get(campo) in (None, "", []):
                rep.erro(onde, f"campo obrigatório ausente: {campo}")
        if d.get("origem") and d["origem"] not in ORIGEM:
            rep.erro(onde, f"origem inválida: {d['origem']}")
        for nivel in ("direcao", "implementacao", "resultado"):
            if d.get(nivel) and d[nivel] not in APROVACAO:
                rep.erro(onde, f"{nivel} inválido: {d[nivel]}")
        for ref in d.get("evidencias", []):
            if ref not in evid:
                rep.erro(onde, f"evidência inexistente: {ref}")
        if d.get("id") in decs:
            rep.erro(onde, "id duplicado")
        for campo in ("enunciado", "limites"):
            if d.get(campo):
                checar_texto_registro(onde, d[campo], rep)
        decs[d.get("id")] = d
    return fontes, evid, decs


# ------------------------------------------------------------------ markdown
def slug(titulo: str) -> str:
    t = titulo.strip().lower()
    t = re.sub(r"`", "", t)
    t = "".join(c for c in t if c.isalnum() or c in " -_")
    return t.replace(" ", "-")


def blocos_markdown(texto: str):
    """devolve (linha_inicial, texto_do_bloco, em_codigo) para parágrafos, itens de lista e linhas de tabela."""
    linhas = texto.split("\n")
    em_codigo = False
    atual: list[str] = []
    inicio = 1
    for n, linha in enumerate(linhas, 1):
        if linha.strip().startswith("```"):
            if atual:
                yield inicio, "\n".join(atual), False
                atual = []
            em_codigo = not em_codigo
            continue
        if em_codigo:
            continue
        nova_unidade = (
            not linha.strip()
            or re.match(r"^\s*([-*+]|\d+\.)\s", linha)
            or linha.lstrip().startswith("|")
            or linha.lstrip().startswith("#")
        )
        if nova_unidade and atual:
            yield inicio, "\n".join(atual), False
            atual = []
        if linha.strip():
            if not atual:
                inicio = n
            atual.append(linha)
            if linha.lstrip().startswith("|") or linha.lstrip().startswith("#"):
                yield inicio, "\n".join(atual), False
                atual = []
    if atual:
        yield inicio, "\n".join(atual), False


def linhas_prosa(texto: str):
    em_codigo = False
    for n, linha in enumerate(texto.split("\n"), 1):
        if linha.strip().startswith("```"):
            em_codigo = not em_codigo
            continue
        if em_codigo:
            continue
        yield n, linha


def coletar_md(root: Path) -> list[Path]:
    arquivos = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORAR_DIRS and not (Path(dirpath) == root and d == "tests")]
        for nome in filenames:
            if nome.endswith(".md"):
                arquivos.append(Path(dirpath) / nome)
    return sorted(arquivos)


def ancoras(texto: str) -> set[str]:
    vistas: dict[str, int] = {}
    resultado = set()
    for _, linha in linhas_prosa(texto):
        m = re.match(r"^(#{1,6})\s+(.*)$", linha)
        if m:
            base = slug(m.group(2))
            k = vistas.get(base, 0)
            resultado.add(base if k == 0 else f"{base}-{k}")
            vistas[base] = k + 1
    return resultado


def validar_markdown(root: Path, evid: dict, decs: dict, fontes: dict, rep: Relatorio) -> tuple[set, set]:
    arquivos = coletar_md(root)
    textos = {p: p.read_text(encoding="utf-8") for p in arquivos}
    cache_ancoras = {p: ancoras(t) for p, t in textos.items()}

    # ids de falha definidos no documento de diagnóstico
    fal_definidas: dict[str, tuple[Path, int]] = {}
    for p, t in textos.items():
        for n, linha in linhas_prosa(t):
            m = re.match(r"^#{2,4}\s+(FAL-\d+)\b", linha)
            if m:
                if m.group(1) in fal_definidas:
                    rep.erro(f"{p.relative_to(root)}:{n}", f"{m.group(1)} definida duas vezes")
                fal_definidas[m.group(1)] = (p, n)

    citadas_ev: set[str] = set()
    citadas_dec: set[str] = set()
    links: dict[Path, set[Path]] = {p: set() for p in arquivos}

    for p, texto in textos.items():
        rel = p.relative_to(root).as_posix()
        for n, linha in linhas_prosa(texto):
            onde = f"{rel}:{n}"
            for ref in ID_EV.findall(linha):
                citadas_ev.add(ref)
                if ref not in evid:
                    rep.erro(onde, f"evidência citada não existe: {ref}")
            for ref in ID_DEC.findall(linha):
                citadas_dec.add(ref)
                if ref not in decs:
                    rep.erro(onde, f"decisão citada não existe: {ref}")
            for ref in ID_FAL.findall(linha):
                if ref not in fal_definidas:
                    rep.erro(onde, f"falha citada não existe: {ref}")
            for ref in ID_S.findall(linha):
                if ref not in fontes:
                    rep.erro(onde, f"fonte citada não existe: {ref}")

            # links relativos
            for alvo in re.findall(r"\]\(([^)\s]+)\)", tirar_codigo(linha)):
                if re.match(r"^[a-z]+:", alvo):
                    continue
                caminho, _, ancora = alvo.partition("#")
                destino = (p.parent / caminho).resolve() if caminho else p.resolve()
                if not destino.exists():
                    rep.erro(onde, f"link quebrado: {alvo}")
                    continue
                if destino.suffix == ".md":
                    links[p].add(destino)
                    if ancora and destino in {q.resolve() for q in arquivos}:
                        alvo_p = next(q for q in arquivos if q.resolve() == destino)
                        if ancora not in cache_ancoras[alvo_p]:
                            rep.erro(onde, f"âncora inexistente: {alvo}")

            # escrita
            limpo = tirar_codigo(linha)
            if re.match(r"^\s*\|", limpo) is None:  # tabelas: ainda checamos travessão
                pass
            if "—" in limpo:
                rep.erro(onde, "travessão (—); reescrever a frase")
            if re.search(r"\s–\s", limpo):
                rep.erro(onde, "travessão (–) usado como pausa; reescrever a frase")
            texto_cmp = sem_acento(limpo.lower())
            for termo in TERMOS_EVITAR:
                if re.search(rf"\b{re.escape(termo)}\b", texto_cmp):
                    rep.erro(onde, f"termo que o manual de voz evita: '{termo}' (use crase se for citação)")
            sem_links = re.sub(r"\]\([^)]*\)", "]", limpo)
            if "!" in re.sub(r"!\[", "[", sem_links) and not limpo.lstrip().startswith("<!--"):
                rep.aviso(onde, "exclamação em prosa; é mesmo necessária?")
            corpo = re.sub(r"^\s*(#{1,6}|[-*+]|\d+\.|>)\s*", "", limpo)
            corpo = re.sub(r"^\*\*[^*]+\*\*:?\s*", "", corpo)
            if re.match(r"^[A-Z]\s·", corpo):  # rótulos de hipótese ou cenário: "A · ..."
                corpo = corpo[3:]
            candidatos = [corpo] + re.split(r"(?<=[.?:;])\s+", corpo)[1:]
            for c in candidatos:
                primeira = re.match(r"^[\"'(]*([A-Za-zÀ-ÿ]+)\b", c.strip())
                if primeira and primeira.group(1) in INICIO_MAIUSCULO:
                    rep.erro(onde, f"frase começando com maiúscula: '{primeira.group(1)}'")
                    break

        # afirmações com medida precisam de evidência no mesmo bloco
        if rel.startswith(PASTAS_COM_EVIDENCIA):
            for inicio, bloco, _ in blocos_markdown(texto):
                if bloco.lstrip().startswith("#"):
                    continue
                sem_cod = tirar_codigo(bloco)
                if MEDIDA.search(sem_cod) and not (ID_EV.search(bloco) or ID_DEC.search(bloco) or ID_FAL.search(bloco)):
                    if re.match(r"^\s*\|[\s:-]+\|", bloco):
                        continue
                    rep.erro(f"{rel}:{inicio}", "bloco com medida ou node id sem citar evidência (EV-, DEC- ou FAL-)")

    # estudos de falha: doze campos
    for fid, (p, n) in fal_definidas.items():
        texto = textos[p]
        trecho = texto.split("\n")[n - 1 :]
        fim = len(trecho)
        for i, linha in enumerate(trecho[1:], 1):
            if re.match(r"^#{2,3}\s", linha):
                fim = i
                break
        secao = "\n".join(trecho[:fim]).lower()
        for campo in FAL_CAMPOS:
            if f"**{campo}" not in secao:
                rep.erro(f"{p.relative_to(root)}:{n}", f"{fid} sem o campo '{campo}'")

    # órfãos: tudo em docs/ precisa ser alcançável a partir do README
    readme = root / "README.md"
    if not readme.exists():
        rep.erro("README.md", "ausente")
    else:
        vistos = {readme.resolve()}
        fila = deque([readme])
        mapa = {q.resolve(): q for q in arquivos}
        while fila:
            atual = fila.popleft()
            for destino in links.get(atual, set()):
                if destino not in vistos:
                    vistos.add(destino)
                    if destino in mapa:
                        fila.append(mapa[destino])
        for p in arquivos:
            rel = p.relative_to(root).as_posix()
            if rel.startswith("docs/") and p.resolve() not in vistos:
                rep.erro(rel, "documento órfão: nenhum caminho de links a partir do README")
    return citadas_ev, citadas_dec


# ------------------------------------------------------------------ auditoria de publicação
def auditar_arquivos(root: Path, rep: Relatorio) -> None:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORAR_DIRS and not (Path(dirpath) == root and d == "tests")]
        for nome in filenames:
            p = Path(dirpath) / nome
            rel = p.relative_to(root).as_posix()
            if p.suffix.lower() in EXT_PROIBIDAS:
                rep.erro(rel, f"tipo de arquivo que não deve ser publicado ({p.suffix}): mídia, fonte ou documento privado")
                continue
            try:
                tamanho = p.stat().st_size
            except OSError:
                continue
            if tamanho > LIMITE_BYTES:
                rep.erro(rel, f"arquivo com {tamanho} bytes; acima do limite de {LIMITE_BYTES}")
                continue
            try:
                texto = p.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                rep.erro(rel, "arquivo binário ou ilegível")
                continue
            if rel == "tools/validate.py":
                continue  # o próprio validador contém os padrões que procura
            for n, linha in enumerate(texto.split("\n"), 1):
                for padrao, motivo in SEGREDOS:
                    if padrao.search(linha):
                        rep.erro(f"{rel}:{n}", f"possível dado sensível: {motivo}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    ap.add_argument("--report", action="store_true")
    args = ap.parse_args(argv)
    root = Path(args.root).resolve()
    rep = Relatorio()
    fontes, evid, decs = validar_registros(root, rep)
    citadas_ev, citadas_dec = validar_markdown(root, evid, decs, fontes, rep)
    auditar_arquivos(root, rep)

    nao_citadas = sorted(set(evid) - citadas_ev)
    for eid in nao_citadas:
        rep.aviso("data/evidencias.toml", f"{eid} não é citada em nenhum documento")

    for linha in rep.erros + rep.avisos:
        print(linha)
    if args.report:
        por_classe: dict[str, int] = {}
        for e in evid.values():
            por_classe[e.get("classe", "?")] = por_classe.get(e.get("classe", "?"), 0) + 1
        print("\nresumo")
        print(f"  fontes: {len(fontes)}  evidências: {len(evid)}  decisões: {len(decs)}")
        for k in sorted(por_classe):
            print(f"  {k}: {por_classe[k]}")
        print(f"  evidências citadas: {len(citadas_ev & set(evid))}/{len(evid)}")
    print(f"\n{len(rep.erros)} erro(s), {len(rep.avisos)} aviso(s)")
    return 1 if rep.erros else 0


if __name__ == "__main__":
    sys.exit(main())
