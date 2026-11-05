"""testes do qa de render com vídeo sintético. pulam se ffmpeg não estiver instalado."""
import contextlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
import render_qa  # noqa: E402

TEM_FFMPEG = shutil.which("ffmpeg") and shutil.which("ffprobe")


def gerar(destino: Path) -> None:
    """6 s em 320x240 a 30 fps: 0-3 cor, 3-4 preto, 4-6 cor; áudio: tom em 0-2 e 3-6, silêncio em 2-3."""
    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-f", "lavfi", "-i", "color=c=0xd04060:s=320x240:r=30:d=3",
        "-f", "lavfi", "-i", "color=c=black:s=320x240:r=30:d=1",
        "-f", "lavfi", "-i", "testsrc2=s=320x240:r=30:d=2",
        "-f", "lavfi", "-i", "sine=frequency=440:duration=2:sample_rate=48000",
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono:d=1",
        "-f", "lavfi", "-i", "sine=frequency=330:duration=3:sample_rate=48000",
        "-filter_complex", "[0:v][1:v][2:v]concat=n=3:v=1:a=0[v];[3:a][4:a][5:a]concat=n=3:v=0:a=1[a]",
        "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest",
        str(destino),
    ]
    subprocess.run(cmd, check=True)


@unittest.skipUnless(TEM_FFMPEG, "ffmpeg não disponível")
class RenderQaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.video = Path(cls.tmp.name) / "sintetico.mp4"
        gerar(cls.video)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def rodar(self, *extra):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            codigo = render_qa.main([str(self.video), "--json", *extra])
        return codigo, json.loads(buf.getvalue())

    def test_detecta_preto_nao_previsto(self):
        codigo, rel = self.rodar()
        self.assertEqual(codigo, 1)
        self.assertTrue(any(abs(p["inicio"] - 3.0) < 0.2 for p in rel["pretos"]))

    def test_preto_intencional_nao_falha(self):
        codigo, rel = self.rodar("--allow-black", "2.9-4.1")
        self.assertEqual(codigo, 0, rel["falhas"])
        self.assertTrue(all(p["intencional"] for p in rel["pretos"]))

    def test_detecta_silencio(self):
        _, rel = self.rodar("--allow-black", "2.9-4.1")
        self.assertTrue(any(1.8 < s["inicio"] < 2.2 for s in rel["silencios"]))

    def test_expectativas(self):
        codigo, rel = self.rodar("--allow-black", "2.9-4.1", "--expect-size", "1440x1080", "--expect-duration", "31.667")
        self.assertEqual(codigo, 1)
        textos = " ".join(rel["falhas"])
        self.assertIn("tamanho", textos)
        self.assertIn("duração", textos)

    def test_nivel_por_segmento(self):
        codigo, rel = self.rodar("--allow-black", "2.9-4.1", "--segment", "tom:0.2-1.8", "--segment", "pausa:2.1-2.9")
        niveis = {s["rotulo"]: s["rms_db"] for s in rel["segmentos"]}
        self.assertIsNotNone(niveis["tom"])
        self.assertTrue(niveis["pausa"] is None or niveis["pausa"] < niveis["tom"] - 30)


if __name__ == "__main__":
    unittest.main()
