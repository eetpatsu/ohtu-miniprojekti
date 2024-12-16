from viite_editori import ViiteEditori
from komentolukija import Komentolukija
from console_io import ConsoleIO

class KomentolukijaLibrary:
    def __init__(self):
        self._io = MockConsoleIO()
        self._viite_editori = ViiteEditori(self._io)
        self._komentolukija = Komentolukija(self._io, self._viite_editori)

    def kaynnista_sovellus(self):
        self._komentolukija.viite_editori.helppi()

    def kaynnista_sovellus_argumenteilla(self, argumentit):
        self._komentolukija.viite_editori.parse_argumentti(["sovellus"] + argumentit.split())
        self._komentolukija.viite_editori.helppi()

    def syota_komento(self, komento):
        self._komentolukija.kasittele_syote(komento)

    def syota_data(self, data):
        self._io.syota(data)

    def tulosteen_tulisi_sisaltaa(self, teksti):
        tuloste = self._io.tuloste
        loytyi = False
        for t in tuloste:
            if teksti in t:
                loytyi = True

        if not loytyi:
            raise AssertionError(
                f"Tekstiä \"{teksti}\" ei löydy tulosteesta \"{str(tuloste)}\""
            )

class MockConsoleIO(ConsoleIO):
    def __init__(self):
        self.syotteet = []
        self.tuloste = []

    def kirjoita(self, teksti):
        self.tuloste.append(teksti)
        print(teksti)  # Debug-tuloste

    def lue(self, kehote):
        self.tuloste.append(kehote)
        if self.syotteet:
            print(f"Luetaan komento: {self.syotteet[0]}")  # Debug tuloste
            return self.syotteet.pop(0)
        return ""

    def syota(self, syote):
        print(f"Syötetään: {syote}") # Debug
        self.syotteet.append(syote)
