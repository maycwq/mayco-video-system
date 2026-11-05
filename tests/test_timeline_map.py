"""testes do mapa de tempo: a conversão fonte <-> final precisa ser exata nos limites das pausas."""
import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "tools"))
import timeline_map as tm  # noqa: E402


def plano_simples():
    return tm.Plano(
        10.0,
        [
            tm.Insercao("a", na_fonte=2.0, duracao=1.5),
            tm.Insercao("b", na_fonte=6.0, duracao=0.5),
            tm.Insercao("sobre", na_fonte=4.0, duracao=0.0, audio="fonte-continua", tipo="overlay"),
        ],
    )


class MapaTest(unittest.TestCase):
    def test_duracao_final_soma_so_pausas(self):
        self.assertEqual(plano_simples().duracao_final, 12.0)

    def test_fonte_para_final(self):
        p = plano_simples()
        self.assertEqual(tm.fonte_para_final(p, 1.0), 1.0)
        self.assertEqual(tm.fonte_para_final(p, 2.0), 3.5)  # a fonte congela antes de 2.0
        self.assertEqual(tm.fonte_para_final(p, 5.0), 6.5)
        self.assertEqual(tm.fonte_para_final(p, 10.0), 12.0)

    def test_final_para_fonte_dentro_da_pausa(self):
        p = plano_simples()
        fonte, desc = tm.final_para_fonte(p, 2.5)
        self.assertIsNone(fonte)
        self.assertIn("pausa:a", desc)

    def test_ida_e_volta(self):
        p = plano_simples()
        for t in (0.0, 1.9, 2.0, 3.3, 5.9, 6.0, 9.99):
            final = tm.fonte_para_final(p, t)
            fonte, _ = tm.final_para_fonte(p, final)
            self.assertAlmostEqual(fonte, t, places=3)

    def test_plano_invalido(self):
        with self.assertRaises(ValueError):
            tm.validar(tm.Plano(5.0, [tm.Insercao("x", na_fonte=9.0, duracao=1.0)]))
        with self.assertRaises(ValueError):
            tm.validar(tm.Plano(5.0, [tm.Insercao("x", na_fonte=1.0, duracao=1.0, audio="fonte-continua")]))

    def test_srt(self):
        p = plano_simples()
        srt = "1\n00:00:05,000 --> 00:00:05,500\nolá\n"
        self.assertIn("00:00:06,500 --> 00:00:07,000", tm.converter_srt(p, srt))

    def test_exemplo_do_repositorio_bate_com_o_relato(self):
        p = tm.carregar(str(RAIZ / "tools" / "exemplos" / "plano-insercoes.toml"))
        self.assertAlmostEqual(p.duracao_final, 60.65, places=3)


if __name__ == "__main__":
    unittest.main()
