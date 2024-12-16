import sys

class Komentolukija:
    def __init__(self, io, viite_editori):
        self.io = io
        self.viite_editori = viite_editori

    def run(self):
        '''Käynnistää sovelluksen ja kysyy komennon.'''
        self.viite_editori.parse_argumentti(sys.argv)
        self.viite_editori.helppi()
        while True:
            # Luetaan käyttäjältä syötettä, kunnes annetaan exit-komento
            syote_raaka = self.io.lue("Syötä komento. (Listaa komennot syöttämällä help.) > ")
            if self.kasittele_syote(syote_raaka) != 0:
                break

    def kasittele_syote(self, syote_raaka):
        # strip poistaa whitespacen, joten ylimääräiset välilyönnit eivät haittaa
        syote = syote_raaka.strip()
        match syote:
            case "help":
                self.viite_editori.helppi()

            case "exit":
                return -1

            case "avaa":
                tiedostonimi = self.io.lue("Anna avattava tiedosto muodossa sijainti/nimi: ")
                self.viite_editori.avaa_tiedosto(tiedostonimi)

            case "luo":
                tiedostonimi = self.io.lue("Anna luotava tiedoston polku/nimi (suhteessa työhakemistoon): ")
                self.viite_editori.luo_ja_avaa_tiedosto(tiedostonimi)

            case "tulosta":
                self.viite_editori.tulosta_tiedosto()

            case "syota":
                self.viite_editori.syota_bib_viite()

            case "muokkaa":
                viitteen_avain = self.io.lue("Anna muokattavan viitteen avain: ")

            case "muokkaaparam":
                viitteen_avain = self.io.lue("Anna muokattavan viitteen avain: ")
                parametrin_tyyppi = self.io.lue("Anna parametrin tyyppi: ")
                muokattu_parametri = self.io.lue("Anna muokattu parametri: ")
                self.viite_editori.muokkaa_parametri(viitteen_avain, parametrin_tyyppi, muokattu_parametri)

            case "lisaatagi":
                viitteen_avain = self.io.lue("Anna viitteen avain: ")
                lisattava_tag = self.io.lue("Anna lisättävä tagi: ")
                self.viite_editori.lisaa_tagi(viitteen_avain, lisattava_tag)

            case "poistatagi":
                viitteen_avain = self.io.lue("Anna viitteen avain: ")
                poistettava_tagi = self.io.lue("Anna poistettava tagi: ")
                self.viite_editori.poista_tagi(viitteen_avain, poistettava_tagi)

            case _:
                if syote == "":
                    self.io.kirjoita("Tuntematon komento \""+syote+"\"")

        return 0
