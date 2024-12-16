import unittest
from viite_valitsin import ViiteValitsin

class TestViiteValitsin(unittest.TestCase):

    maxDiff = None

    esimerkkiviitteet = ["""@article{kadiyala2018applications,
title={Applications of python to evaluate the performance of decision tree-based boosting algorithms},
author={Kadiyala, Akhil and Kumar, Ashok},
journal={Environmental Progress & Sustainable Energy},
volume={37},
number={2},
pages={618--623},
year={2018},
publisher={Wiley Online Library}
}""",
"""@article{saabith2019python,
  title   = {Python current trend applications-an overview},
  author  = {Saabith, AS and Fareez, MMM and Vinothraj, T},
  journal = {International Journal of Advance Engineering and Research Development},
  volume  = {6},
  number  = {10},
  year    = {2019}
}@comment{python,katselmus,englannin kielinen}""",
"""@article{larsen2017atomic,
  title={The atomic simulation environment—a Python library for working with atoms},
  author={Larsen, Ask Hjorth and Mortensen, Jens Jorgen and Blomqvist, Jakob and Castelli, Ivano E and Christensen, Rune and Dulak, Marcin and Friis, Jesper and Groves, Michael N and Hammer, Bjork and Hargus, Cory and others},
  journal={Journal of Physics: Condensed Matter},
  volume={29},
  number={27},
  pages={273002},
  year={2017},
  publisher={IOP Publishing}
}@comment{larsen,   fysiikka  , 2017,englannin kielinen}"""]

    def test_tagien_haku(self):
        self.assertEqual(
            ViiteValitsin.hae_tagit(self.esimerkkiviitteet[0]),
            []
        )

        self.assertEqual(
            ViiteValitsin.hae_tagit(self.esimerkkiviitteet[1]),
            ["python","katselmus","englannin kielinen"]
        )

        self.assertEqual(
            ViiteValitsin.hae_tagit(self.esimerkkiviitteet[2]),
            ["larsen","fysiikka","2017","englannin kielinen"]
        )

    def test_tagine_olemassaolo_tiedustelu(self):
        self.assertEqual(
            ViiteValitsin.tagi_tiedustelu(self.esimerkkiviitteet[0],"java"),
            False
        )
        self.assertEqual(
            ViiteValitsin.tagi_tiedustelu(self.esimerkkiviitteet[0],"englannin kielinen"),
            False
        )

        self.assertEqual(
            ViiteValitsin.tagi_tiedustelu(self.esimerkkiviitteet[1],"python"),
            True
        )
        self.assertEqual(
            ViiteValitsin.tagi_tiedustelu(self.esimerkkiviitteet[1],"englannin kielinen"),
            True
        )
        self.assertEqual(
            ViiteValitsin.tagi_tiedustelu(self.esimerkkiviitteet[1],"java"),
            False
        )

        self.assertEqual(
            ViiteValitsin.tagi_tiedustelu(self.esimerkkiviitteet[2],"fysiikka"),
            True
        )
        self.assertEqual(
            ViiteValitsin.tagi_tiedustelu(self.esimerkkiviitteet[1],"englannin kielinen"),
            True
        )
        self.assertEqual(
            ViiteValitsin.tagi_tiedustelu(self.esimerkkiviitteet[2],"python"),
            False
        )
        self.assertEqual(
            ViiteValitsin.tagi_tiedustelu(self.esimerkkiviitteet[2],"java"),
            False
        )


    def test_tagine_olemassaolo_tiedustelu_tyhjalla_viitteella(self):
        self.assertEqual(
            ViiteValitsin.tagi_tiedustelu(self.esimerkkiviitteet[0],""),
            False
        )

        self.assertEqual(
            ViiteValitsin.tagi_tiedustelu(self.esimerkkiviitteet[1],""),
            False
        )

        self.assertEqual(
            ViiteValitsin.tagi_tiedustelu(self.esimerkkiviitteet[2],""),
            False
        )


    def test_viite_listan_seulonta_1_1(self):
        self.assertEqual(
            len(ViiteValitsin.tagi_seulo_viitteet(self.esimerkkiviitteet,"java")),
            0
        )

    def test_viite_listan_seulonta_1_2(self):
        self.assertEqual(
            ViiteValitsin.tagi_seulo_viitteet(self.esimerkkiviitteet,"java"),
            []
        )

    def test_viite_listan_seulonta_2_1(self):
        self.assertEqual(
            len(ViiteValitsin.tagi_seulo_viitteet(self.esimerkkiviitteet,"englannin kielinen")),
            2
        )

    def test_viite_listan_seulonta_2_2(self):

        esimerkkiviitteet_kopio = []
        for i in self.esimerkkiviitteet:
            esimerkkiviitteet_kopio.append(i)
        esimerkkiviitteet_kopio.pop(0)

        self.assertEqual(
            ViiteValitsin.tagi_seulo_viitteet(self.esimerkkiviitteet,"englannin kielinen"),
            esimerkkiviitteet_kopio
        )

    def test_viite_listan_seulonta_3_1(self):
        self.assertEqual(
            len(ViiteValitsin.tagi_seulo_viitteet(self.esimerkkiviitteet,"python")),
            1
        )

    def test_viite_listan_seulonta_3_2(self):

        esimerkkiviitteet_kopio = []
        for i in self.esimerkkiviitteet:
            esimerkkiviitteet_kopio.append(i)
        esimerkkiviitteet_kopio.pop(2)
        esimerkkiviitteet_kopio.pop(0)

        self.assertEqual(
            ViiteValitsin.tagi_seulo_viitteet(self.esimerkkiviitteet,"python"),
            esimerkkiviitteet_kopio
        )
