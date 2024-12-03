

class ViiteParseri:

    viite_teksti = ''

    viitteen_tyyppi = ''
    viitteen_avain = ''

    viitteen_tiedot = []
    #viitteen_tagit = [] # Taulukko jota tagit tulevat käyttämään jossain vaiheessa.

    def __init__(self, viite_teksti):
        self.viite_teksti = viite_teksti
        self.parse()

    def parse(self):
        """Jäsentää viite_teksti:n sisältämän viitteen ja tallentaa tiedot attribuutteihin."""
        # parse(self)-metodi on tarkoitettu vain olion sisäisen logiikan toimintaan.

        viite_teksti_lista = self.viite_teksti.splitlines()

        self.viitteen_tyyppi = viite_teksti_lista[0][1:viite_teksti_lista[0].index("{")]
        self.viitteen_avain = viite_teksti_lista[0][viite_teksti_lista[0].index("{")+1:viite_teksti_lista[0].index(",")]

        def siivoa_rivi(rivi):
            jaettu_rivi = rivi.split('=')
            jaettu_rivi[1] = jaettu_rivi[1][jaettu_rivi[1].index("{")+1:jaettu_rivi[1].index("}")]
            self.viitteen_tiedot.append(jaettu_rivi)

        for i in range(1,len(viite_teksti_lista)-1):
            siivoa_rivi(viite_teksti_lista[i])


    def update(self): #TODO: Ei vaikuta palauttavan täysin identtistä syötettä mitä se sasi vastaan. Luultavasti testi ei realistinen.
        """Päivittää viite_teksti:n uusille muokatuille attribuutelle."""

        self.viite_teksti = '@' + self.viitteen_tyyppi + '{' + self.viitteen_avain
        for k in self.viitteen_tiedot:
            self.viite_teksti += ',\n' + k[0] + '={' + k[1] + '}'

        self.viite_teksti += '\n}'


    def muokkaa(self, field, uusi_tieto):
        """"Asettaa paramentrin nimisen kentän arvoksi uuden tiedon"""

        field_numero = -1

        for i in range(len(self.viitteen_tiedot)): # TODO: vähemmän ö-luokkaisen näköinen looppi
            if (field == self.viitteen_tiedot[i][0]):
                self.viitteen_tiedot[i][1] = uusi_tieto
                field_numero = i
                break

        self.update()

        # Palauttaa -1, mikäli kyseistä kenttää ei ole olemassakaan.
        # Muussa tapauksessa palauttaa kentän indeksin.
        # Eli jos field_numero >= 0, muokkaus onnistui.
        return field_numero

    def __str__(self):
        return self.viite_teksti
