import unittest
import os
from viite_editori import ViiteEditori
from pathlib import Path

class TestViiteEditori(unittest.TestCase):

    def setUp(self):
        self.testieditori = ViiteEditori(DummyConsoleIO())
        self.testitiedosto = "testi.bib"

    def test_avaa_tiedosto_onnistuneesti(self):
        # Luo testitiedoston
        with open(self.testitiedosto, "w") as f:
            f.write("Testitiedoston sisältö")
        self.testieditori.avaa_tiedosto(self.testitiedosto)
        self.assertEqual(str(self.testieditori.aktiivinen_tiedosto), str(Path(self.testitiedosto).resolve()))

    def test_tiedosto_lisataan_paatteella(self):
        tiedostonimi_ilman_paatetta = "tiedosto_ilman_paatetta"
        # Luo testitiedoston .bib-päätteellä
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
    
    def test_tulosta_tiedosto(self):
        nimi = "testitiedosto.bib"
        self.testieditori.avaa_tiedosto(nimi)
        self.assertEqual(self.testieditori.Tulosta_tiedosto(nimi), 0)

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

class DummyConsoleIO:
    data = []
    indeksi = 0

    def kirjoita(self, str):
        pass
    def lue(self, kehote=""):
        if self.indeksi < len(self.data):
            result = self.data[self.indeksi]
            self.indeksi += 1
            return result
        return ""