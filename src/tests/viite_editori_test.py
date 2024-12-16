import unittest
import os
from pathlib import Path

from viite_editori import ViiteEditori

class TestViiteEditori(unittest.TestCase):

    def setUp(self):
        self.testieditori = ViiteEditori(DummyConsoleIO())
        self.testitiedosto = "testi.bib"
        self.tiedostonimi_ilman_paatetta = "tiedosto_ilman_paatetta"

    def test_avaa_tiedosto_onnistuneesti(self):
        with open(self.testitiedosto, "w") as f:
            f.write("Testitiedoston sisältö")
        self.testieditori.avaa_tiedosto(self.testitiedosto)
        self.assertEqual(str(self.testieditori.aktiivinen_tiedosto), str(Path(self.testitiedosto).resolve()))

    def test_tiedosto_lisataan_paatteella(self):
        with open(self.tiedostonimi_ilman_paatetta + ".bib", "w") as f:
            f.write("Sisältöä")
        self.testieditori.avaa_tiedosto(self.tiedostonimi_ilman_paatetta)
        odotettu_polku = Path(self.tiedostonimi_ilman_paatetta + ".bib").resolve()
        self.assertEqual(self.testieditori.aktiivinen_tiedosto, odotettu_polku)

    def test_avaa_tiedosto_ilman_paatetta_luodaan_polku(self):
        with open(self.tiedostonimi_ilman_paatetta + ".bib", "w") as f:
            f.write("Sisältöä")
        self.testieditori.avaa_tiedosto(self.tiedostonimi_ilman_paatetta)
        odotettu_polkumuoto = os.path.join(os.getcwd(), self.tiedostonimi_ilman_paatetta + ".bib")
        self.assertEqual(str(self.testieditori.aktiivinen_tiedosto), odotettu_polkumuoto)

    def test_avaa_tiedosto_ei_olemassa(self):
        tiedostonimi_ei_olemassa = "eioletamannimista"
        self.testieditori.avaa_tiedosto(tiedostonimi_ei_olemassa)
        odotettu_polku = Path(tiedostonimi_ei_olemassa + ".bib").resolve()
        self.assertIn("Tapahtui virhe: Tiedostoa "+str(odotettu_polku)+" ei löynyt.",
                      self.testieditori.io.messages)

    def test_parse_argumentti_olemassa_oleva_tiedosto(self):
        """Testaa, että olemassa oleva tiedosto avataan komentoriviparametrilla."""
        tiedostonimi = "olemassaoleva.bib"
        with open(tiedostonimi, "w") as f:
            f.write("Testitiedoston sisältö")

        self.testieditori.parse_argumentti(["viite_editori.py", tiedostonimi])

        self.assertEqual(str(self.testieditori.aktiivinen_tiedosto), str(Path(tiedostonimi).resolve()))
        os.remove(tiedostonimi)

    def test_parse_argumentti_uusi_tiedosto(self):
        """Testaa, että uusi tiedosto luodaan komentoriviparametrilla."""
        tiedostonimi = "uusi_tiedosto.bib"
        if os.path.exists(tiedostonimi):
            os.remove(tiedostonimi)

        self.testieditori.parse_argumentti(["viite_editori.py", tiedostonimi])

        self.assertTrue(os.path.exists(tiedostonimi))
        self.assertEqual(str(self.testieditori.aktiivinen_tiedosto), str(Path(tiedostonimi).resolve()))
        os.remove(tiedostonimi)

    def test_parse_argumentti_ilman_parametreja(self):
        """Testaa, että ohjelma ei yritä avata tai luoda tiedostoja ilman parametreja."""
        self.testieditori.parse_argumentti(["viite_editori.py"])

        self.assertIsNone(self.testieditori.aktiivinen_tiedosto)

    def test_tiedosto_ei_auki(self):
        self.testieditori.aktiivinen_tiedosto = None
        result = self.testieditori.syota_bib_viite()
        self.assertEqual(result, -1)

    def test_tulosta_tiedosto_onnistuneesti(self):
        tiedoston_sisalto = """
@article{other1,
  author = {Some Author},
  title = {Some Title},
  year = {2021}
}
"""
        with open(self.testitiedosto, "w") as f:
            f.write(tiedoston_sisalto)
        self.testieditori.aktiivinen_tiedosto = Path(self.testitiedosto)

        result = self.testieditori.tulosta_tiedosto()
        self.assertEqual(result, 0)
        self.assertIn(f"Tiedoston {Path(self.testitiedosto).name} sisältö:\n{tiedoston_sisalto}",
                      self.testieditori.io.messages)

    def test_tulosta_tiedosto_ei_avaa(self):
        self.testieditori.aktiivinen_tiedosto = None
        result = self.testieditori.tulosta_tiedosto()
        self.assertEqual(result, -1)
        self.assertIn("Ei avattua tiedostoa. Avaa tiedosto ensin komennolla 'avaa'.",
                    self.testieditori.io.messages)

    def test_tulosta_tiedosto_lukuvirhe(self):
        self.testieditori.aktiivinen_tiedosto = Path("olemassa_olematon_tiedosto.bib")
        result = self.testieditori.tulosta_tiedosto()
        self.assertEqual(result, -1)
        self.assertIn(f"Tapahtui virhe: Tiedostoa {self.testieditori.aktiivinen_tiedosto} ei voitu lukea.",
                    self.testieditori.io.messages)

    def test_syotetty_viite_lisataan_tiedostoon(self):
        DummyConsoleIO.data = [
            "author = {Test Author}\ntitle = {Test Title}\nyear = {2024}",
            "valmis"
        ]

        self.testieditori.aktiivinen_tiedosto = "temptiedosto.bib"
        with open(self.testieditori.aktiivinen_tiedosto, "w") as f:
            f.write("")
        self.testieditori.syota_bib_viite()
        with open(self.testieditori.aktiivinen_tiedosto, "r") as f:
            sisalto = f.read()
        odotettu_sisalto = "\nauthor = {Test Author}\ntitle = {Test Title}\nyear = {2024}\n\n"
        self.assertEqual(sisalto, odotettu_sisalto)

    def test_lisays_ilman_rivinvaihtoa(self):
        DummyConsoleIO.data = [
            "author = {Another Author}",
            "valmis"
        ]
        self.testieditori.aktiivinen_tiedosto = "temptiedosto.bib"
        alkuperainen_sisalto = "Alkuperäinen sisältö ilman rivinvaihtoa"
        with open(self.testieditori.aktiivinen_tiedosto, "w") as f:
            f.write(alkuperainen_sisalto)
        self.testieditori.syota_bib_viite()
        with open(self.testieditori.aktiivinen_tiedosto, "r") as f:
            sisalto = f.read()
        odotettu_sisalto = "Alkuperäinen sisältö ilman rivinvaihtoa\nauthor = {Another Author}\n\n"
        self.assertEqual(sisalto, odotettu_sisalto)

    def tearDown(self):
        if os.path.exists("temptiedosto.bib"):
            os.remove("temptiedosto.bib")
        if os.path.exists(self.testitiedosto):
            os.remove(self.testitiedosto)
        if os.path.exists(self.tiedostonimi_ilman_paatetta + ".bib"):
            os.remove(self.tiedostonimi_ilman_paatetta + ".bib")

    def test_helppi(self):
        self.assertEqual(self.testieditori.helppi(), 0)
        self.assertIn("\nKomennot:\n\
help\t\ttulostaa tämän viestin\n\
exit\t\tpoistuu ohjelmasta\n\
avaa\t\tavaa bib-tiedoston\n\
luo\t\tluo bib-tiedoston\n\
tulosta\t\ttulostaa aktiivisen bib-tiedoston sisällön\n\
syota\t\ttallentaa bib-dataa aktiiviseen bib-tiedostoon\n\
muokkaa\t\tmuokkaa valitun viitteen parametreja\n\
muokkaaparam\tmuokkaa valitun viitteen haluttua parametria\n\
lisaatagi\tlisää halutun tagin\n\
poistatagi\tpoistaa halutun tagin\n\
",
            self.testieditori.io.messages)

    def test_muokkaa_viite_onnistuneesti(self):
        alkuperainen_sisalto = """
@article{test1,
  author = {Old Author},
  title = {Old Title},
  year = {2020}
}
"""
        with open(self.testitiedosto, "w") as f:
            f.write(alkuperainen_sisalto)

        self.testieditori.aktiivinen_tiedosto = Path(self.testitiedosto)
        self.testieditori.muokkaa_parametri("test1", "author", "New Author")

        with open(self.testitiedosto, "r") as f:
            sisalto = f.read()

        odotettu_sisalto = """
@article{test1,
  author = {New Author},
  title = {Old Title},
  year = {2020}
}
"""
        self.assertEqual(sisalto.strip(), odotettu_sisalto.strip())
        self.assertIn("Muokkaus onnistui", self.testieditori.io.messages)

    def test_muokkaa_ei_avattua_tiedostoa(self):
        self.testieditori.aktiivinen_tiedosto = None
        tulos = self.testieditori.muokkaa_parametri("test1", "author", "New Author")
        self.assertEqual(tulos, -1)
        self.assertIn("Ei avattua tiedostoa. Avaa tiedosto ensin komennolla 'avaa'.", self.testieditori.io.messages)

    def test_muokkaa_viite_ei_loytynyt(self):
        alkuperainen_sisalto = """
@article{other1,
  author = {Some Author},
  title = {Some Title},
  year = {2021}
}
"""
        with open(self.testitiedosto, "w") as f:
            f.write(alkuperainen_sisalto)

        self.testieditori.aktiivinen_tiedosto = Path(self.testitiedosto)
        tulos = self.testieditori.muokkaa_parametri("test1", "author", "New Author")

        self.assertEqual(tulos, -1)
        self.assertIn("Viitettä avaimella 'test1' ei löytynyt.", self.testieditori.io.messages)

    def test_muokkaa_parametrin_muokkaus_epaonnistuu(self):
        alkuperainen_sisalto = """
@article{test1,
  author = {Old Author},
  title = {Old Title},
  year = {2020}
}
"""
        with open(self.testitiedosto, "w") as f:
            f.write(alkuperainen_sisalto)

        self.testieditori.aktiivinen_tiedosto = Path(self.testitiedosto)
        tulos = self.testieditori.muokkaa_parametri("test1", "nonexistent_param", "New Value")

        self.assertEqual(tulos, 0)
        self.assertIn("Muokkaus epäonnistui tarkista parametrin tyyppi", self.testieditori.io.messages)

    def test_lisaa_tagi_onnistuneesti(self):
        """testataan tagin lisäämistä oikeilla arvoilla"""
        alkuperainen_sisalto = """
@article{test1,
  author = {Old Author},
  title = {Old Title},
  year = {2020}
}@comment{tag1}
"""
        with open(self.testitiedosto, "w") as f:
            f.write(alkuperainen_sisalto)

        self.testieditori.aktiivinen_tiedosto = Path(self.testitiedosto)
        self.testieditori.lisaa_tagi("test1", "tag2")

        with open(self.testitiedosto, "r") as f:
            sisalto = f.read()

        odotettu_sisalto = """
@article{test1,
  author = {Old Author},
  title = {Old Title},
  year = {2020}
}@comment{tag1, tag2}
"""
        self.assertEqual(sisalto.strip(), odotettu_sisalto.strip())

    def test_lisaa_tagi_viite_ei_loytynyt(self):
        """testataan tagin lisäämistä väärällä arvolla"""
        alkuperainen_sisalto = """
@article{test1,
  author = {Old Author},
  title = {Old Title},
  year = {2020}
}@comment{tag1, tag2}
"""
        with open(self.testitiedosto, "w") as f:
            f.write(alkuperainen_sisalto)

        self.testieditori.aktiivinen_tiedosto = Path(self.testitiedosto)
        result = self.testieditori.lisaa_tagi("testaus", "tagi")

        self.assertEqual(result, -1)

    def test_poista_tagi_onnistuneesti(self):
        """testataan tagin poistamista oikeilla arvoilla"""
        alkuperainen_sisalto = """
@article{test1,
  author = {Old Author},
  title = {Old Title},
  year = {2020}
}@comment{tag1, tag2, tag3}
"""
        with open(self.testitiedosto, "w") as f:
            f.write(alkuperainen_sisalto)

        self.testieditori.aktiivinen_tiedosto = Path(self.testitiedosto)
        self.testieditori.poista_tagi("test1", "tag1")

        with open(self.testitiedosto, "r") as f:
            sisalto = f.read()

        odotettu_sisalto = """
@article{test1,
  author = {Old Author},
  title = {Old Title},
  year = {2020}
}@comment{tag2, tag3}
"""

        self.assertEqual(sisalto.strip(), odotettu_sisalto.strip())

    def test_poista_tagi_viite_ei_loytynyt(self):
        """testataan tagin poistamista väärillä arvoilla"""
        alkuperainen_sisalto = """
@article{test1,
  author = {Old Author},
  title = {Old Title},
  year = {2020},
  tags = {newTag}
}
"""
        with open(self.testitiedosto, "w") as f:
            f.write(alkuperainen_sisalto)

        self.testieditori.aktiivinen_tiedosto = Path(self.testitiedosto)
        result = self.testieditori.poista_tagi("testi", "Tagi")

        self.assertEqual(result, -1)

    def tear_down(self):
        if os.path.exists(self.testitiedosto):
            os.remove(self.testitiedosto)

class DummyConsoleIO:
    data = []
    indeksi = 0
    messages = []

    def kirjoita(self, str_str):
        self.messages.append(str_str)

    def lue(self, _kehote=""):
        if self.indeksi < len(self.data):
            result = self.data[self.indeksi]
            self.indeksi += 1
            return result
        return ""
