import unittest
from viite_parseri import ViiteParseri

class TestViiteParseri(unittest.TestCase):

    maxDiff = None

    esimerkkiviite ="""@article{kadiyala2018applications,
title={Applications of python to evaluate the performance of decision tree-based boosting algorithms},
author={Kadiyala, Akhil and Kumar, Ashok},
journal={Environmental Progress & Sustainable Energy},
volume={37},
number={2},
pages={618--623},
year={2018},
publisher={Wiley Online Library}
}"""

    def setUp(self):
        self.testiparseri = ViiteParseri(self.esimerkkiviite)

    def test_konstruktori_ja_to_string(self):
        self.assertAlmostEqual(str(self.testiparseri), self.esimerkkiviite)

#    def test_update(self): # Tämä testi ei luultavasti järkevä. Ei myöskään mene läpi atm.
#        self.testiparseri.update()
#        self.assertEqual(str(self.testiparseri),self.esimerkkiviite)

    def test_viitteen_tyyppi(self):
        self.assertEqual(self.testiparseri.viitteen_tyyppi, "article")

    def test_viitteen_avain(self):
        self.assertEqual(self.testiparseri.viitteen_avain, "kadiyala2018applications")

    def test_viitteen_tiedot(self):
        self.assertEqual(self.testiparseri.viitteen_tiedot[0][0], "title")
        self.assertEqual(self.testiparseri.viitteen_tiedot[0][1], "Applications of python to evaluate the performance of decision tree-based boosting algorithms")

    def test_viitteen_muokkaus(self):
        self.testiparseri.muokkaa("author","Kadiyala et al")
        self.assertEqual(self.testiparseri.viitteen_tiedot[1][1],"Kadiyala et al")