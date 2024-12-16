import re
from viite_editori import ViiteEditori
from komentolukija import Komentolukija
from console_io import ConsoleIO

class KomentolukijaLibrary:
    def __init__(self):
        self._io = MockConsoleIO()
        self._viite_editori = ViiteEditori(self._io)
        self._komentolukija = Komentolukija(self._io, self._viite_editori)

    def kaynnista_sovellus(self):
        '''Kutsuu samoja funktioita kuin sovellus käynnistettäessä. Ei kuitenkaan oikeasti käynnistä mitään.'''
        self._komentolukija.viite_editori.helppi()

    def kaynnista_sovellus_argumenteilla(self, argumentit):
        '''Sama kuin edellinen, mutta tekee samat asiat kuin sovellus käynnistettäessä samoilla argumenteilla.'''
        self._komentolukija.viite_editori.parse_argumentti(["sovellus"] + argumentit.split())
        self._komentolukija.viite_editori.helppi()

    def syota_komento(self, komento):
        '''Laittaa sovelluksen käsittelemään annetun komennon. 
        Jos komennon seurauksena kysytään käyttäjältä lisää parametreja,
        ne täytyy syöttää ennen funktion kutsumista. (Katso resource.robot "Syota Komennot")'''
        self._komentolukija.kasittele_syote(komento)

    def syota_data(self, data):
        '''Syöttää käyttäjän antamaa dataa valmiiksi. Ohjelma lukee näitä sitä mukaa kun io:n funktiota "lue" kutsutaan.'''
        if data == "ENTER": # Jos syötetään "ENTER", ohjelma käyttäytyy kuin käyttäjä olisi painanut enter ilman inputtia
            data = ""
        self._io.syota(data)

    def tulosteen_tulisi_sisaltaa(self, teksti):
        '''Tarkistaa löytyykö tulosteesta (mistään) annettua merkkijonoa. Yhden välilyönnin tilalla sallitaan enemmänkin tilaa.'''
        teksti_regex = teksti.replace(" ", "\\s+")
        teksti_regex = teksti_regex.replace("{", "\\{")
        teksti_regex = teksti_regex.replace("}", "\\}")
        teksti_regex = teksti_regex.replace("[", "\\[")
        teksti_regex = teksti_regex.replace("]", "\\]")
        tuloste = self._io.tuloste
        loytyi = False
        for t in tuloste:
            if re.search(teksti_regex, t): # Etsitään tekstillä, mutta niin että välilyöntejä voi olla enemmän
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
        '''Kirjoittaa tuloste-taulukkoon tekstin, jonka ohjelma tulostaisi konsoliin.'''
        self.tuloste.append(teksti)
        print(teksti)  # Debug-tuloste

    def lue(self, kehote):
        '''Ottaa syotteet-taulukosta ensimmäisen alkion pois ja palauttaa sen kutsuvalle ohjelmalle.'''
        self.tuloste.append(kehote)
        if self.syotteet:
            print(f"Luetaan komento: {self.syotteet[0]}")  # Debug tuloste
            return self.syotteet.pop(0)
        return ""

    def syota(self, syote):
        '''Kirjoittaa annetun syötteen taulukkoon syotteet. Muuta ei tehdä.
        Ohjelma lukee seuraavan komennon syotteet-taulukosta aina kun funktiota "lue" kutsutaan.'''
        print(f"Syötetään: {syote}") # Debug
        self.syotteet.append(syote)
