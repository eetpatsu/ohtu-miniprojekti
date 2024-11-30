

class ViiteParseri:

    viite_teksti = ''

    viitteen_avain = ''
    viitteen_tyyppi = ''
    # Viitteen arvot kannattanee tallentaa listaan,
    # joka koostuu kaksialkoisista listoista. Hashmapit
    # ei pidä yllä niiden järjestystä. Ehkä. Sisäinen
    # toiminta hieman auki vielä.

    def __init__(self, viite_teksti):
        self.viite_teksti = viite_teksti
        # parse(self)

    # def parse():
        # Funktio käy läpi kaikki konstuktorissa annetun
        # viitteen arvot ja tallentaa ne listaa, joka koostuu
        # kahden mittaisista listoista.

    # def update():
        # Funktio tallentaa kaikki objektin attribuutit
        # 'viite_teksti' attribuuttiin.

    def __str__(self):
        # update(self)
        return self.viite_teksti