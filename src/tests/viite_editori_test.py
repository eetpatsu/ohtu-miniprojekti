import unittest
import os
from viite_editori import ViiteEditori
from pathlib import Path

class TestViiteEditori(unittest.TestCase):

    def setUp(self):
        self.testieditori = ViiteEditori(DummyConsoleIO())
        self.testitiedosto = "testi.bib"

    def test_avaa_tiedosto_onnistuneesti(self):
        with open(self.testitiedosto, "w") as f:
            f.write("Testitiedoston sisältö")
        self.testieditori.avaa_tiedosto(self.testitiedosto)
        self.assertEqual(str(self.testieditori.aktiivinen_tiedosto), str(Path(self.testitiedosto).resolve()))

    def test_tiedosto_lisataan_paatteella(self):
        tiedostonimi_ilman_paatetta = "tiedosto_ilman_paatetta"
        with open(tiedostonimi_ilman_paatetta + ".bib", "w") as f:
            f.write("Sisältöä")
        self.testieditori.avaa_tiedosto(tiedostonimi_ilman_paatetta)
        odotettu_polku = Path(tiedostonimi_ilman_paatetta + ".bib").resolve()
        self.assertEqual(self.testieditori.aktiivinen_tiedosto, odotettu_polku)

    def test_avaa_tiedosto_ilman_paatetta_luodaan_polku(self):
        tiedostonimi_ilman_paatetta = "tiedosto_ilman_paatetta"
        self.testieditori.avaa_tiedosto(tiedostonimi_ilman_paatetta)
        odotettu_polkumuoto = os.path.join(os.getcwd(), tiedostonimi_ilman_paatetta + ".bib")
        self.assertEqual(str(self.testieditori.aktiivinen_tiedosto), odotettu_polkumuoto)

    def test_tiedosto_ei_auki(self):
        self.testieditori.aktiivinen_tiedosto = None
        result = self.testieditori.syota_bib_viite()
        self.assertEqual(result, -1)
    
    def test_tulosta_tiedosto_onnistuneesti(self):
        tiedoston_sisalto = "Testitiedoston sisältö"
        with open(self.testitiedosto, "w") as f:
            f.write(tiedoston_sisalto)
        self.testieditori.aktiivinen_tiedosto = Path(self.testitiedosto)
        
        result = self.testieditori.Tulosta_tiedosto(self.testitiedosto)
        self.assertEqual(result, 0)
        self.assertIn(f"Tiedoston {Path(self.testitiedosto).name} sisältö:\n{tiedoston_sisalto}",
                      self.testieditori.io.messages)

    def test_tulosta_tiedosto_ei_avaa(self):
        self.testieditori.aktiivinen_tiedosto = None
        result = self.testieditori.Tulosta_tiedosto("testi.bib")
        self.assertEqual(result, -1)
        self.assertIn("Ei avattua tiedostoa. Avaa tiedosto ensin komennolla 'avaa'.",
                    self.testieditori.io.messages)
    
    def test_tulosta_tiedosto_lukuvirhe(self):
        self.testieditori.aktiivinen_tiedosto = Path("olemassa_olematon_tiedosto.bib")
        result = self.testieditori.Tulosta_tiedosto("olemassa_olematon_tiedosto.bib")
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

    def test_helppi(self):
        self.assertEqual(self.testieditori.helppi(), 0)
        self.assertIn("\nKomennot:\n\
help:\t\ttulostaa tämän viestin\n\
exit:\t\tpoistuu ohjelmasta\n\
avaa:\t\tavaa bib-tiedoston\n\
luo:\t\tluo bib-tiedoston\n\
tulosta:\ttulostaa aktiivisen bib-tiedoston sisällön\n\
syota:\t\ttallentaa bib-viitteen aktiiviseen bib-tiedostoon\n\
muokkaa:\tmuokkaa valitun viitteen haluttua parametria\
",
            self.testieditori.io.messages)

class DummyConsoleIO:
    data = []
    indeksi = 0
    messages = []

    def kirjoita(self, str):
        self.messages.append(str)

    def lue(self, kehote=""):
        if self.indeksi < len(self.data):
            result = self.data[self.indeksi]
            self.indeksi += 1
            return result
        return ""
