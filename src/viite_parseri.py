

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
        """Jäsentää viite_teksti-muuttujan sisältämän viitteen ja tallentaa tiedot haluttuihin attribuutteihin."""

        viite_teksti_lista = self.viite_teksti.splitlines()

        self.viitteen_tyyppi = viite_teksti_lista[0][1:viite_teksti_lista[0].index("{")]
        self.viitteen_avain = viite_teksti_lista[0][viite_teksti_lista[0].index("{")+1:viite_teksti_lista[0].index(",")]

        def siivoa_rivi(rivi):
            jaettu_rivi = rivi.split('=')
            jaettu_rivi[1] = jaettu_rivi[1][jaettu_rivi[1].index("{")+1:jaettu_rivi[1].index("}")]
            self.viitteen_tiedot.append(jaettu_rivi)

        for i in range(1,len(viite_teksti_lista)-1):
            siivoa_rivi(viite_teksti_lista[i])


    # def update():
        # Funktio tallentaa kaikki objektin attribuutit
        # 'viite_teksti' attribuuttiin.

    def __str__(self):
        # update(self)
        return self.viite_teksti
