"""import unittest
from viite_editori import ViiteEditori


class TestViiteEditori(unittest.TestCase):


    def setUp(self):
        #self.testiparseri = ViiteParseri(self.esimerkkiviite)
        #self.testieditori = ViiteEditori(...)
        

# Kopioitu toisesta testitiedostosta

    def test_konstruktori_ja_to_string(self):
        self.assertAlmostEqual(str(self.testiparseri), self.esimerkkiviite)

    def test_viitteen_tyyppi(self):
        self.assertEqual(self.testiparseri.viitteen_tyyppi, "article")

    def test_viitteen_avain(self):
        self.assertEqual(self.testiparseri.viitteen_avain, "kadiyala2018applications")

    def test_viitteen_tiedot(self):
        self.assertEqual(self.testiparseri.viitteen_tiedot[0][0], "title")
        self.assertEqual(self.testiparseri.viitteen_tiedot[0][1], "Applications of python to evaluate the performance of decision tree-based boosting algorithms")
        #self.assertEqual(self.testiparseri.viitteen_tiedot[0], "title={Applications of python to evaluate the performance of decision tree-based boosting algorithms},")
        #self.assertEqual(self.testiparseri.viitteen_tiedot[1], "author={Kadiyala, Akhil and Kumar, Ashok},")
        #self.assertEqual(self.testiparseri.viitteen_tiedot[2], "journal={Environmental Progress \& Sustainable Energy},")

"""
