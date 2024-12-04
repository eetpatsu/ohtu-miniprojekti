import unittest
import os
from viite_editori import ViiteEditori

class TestViiteEditori(unittest.TestCase):

    def setUp(self):
        self.testieditori = ViiteEditori(DummyConsoleIO())

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
        
    def tearDown(self):
        if os.path.exists("temptiedosto.bib"):
            os.remove("temptiedosto.bib")


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