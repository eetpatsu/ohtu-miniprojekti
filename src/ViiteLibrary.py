from viite_editori import ViiteEditori
from console_io import ConsoleIO

class ViiteLibrary:
    def __init__(self):
        self.io = ConsoleIO()
        self.viite_editori = ViiteEditori(self.io)

    def luo_bib_tiedosto(self, tiedostonimi):
        self.viite_editori.luo_ja_avaa_tiedosto(tiedostonimi)
    
    def avaa_bib_tiedosto(self, tiedostonimi):
        self.viite_editori.avaa_tiedosto(tiedostonimi)
