import unittest
from viite_editori import ViiteEditori

class TestViiteEditori(unittest.TestCase):

    def setUp(self):
        self.testieditori = ViiteEditori(DummyConsoleIO)

    def test_tulosta_tiedosto(self):
        nimi = "testitiedosto.bib"
        self.testieditori.avaa_tiedosto(nimi)
        self.assertEqual(self.testieditori.Tulosta_tiedosto(nimi), 0)


class DummyConsoleIO:
    def kirjoita(str):
        return
    def lue():
        return

