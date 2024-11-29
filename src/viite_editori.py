import os
from pathlib import Path

class ViiteEditori:
    def __init__(self, io):
        self.io = io
    
    def run(self):
        '''Käynnistää sovelluksen ja kysyy komennon.'''
        self.io.kirjoita("Viite-editori   ('exit' sulkee ohjelman)")
        while True:
            # Luetaan käyttäjältä syötettä, kunnes annetaan exit-komento
            syote = self.io.lue("Avaa bib-tiedosto tai luo uusi ('avaa' tai 'luo')?: ")

            # strip poistaa whitespacen, joten ylimääräiset välilyönnit eivät haittaa
            if syote.strip() == "exit":
                break

            if syote.strip() == "avaa":
                tiedostonimi = self.io.lue("Anna avattavan tiedoston sijainti/nimi: ")
                self.avaa_tiedosto(tiedostonimi)

            if syote.strip() == "luo":
                tiedostonimi = self.io.lue("Anna luotavan tiedoston sijainti/nimi (suhteessa tähän hakemistoon): ")
                self.luo_ja_avaa_tiedosto(tiedostonimi)

    def avaa_tiedosto(self, tiedostonimi):
        '''Avaa tiedoston sovelluksen käsiteltäväksi.'''
        tiedosto = None
        if not tiedostonimi.strip().endswith(".bib"):
            tiedostonimi = tiedostonimi + ".bib"
        if Path(tiedostonimi).is_absolute():
            polku = tiedostonimi
        else:
            tyohakemisto_str = os.path.abspath(os.getcwd())
            tyohakemisto_polku = Path(tyohakemisto_str)
            tiedostonimi_polku = Path(tiedostonimi)
            polku = tyohakemisto_polku / tiedostonimi_polku
        try:
            # Avaa tiedoston read/write tilassa tai I/O error, jos tiedostoa ei löydy
            tiedosto = open(polku, "r+")
            self.io.kirjoita("Avataan tiedosto: "+str(polku))
        except IOError:
            self.io.kirjoita("Tapahtui virhe: Tiedostoa "+str(polku)+" ei löynyt.")
        finally:
            # Suljetaan tiedosto lopulta (vaikka tapahtuisi virhe)
            if tiedosto is not None:
                tiedosto.close()

    def luo_ja_avaa_tiedosto(self, tiedostonimi):
        '''Luo uuden .bib-tiedoston ja avaa sen sovelluksen käsiteltäväksi.'''
        tiedosto = None
        if not tiedostonimi.strip().endswith(".bib"):
            tiedostonimi = tiedostonimi + ".bib"
        if Path(tiedostonimi).is_absolute():
            polku = tiedostonimi
        else:
            tyohakemisto_str = os.path.abspath(os.getcwd())
            tyohakemisto_polku = Path(tyohakemisto_str)
            tiedostonimi_polku = Path(tiedostonimi)
            polku = tyohakemisto_polku / tiedostonimi_polku
        try:
            # Luo ja avaa uuden tiedoston read/write tilassa, antaa errorin, jos tiedosto on jo olemassa
            tiedosto = open(polku, "x+")
            self.io.kirjoita("Luodaan tiedosto sijaintiin: "+str(polku))
        except IOError:
            self.io.kirjoita("Tapahtui virhe: Tiedosto "+str(polku)+" on jo olemassa.")
        finally:
            if tiedosto is not None:
                tiedosto.close()
