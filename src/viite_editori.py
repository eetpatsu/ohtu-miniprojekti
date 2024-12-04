import os
from pathlib import Path

class ViiteEditori:
    def __init__(self, io):
        self.io = io
        self.aktiivinen_tiedosto = None

    def run(self):
        '''Käynnistää sovelluksen ja kysyy komennon.'''
        self.io.kirjoita("Viite-editori   ('exit' sulkee ohjelman)")
        tiedostonimi = None
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

            if syote.strip() == "tulosta":
                self.Tulosta_tiedosto(tiedostonimi)
            
            if syote.strip() == "syota":
                self.syota_bib_viite()


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
            self.aktiivinen_tiedosto = polku
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
            self.aktiivinen_tiedosto = polku
            tiedosto = open(polku, "x+")
            self.io.kirjoita("Luodaan tiedosto sijaintiin: "+str(polku))
        except IOError:
            self.io.kirjoita("Tapahtui virhe: Tiedosto "+str(polku)+" on jo olemassa.")
        finally:
            if tiedosto is not None:
                tiedosto.close()

    '''Tulostaa avatun tidoston sisällön.(aktiivinen_tiedosto)'''
    def Tulosta_tiedosto(self, tiedostonimi):
        
        if self.aktiivinen_tiedosto is None:
            self.io.kirjoita("Ei avattua tiedostoa. Avaa tiedosto ensin komennolla 'avaa'.")
            return -1
        
        try:
            with open(self.aktiivinen_tiedosto, "r") as tiedosto:
                sisalto = tiedosto.read()
                self.io.kirjoita(f"Tiedoston {self.aktiivinen_tiedosto.name} sisältö:\n{sisalto}")
                return 0
        except IOError:
            self.io.kirjoita(f"Tapahtui virhe: Tiedostoa {self.tiedosto} ei voitu lukea.")
            return -1

    '''Ottaa käyttäjältä vastaan valmiita viitteitä bib-syntaksissa ja tallentaa aktiiviseen tiedostoon'''
    def syota_bib_viite(self):
        if self.aktiivinen_tiedosto is None:
            self.io.kirjoita("Ei avattua tiedostoa. Avaa tiedosto ensin komennolla 'avaa'.")
            return -1
        self.io.kirjoita("Syötä lisättävä bib-data. Lopeta syöttö kirjaamalla tyhjälle riville 'valmis'.")
        rivit = []
        while True:
            rivi = self.io.lue("> ").rstrip()
            if rivi == "valmis":
                break
            rivit.append(rivi)
        
        uusi_data = "\n".join(rivit)
        
        with open(self.aktiivinen_tiedosto, "r") as tiedosto:
            sisalto = tiedosto.read()
        
        if not sisalto.endswith("\n"):
            uusi_data = "\n" + uusi_data
        
        with open(self.aktiivinen_tiedosto, "a") as tiedosto:
            tiedosto.write(uusi_data + "\n\n")  
        
        self.io.kirjoita("Viite lisätty tiedoston loppuun.")