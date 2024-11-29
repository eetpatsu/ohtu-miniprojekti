class ViiteEditori:
    def __init__(self, io):
        self.io = io
    
    def run(self):
        '''Käynnistää sovelluksen ja kysyy komennon.'''
        self.io.kirjoita("Viite-editori   ('exit' sulkee ohjelman)")
        while True:
            syote = self.io.lue("Avaa bib-tiedosto tai luo uusi ('avaa' tai 'luo')?: ")

            if syote == "exit":
                break

            if syote == "avaa":
                polku = self.io.lue("Anna avattavan tiedoston sijainti/nimi: ")
                self.avaa_tiedosto(polku)

            if syote == "luo":
                polku = self.io.lue("Anna luotavan tiedoston sijainti/nimi: ")
                self.luo_ja_avaa_tiedosto(polku)

    def avaa_tiedosto(self, polku):
        '''Avaa tiedoston sovelluksen käsiteltäväksi.'''
        self.io.kirjoita("Avataan tiedosto: "+polku)

    def luo_ja_avaa_tiedosto(self, polku):
        '''Luo uuden .bib-tiedoston ja avaa sen sovelluksen käsiteltäväksi.'''
        self.io.kirjoita("Luodaan tiedosto sijaintiin: "+polku)
