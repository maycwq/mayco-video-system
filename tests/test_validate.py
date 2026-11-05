"""testes do validador: cada regra precisa pegar o problema que ela promete pegar."""
import contextlib
import io
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import validate  # noqa: E402

FONTES = """
[[fonte]]
id = "S-TESTE"
tipo = "teste"
titulo = "fonte de teste"
localizador = "aqui"
acesso = "acessada"
coletada_em = "2026-11-05"
publicavel = "metadados"
"""

EVID = """
[[evidencia]]
id = "EV-T-01"
classe = "fato-observado"
fonte = "S-TESTE"
localizador = "nó 1:2"
afirmacao = "uma camada existe."
confianca = "alta"
escopo = "teste"
"""

DEC = """
[[decisao]]
id = "DEC-01"
enunciado = "uma decisão."
origem = "nova"
direcao = "nao-se-aplica"
implementacao = "nao-se-aplica"
resultado = "nao-se-aplica"
evidencias = ["EV-T-01"]
escopo = "teste"
limites = "nenhum."
"""

README = "# base\n\nver [estudo](docs/estudos/um.md).\n"
ESTUDO = "# um estudo\n\na fonte dura 35,9 s [EV-T-01].\n\na decisão está em DEC-01.\n"


def montar(raiz: Path, extras: dict[str, str] | None = None) -> None:
    arquivos = {
        "data/fontes.toml": FONTES,
        "data/evidencias.toml": EVID,
        "data/decisoes.toml": DEC,
        "README.md": README,
        "docs/estudos/um.md": ESTUDO,
    }
    arquivos.update(extras or {})
    for rel, conteudo in arquivos.items():
        p = raiz / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(textwrap.dedent(conteudo), encoding="utf-8")


def rodar(raiz: Path) -> tuple[int, str]:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        codigo = validate.main(["--root", str(raiz)])
    return codigo, buf.getvalue()


class ValidadorTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.raiz = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_base_valida_passa(self):
        montar(self.raiz)
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 0, saida)

    def test_citacao_inexistente(self):
        montar(self.raiz, {"docs/estudos/um.md": ESTUDO + "\noutra coisa [EV-T-99].\n"})
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 1)
        self.assertIn("EV-T-99", saida)

    def test_medida_sem_evidencia(self):
        montar(self.raiz, {"docs/estudos/um.md": ESTUDO + "\no hook sobe 18 px.\n"})
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 1)
        self.assertIn("sem citar evidência", saida)

    def test_documento_orfao(self):
        montar(self.raiz, {"docs/estudos/solto.md": "# solto\n\nninguém aponta pra cá.\n"})
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 1)
        self.assertIn("órfão", saida)

    def test_link_quebrado(self):
        montar(self.raiz, {"README.md": README + "\nver [nada](docs/nao-existe.md).\n"})
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 1)
        self.assertIn("link quebrado", saida)

    def test_ancora_inexistente(self):
        montar(self.raiz, {"README.md": README + "\nver [parte](docs/estudos/um.md#nao-tem).\n"})
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 1)
        self.assertIn("âncora", saida)

    def test_travessao(self):
        montar(self.raiz, {"docs/estudos/um.md": ESTUDO + "\no ambiente — quando real — ajuda [EV-T-01].\n"})
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 1)
        self.assertIn("travessão", saida)

    def test_travessao_em_codigo_e_permitido(self):
        montar(self.raiz, {"docs/estudos/um.md": ESTUDO + "\na página `03 — motion` existe [EV-T-01].\n"})
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 0, saida)

    def test_maiuscula_no_inicio(self):
        montar(self.raiz, {"docs/estudos/um.md": ESTUDO + "\nO ambiente importa [EV-T-01].\n"})
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 1)
        self.assertIn("maiúscula", saida)

    def test_termo_do_manual(self):
        montar(self.raiz, {"docs/estudos/um.md": ESTUDO + "\num resultado incrível [EV-T-01].\n"})
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 1)
        self.assertIn("incrivel", saida)

    def test_midia_proibida(self):
        montar(self.raiz)
        (self.raiz / "render.mp4").write_bytes(b"\x00\x00")
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 1)
        self.assertIn(".mp4", saida)

    def test_url_assinada(self):
        montar(self.raiz, {"docs/estudos/um.md": ESTUDO + "\n[x](https://exemplo.com/a?X-Amz-Signature=abc)\n"})
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 1)
        self.assertIn("url assinada", saida)

    def test_email(self):
        montar(self.raiz, {"docs/estudos/um.md": ESTUDO + "\ncontato: alguem@exemplo.com\n"})
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 1)
        self.assertIn("e-mail", saida)

    def test_evidencia_com_fonte_inexistente(self):
        montar(self.raiz, {"data/evidencias.toml": EVID.replace('fonte = "S-TESTE"', 'fonte = "S-NADA"')})
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 1)
        self.assertIn("fonte inexistente", saida)

    def test_interpretacao_sem_base(self):
        montar(self.raiz, {"data/evidencias.toml": EVID.replace('"fato-observado"', '"interpretacao"')})
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 1)
        self.assertIn("relacionadas", saida)

    def test_falha_incompleta(self):
        falhas = "# falhas\n\n### FAL-01 · algo\n\n**intenção**: x [EV-T-01]\n"
        montar(self.raiz, {
            "docs/diagnostico/falhas.md": falhas,
            "README.md": README + "\n[falhas](docs/diagnostico/falhas.md)\n",
        })
        codigo, saida = rodar(self.raiz)
        self.assertEqual(codigo, 1)
        self.assertIn("FAL-01 sem o campo", saida)


if __name__ == "__main__":
    unittest.main()
