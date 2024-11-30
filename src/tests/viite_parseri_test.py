import unittest
from viite_parseri import ViiteParseri

class TestViiteParseri(unittest.TestCase):

    esimerkkiviite = """"
        @article{kadiyala2018applications,
            title={Applications of python to evaluate the performance of decision tree-based boosting algorithms},
            author={Kadiyala, Akhil and Kumar, Ashok},
            journal={Environmental Progress \& Sustainable Energy},
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
        
