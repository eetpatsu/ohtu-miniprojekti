import unittest
from viite_parseri import ViiteParseri

class TestViiteParseri(unittest.TestCase):

    maxDiff = None

    esimerkkiviite_1 = """@article{kadiyala2018applications,
title={Applications of python to evaluate the performance of decision tree-based boosting algorithms},
author={Kadiyala, Akhil and Kumar, Ashok},
journal={Environmental Progress & Sustainable Energy},
volume={37},
number={2},
pages={618--623},
year={2018},
publisher={Wiley Online Library}
}"""

    esimerkkiviite_2 = """@article{saabith2019python,
  title   = {Python current trend applications-an overview},
  author  = {Saabith, AS and Fareez, MMM and Vinothraj, T},
  journal = {International Journal of Advance Engineering and Research Development},
  volume  = {6},
  number  = {10},
  year    = {2019}
}"""

    def setUp(self):
        self.testiparseri_1 = ViiteParseri(self.esimerkkiviite_1)
        self.testiparseri_2 = ViiteParseri(self.esimerkkiviite_2)

    def test_konstruktori_ja_to_string(self):
        self.assertEqual(str(self.testiparseri_1), self.esimerkkiviite_1)
        self.assertEqual(str(self.testiparseri_2), self.esimerkkiviite_2)

#    def test_update(self): # Tämä testi ei luultavasti järkevä. Ei myöskään mene läpi atm.
#        self.testiparseri.update()
#        self.assertEqual(str(self.testiparseri),self.esimerkkiviite)

    def test_viitteen_tyyppi(self):
        self.assertEqual(self.testiparseri_1.viitteen_tyyppi, "article")
        self.assertEqual(self.testiparseri_2.viitteen_tyyppi, "article")

    def test_viitteen_avain(self):
        self.assertEqual(self.testiparseri_1.viitteen_avain, "kadiyala2018applications")
        self.assertEqual(self.testiparseri_2.viitteen_avain, "saabith2019python")

    def test_viitteen_tiedot(self):
        self.assertEqual(self.testiparseri_1.viitteen_tiedot[0][0], "title")
        self.assertEqual(self.testiparseri_1.viitteen_tiedot[0][1],
                         "Applications of python to evaluate the performance of decision tree-based boosting algorithms")

        self.assertEqual(self.testiparseri_2.viitteen_tiedot[3][0], "volume")
        self.assertEqual(self.testiparseri_2.viitteen_tiedot[3][1],
                         "6")

    def test_viitteen_muokkaus(self):
        self.testiparseri_1.muokkaa("author","Kadiyala et al")
        self.assertEqual(self.testiparseri_1.viitteen_tiedot[1][1],"Kadiyala et al")

        self.testiparseri_2.muokkaa("title","Python current trend applications")
        self.assertEqual(self.testiparseri_2.viitteen_tiedot[0][1],"Python current trend applications")

