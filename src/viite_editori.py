import os
import re
from pathlib import Path
from viite_parseri import ViiteParseri
from viite_valitsin import ViiteValitsin

class ViiteEditori:
    def __init__(self, io):
        self.io = io
        self.aktiivinen_tiedosto = None

    def helppi(self):
        self.io.kirjoita("\nKomennot:\n\
help\t\ttulostaa tämän viestin\n\
exit\t\tpoistuu ohjelmasta\n\
avaa\t\tavaa bib-tiedoston\n\
luo\t\tluo bib-tiedoston\n\
tulosta\t\ttulostaa aktiivisen bib-tiedoston sisällön\n\
syota\t\ttallentaa bib-dataa aktiiviseen bib-tiedostoon\n\
muokkaa\t\tmuokkaa valitun viitteen parametreja\n\
muokkaaparam\tmuokkaa valitun viitteen haluttua parametria\n\
lisaatagi\tlisää halutun tagin\n\
poistatagi\tpoistaa halutun tagin\n\
")
        return 0

    def muuta_bibiksi_ja_absoluuttiseksi(self, tiedostonimi):
        if not tiedostonimi.strip().endswith(".bib"):
            tiedostonimi = tiedostonimi + ".bib"
        if Path(tiedostonimi).is_absolute():
            return Path(tiedostonimi)

        tyohakemisto_str = os.path.abspath(os.getcwd())
        tyohakemisto_polku = Path(tyohakemisto_str)
        tiedostonimi_polku = Path(tiedostonimi)
        return tyohakemisto_polku / tiedostonimi_polku

    def parse_argumentti(self, argumentit):
        if len(argumentit) > 1:
            tiedostonimi = argumentit[1]
            polku = self.muuta_bibiksi_ja_absoluuttiseksi(tiedostonimi)
            if os.path.isfile(polku):
                self.avaa_tiedosto(str(polku))
            else:
                self.luo_ja_avaa_tiedosto(str(polku))

    def avaa_tiedosto(self, tiedostonimi):
        '''Avaa tiedoston sovelluksen käsiteltäväksi.'''
        tiedosto = None
        polku = self.muuta_bibiksi_ja_absoluuttiseksi(tiedostonimi)
        try:
            # Avaa tiedoston read/write tilassa tai I/O error, jos tiedostoa ei löydy
            with open(polku, "r+") as tiedosto:
                self.aktiivinen_tiedosto = polku
                self.io.kirjoita("Avattiin tiedosto: "+str(polku))
        except IOError:
            self.io.kirjoita("Tapahtui virhe: Tiedostoa "+str(polku)+" ei löynyt.")
        finally:
            # Suljetaan tiedosto lopulta (vaikka tapahtuisi virhe)
            if tiedosto is not None:
                tiedosto.close()

    def luo_ja_avaa_tiedosto(self, tiedostonimi):
        '''Luo uuden .bib-tiedoston ja avaa sen sovelluksen käsiteltäväksi.'''
        tiedosto = None
        polku = self.muuta_bibiksi_ja_absoluuttiseksi(tiedostonimi)

        try:
            # Luo ja avaa uuden tiedoston read/write tilassa, antaa errorin, jos tiedosto on jo olemassa
            with open(polku, "x+") as tiedosto:
                self.aktiivinen_tiedosto = polku
                self.io.kirjoita("Luodaan tiedosto sijaintiin: "+str(polku))
        except IOError:
            self.io.kirjoita("Tapahtui virhe: Tiedosto "+str(polku)+" on jo olemassa.")
        finally:
            if tiedosto is not None:
                tiedosto.close()

    def tulosta_tiedosto(self):
        '''Tulostaa avatun tidoston sisällön.(aktiivinen_tiedosto)'''
        if self.aktiivinen_tiedosto is None:
            self.io.kirjoita("Ei avattua tiedostoa. Avaa tiedosto ensin komennolla 'avaa'.")
            return -1

        try:
            with open(self.aktiivinen_tiedosto, "r") as tiedosto:
                sisalto = tiedosto.read()
                self.io.kirjoita(f"Tiedoston {self.aktiivinen_tiedosto.name} sisältö:\n{sisalto}")
                return 0
        except IOError:
            self.io.kirjoita(f"Tapahtui virhe: Tiedostoa {self.aktiivinen_tiedosto} ei voitu lukea.")
            return -1

    def syota_bib_viite(self):
        '''Ottaa käyttäjältä vastaan valmiita viitteitä bib-syntaksissa ja tallentaa aktiiviseen tiedostoon'''
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
        return 0

    def muokkaa_viite(self, viitteen_avain):
        '''Muokkaa valitun viitteen parametreja'''
        if self.aktiivinen_tiedosto is None:
            self.io.kirjoita("Ei avattua tiedostoa. Avaa tiedosto ensin komennolla 'avaa'.")
            return -1

        try:
            with open(self.aktiivinen_tiedosto, "r") as tiedosto:
                viite_alku = tiedosto.read()

            viitteet = self.etsi_viitteet(viite_alku)

            muokattavat_viitteet = []
            for viite in viitteet:
                if viitteen_avain in viite:
                    muokattavat_viitteet.append(viite)
                    break

            if len(muokattavat_viitteet) == 0:
                self.io.kirjoita(f"Viitettä avaimella '{viitteen_avain}' ei löytynyt.")
                return -1

            for muokattava_viite in muokattavat_viitteet:
                parseri = ViiteParseri(muokattava_viite)
                for param, arvo in parseri.viitteen_tiedot:
                    self.io.kirjoita(f"Nykyinen {param}: {arvo}")
                    # Ajetaan self.muokkaa_parametri?
            return 0

        except FileNotFoundError:
            print("Tiedostoa ei löytynyt.")
            return -1

    def muokkaa_parametri(self, viitteen_avain, parametrin_tyyppi, muokattu_parametri):
        '''Muokkaa valitun viitteen haluttua parametriä'''
        if self.aktiivinen_tiedosto is None:
            self.io.kirjoita("Ei avattua tiedostoa. Avaa tiedosto ensin komennolla 'avaa'.")
            return -1

        try:
            with open(self.aktiivinen_tiedosto, "r") as tiedosto:
                viite_alku = tiedosto.read()

            viitteet = self.etsi_viitteet(viite_alku)
            muokattava_viite = self.etsi_viite(viitteet, viitteen_avain)
            if not muokattava_viite:
                return -1

            parseri = ViiteParseri(muokattava_viite)
            tulos = parseri.muokkaa(parametrin_tyyppi, muokattu_parametri)

            viitteet = [viite if viite != muokattava_viite else str(parseri) for viite in viitteet]

            with open(self.aktiivinen_tiedosto, "w") as tiedosto:
                tiedosto.write("\n\n".join(viitteet))

            if tulos >= 0:
                self.io.kirjoita("Muokkaus onnistui")
            else:
                self.io.kirjoita("Muokkaus epäonnistui tarkista parametrin tyyppi")
            return 0

        except FileNotFoundError:
            print("Tiedostoa ei löytynyt.")
            return -1

    def lisaa_tagi(self, viitteen_avain, lisattava_tag):
        '''Lisätään haluttu tagi'''
        if self.aktiivinen_tiedosto is None:
            self.io.kirjoita("Ei avattua tiedostoa. Avaa tiedosto ensin komennolla 'avaa'.")
            return -1

        try:
            with open(self.aktiivinen_tiedosto, "r") as tiedosto:
                viite_alku = tiedosto.read()

            viitteet = self.etsi_viitteet(viite_alku)
            muokattava_viite = self.etsi_viite(viitteet, viitteen_avain)
            if not muokattava_viite:
                return -1

            parseri = ViiteParseri(muokattava_viite)
            parseri.tagaa(lisattava_tag)

            viitteet = [viite if viite != muokattava_viite else str(parseri) for viite in viitteet]

            with open(self.aktiivinen_tiedosto, "w") as tiedosto:
                tiedosto.write("\n\n".join(viitteet))
            return 1

        except FileNotFoundError:
            print("Tiedostoa ei löytynyt.")
            return -1

    def poista_tagi(self, viitteen_avain, poistettava_tagi):
        '''Poistetaan haluttu tagi'''
        if self.aktiivinen_tiedosto is None:
            self.io.kirjoita("Ei avattua tiedostoa. Avaa tiedosto ensin komennolla 'avaa'.")
            return -1

        try:
            with open(self.aktiivinen_tiedosto, "r", encoding="utf-8") as tiedosto:
                viite_alku = tiedosto.read()

            viitteet = self.etsi_viitteet(viite_alku)
            muokattava_viite = self.etsi_viite(viitteet, viitteen_avain)
            if not muokattava_viite:
                return -1

            parseri = ViiteParseri(muokattava_viite)

            parseri.poista_tagi(poistettava_tagi)

            viitteet = [viite if viite != muokattava_viite else str(parseri) for viite in viitteet]

            with open(self.aktiivinen_tiedosto, "w") as tiedosto:
                tiedosto.write("\n\n".join(viitteet))
            return 1

        except FileNotFoundError:
            print("Tiedostoa ei löytynyt.")
            return -1

    def etsi_tagi(self, etsittava_tagi):
        '''Etsitään kaikki viitteet missä on etsittävä tagi'''
        if self.aktiivinen_tiedosto is None:
            self.io.kirjoita("Ei avattua tiedostoa. Avaa tiedosto ensin komennolla 'avaa'.")
            return -1

        try:
            with open(self.aktiivinen_tiedosto, "r", encoding="utf-8") as tiedosto:
                viite_alku = tiedosto.read()

            viitteet = self.etsi_viitteet(viite_alku)

            valikoitu_viite_lista = ViiteValitsin.tagi_seulo_viitteet(viitteet, etsittava_tagi)

            parsitut_viitteet = []
            for viite in valikoitu_viite_lista:
                parseri = ViiteParseri(viite)
                parsitut_viitteet.append(self.muodosta_luettava_viite(parseri))

            # Muodostetaan luettava lista ja tulostetaan
            valmis_lista = "\n\n".join(parsitut_viitteet)
            print(" ")
            self.io.kirjoita(valmis_lista)

            return 1
        except FileNotFoundError:
            print("Tiedostoa ei löytynyt.")
            return -1

    def muodosta_luettava_viite(self, parseri):
        """auttaa etsi_tagi toimintoa tulostamaan halutut viitteet helposti luettavassa muodossa"""
        viite_rivit = [
            f"Tyyppi: {parseri.viitteen_tyyppi}",
            f"Avain: {parseri.viitteen_avain}",
            "Tiedot:"
        ]
        for kentta, arvo in parseri.viitteen_tiedot:
            viite_rivit.append(f"  {kentta}: {arvo}")

        if parseri.viitteen_tagit:
            viite_rivit.append("Tagit: " + ", ".join(parseri.viitteen_tagit))

        return "\n".join(viite_rivit)

    def etsi_viitteet(self, viite_alku):
        """Etsitään ja palautetaan tiedoston viitteet"""
        tiedoston_viitteet = re.split(r"@(a|b|i)", viite_alku)[1:]
        viitteet = []
        for i in range(0, len(tiedoston_viitteet), 2):
            tyyppi = tiedoston_viitteet[i]
            sisalto = tiedoston_viitteet[i + 1].strip()
            viitteet.append(f"@{tyyppi}{sisalto}")
        return viitteet

    def etsi_viite(self, viitteet, viitteen_avain):
        """Etsitään ja palautetaan avainta vastaava viite"""
        avaimen_viite = None
        for viite in viitteet:
            if viitteen_avain in viite:
                avaimen_viite = viite
                return avaimen_viite

        self.io.kirjoita(f"Viitettä avaimella '{viitteen_avain}' ei löytynyt.")
        return avaimen_viite
