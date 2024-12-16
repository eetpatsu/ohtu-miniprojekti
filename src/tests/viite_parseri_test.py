import unittest
from viite_parseri import ViiteParseri

class TestViiteParseri(unittest.TestCase):

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
}""",
"""@article{larsen2017atomic,
  title={The atomic simulation environment—a Python library for working with atoms},
  author={Larsen, Ask Hjorth and Mortensen, Jens Jorgen and Blomqvist, Jakob and Castelli, Ivano E and Christensen, Rune and Dulak, Marcin and Friis, Jesper and Groves, Michael N and Hammer, Bjork and Hargus, Cory and others},
  journal={Journal of Physics: Condensed Matter},
  volume={29},
  number={27},
  pages={273002},
  year={2017},
  publisher={IOP Publishing}
}@comment{larsen,   fysiikka  , 2017}"""]


    esimerkkiviitteet_to_string = ["""@article{kadiyala2018applications,
  title     = {Applications of python to evaluate the performance of decision tree-based boosting algorithms},
  author    = {Kadiyala, Akhil and Kumar, Ashok},
  journal   = {Environmental Progress & Sustainable Energy},
  volume    = {37},
  number    = {2},
  pages     = {618--623},
  year      = {2018},
  publisher = {Wiley Online Library}
}""",
"""@article{saabith2019python,
  title   = {Python current trend applications-an overview},
  author  = {Saabith, AS and Fareez, MMM and Vinothraj, T},
  journal = {International Journal of Advance Engineering and Research Development},
  volume  = {6},
  number  = {10},
  year    = {2019}
}""",
"""@article{larsen2017atomic,
  title     = {The atomic simulation environment—a Python library for working with atoms},
  author    = {Larsen, Ask Hjorth and Mortensen, Jens Jorgen and Blomqvist, Jakob and Castelli, Ivano E and Christensen, Rune and Dulak, Marcin and Friis, Jesper and Groves, Michael N and Hammer, Bjork and Hargus, Cory and others},
  journal   = {Journal of Physics: Condensed Matter},
  volume    = {29},
  number    = {27},
  pages     = {273002},
  year      = {2017},
  publisher = {IOP Publishing}
}@comment{larsen, fysiikka, 2017}"""]


    def setUp(self):
        self.testiparserit = [
            ViiteParseri(self.esimerkkiviitteet[0]),
            ViiteParseri(self.esimerkkiviitteet[1]),
            ViiteParseri(self.esimerkkiviitteet[2])
        ]

    # Konstruktori testit
    def test_konstruktori_0(self):
        self.assertEqual(self.testiparserit[0].viite_teksti, self.esimerkkiviitteet[0])
    def test_konstruktori_1(self):
        self.assertEqual(self.testiparserit[1].viite_teksti, self.esimerkkiviitteet[1])
    def test_konstruktori_2(self):
        self.assertEqual(self.testiparserit[2].viite_teksti, self.esimerkkiviitteet[2])

    # __str__()-, parse()- ja update()-metodien tesit.
    def test_to_string_0(self):
        self.assertEqual(str(self.testiparserit[0]), self.esimerkkiviitteet_to_string[0])
    def test_to_string_1(self):
        self.assertEqual(str(self.testiparserit[1]), self.esimerkkiviitteet_to_string[1])
    def test_to_string_2(self):
        self.assertEqual(str(self.testiparserit[2]), self.esimerkkiviitteet_to_string[2])

    # Olion attribuuttitestit.
    def test_viitteen_tyyppi_0(self):
        self.assertEqual(self.testiparserit[0].viitteen_tyyppi, "article")
    def test_viitteen_tyyppi_1(self):
        self.assertEqual(self.testiparserit[1].viitteen_tyyppi, "article")
    def test_viitteen_tyyppi_2(self):
        self.assertEqual(self.testiparserit[2].viitteen_tyyppi, "article")

    def test_viitteen_avain_0(self):
        self.assertEqual(self.testiparserit[0].viitteen_avain, "kadiyala2018applications")
    def test_viitteen_avain_1(self):
        self.assertEqual(self.testiparserit[1].viitteen_avain, "saabith2019python")
    def test_viitteen_avain_2(self):
        self.assertEqual(self.testiparserit[2].viitteen_avain, "larsen2017atomic")

    def test_viitteen_tiedot_0(self):
        self.assertEqual(self.testiparserit[0].viitteen_tiedot[0][0], "title")
        self.assertEqual(self.testiparserit[0].viitteen_tiedot[0][1], "Applications of python to evaluate the performance of decision tree-based boosting algorithms")
    def test_viitteen_tiedot_1(self):
        self.assertEqual(self.testiparserit[1].viitteen_tiedot[3][0], "volume")
        self.assertEqual(self.testiparserit[1].viitteen_tiedot[3][1], "6")
    def test_viitteen_tiedot_2(self):
        self.assertEqual(self.testiparserit[2].viitteen_tiedot[5][0], "pages")
        self.assertEqual(self.testiparserit[2].viitteen_tiedot[5][1], "273002")

    # Viitteen tietojen muokkaus testit.
    def test_viitteen_muokkaus_0(self):
        self.testiparserit[0].muokkaa("author","Kadiyala et al")
        self.assertEqual(self.testiparserit[0].viitteen_tiedot[1][1],"Kadiyala et al")
    def test_viitteen_muokkaus_1(self):
        self.testiparserit[1].muokkaa("title","Python current trend applications")
        self.assertEqual(self.testiparserit[1].viitteen_tiedot[0][1],"Python current trend applications")
    def test_viitteen_muokkaus_2(self):
        self.testiparserit[2].muokkaa("pages","273--275")
        self.assertEqual(self.testiparserit[2].viitteen_tiedot[5][1],"273--275")

    # Tagien käsittelytestit
    def test_viitteen_tagien_luku(self):
        self.assertEqual(self.testiparserit[2].viitteen_tagit[0],"larsen")
        self.assertEqual(self.testiparserit[2].viitteen_tagit[1],"fysiikka")
        self.assertEqual(self.testiparserit[2].viitteen_tagit[2],"2017")

    def test_tagien_lisaus_0(self): # Lisäys, ei listaus. Ääkkösongelmia nimeämisessä.
        self.testiparserit[0].tagaa("   python     ")
        self.assertEqual(self.testiparserit[0].viitteen_tagit[0],"python")
    def test_tagien_lisaus_1(self): # Lisäys, ei listaus. Ääkkösongelmia nimeämisessä.
        self.testiparserit[1].tagaa("trend overview")
        self.assertEqual(self.testiparserit[1].viitteen_tagit[0],"trend overview")
    def test_tagien_lisaus_2(self): # Lisäys, ei listaus. Ääkkösongelmia nimeämisessä.
        self.testiparserit[2].tagaa("python")
        self.assertEqual(self.testiparserit[2].viitteen_tagit[3],"python")

    def test_tagien_poisto(self):
        self.testiparserit[2].poista_tagi("fysiikka")
        self.assertEqual(self.testiparserit[2].viitteen_tagit[1],"2017")

    def test_usean_tagin_lisaus_0(self): # Lisäys, ei listaus. Ääkkösongelmia nimeämisessä.
        self.testiparserit[0].tagaa("   python     ")
        self.testiparserit[0].tagaa("enviromentalism")
        self.assertEqual(self.testiparserit[0].viitteen_tagit[0],"python")
        self.assertEqual(self.testiparserit[0].viitteen_tagit[1],"enviromentalism")
    def test_usean_tagin_lisaus_1(self): # Lisäys, ei listaus. Ääkkösongelmia nimeämisessä.
        self.testiparserit[1].tagaa("overview")
        self.testiparserit[1].tagaa("engineering journal")
        self.assertEqual(self.testiparserit[1].viitteen_tagit[0],"overview")
        self.assertEqual(self.testiparserit[1].viitteen_tagit[1],"engineering journal")

    # Usean toiminnon yhteistestit.
    def test_perattainen_tagin_lisaus_ja_muokkaus(self): # Lisäys, ei listaus. Ääkkösongelmia nimeämisessä.
        self.testiparserit[0].tagaa("   python     ")
        self.assertEqual(self.testiparserit[0].viitteen_tagit[0],"python")
        self.testiparserit[0].muokkaa("author","Kadiyala et al")
        self.assertEqual(self.testiparserit[0].viitteen_tiedot[1][1],"Kadiyala et al")

    def test_kaikkien_tagien_poisto(self):
        self.testiparserit[2].poista_tagi("fysiikka")
        self.testiparserit[2].poista_tagi("2017")
        self.testiparserit[2].poista_tagi("larsen")
        self.assertEqual(len(self.testiparserit[2].viitteen_tagit),0)

    def test_kaikkien_tagien_poisto_ja_muokkaus(self):
        self.testiparserit[2].poista_tagi("fysiikka")
        self.testiparserit[2].poista_tagi("2017")
        self.testiparserit[2].poista_tagi("larsen")
        self.assertEqual(len(self.testiparserit[2].viitteen_tagit),0)
        self.testiparserit[2].muokkaa("pages","273--275")
        self.assertEqual(self.testiparserit[2].viitteen_tiedot[5][1],"273--275")
