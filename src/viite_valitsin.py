
class ViiteValitsin:

    @staticmethod
    def hae_tagit(viite):
        """
        Palauttaa listana kaikki parametrinä annetun viitteen sisältämät tagit.
        Metodi ei sisällä syötteen oikeellisuuden tarkastusta.
        
        Args:
            viite (string): BibTeX-muotoinen Viite Editori:n käyttämä viite.
        
            returns:
                [string]: Lista merkkijonoja viite-argumentin sisältämistä tageista.
        """

        viimeinen_rivi = viite.splitlines()[-1]

        if "@comment" in viimeinen_rivi:
            viimeinen_rivi = viimeinen_rivi[viimeinen_rivi.index("@comment")+8:]
            viimeinen_rivi = viimeinen_rivi[viimeinen_rivi.index("{")+1:viimeinen_rivi.index("}")]

            jaettu_viimeinen_rivi = viimeinen_rivi.split(",")

            viitteen_tagit = []

            for tagi in jaettu_viimeinen_rivi:
                viitteen_tagit.append(tagi.strip())

            return viitteen_tagit

        return []

    @staticmethod
    def tagi_tiedustelu(viite,tiedusteltu_tagi):
        """
        Palauttaa tiedon siitä, sisältääkö parametrinä annettu viite toisena
        parametrina annetun tagin. Metodi ei sisällä syötteen oikeellisuuden
        tarkastusta.
        
        Args:
            viite (string): BibTeX-muotoinen Viite Editori:n käyttämä viite.
            tiedusteltu_tagi (string): Tagi, josta halutaan tietää onko se
                toisena parametrinä annetussa viitteesä.
        
        returns:
            boolean: True, jos tagi on viitteessä. False, jso tagi ei ole
                viitteessä.
        """

        if tiedusteltu_tagi == "":
            return False

        tagit = ViiteValitsin.hae_tagit(viite)

        for tagi in tagit:
            if tiedusteltu_tagi == tagi:
                return True

        return False

    @staticmethod
    def tagi_seulo_viitteet(viite_lista,tagi):
        """
        Käy läpi parametrina annetun listan BibTeX muotoisia viitteitä ja
        palauttaa kopion listasta, joka sisältää vain ne viitteet, joissa
        on kyseinen tagi. Metodi ei tarkasta viitteiden oikeellisuutta.
        Toimii seuraavalla tavalla:
        
         # Lista merkkijonoja, joissa BibTex-muotoisia viitteitä.
        viite_lista = [viite_1, viite_2,... ...,viite_n]
        # Tagi, jolla viitteitä etsitään
        tagi = 'python'
        # Kopio alkuperäisestä listasta, jossa vain halutun tagin omaavat viitteet.
        valikoitu_viite_lista = ViiteValitsin.tagi_seulo_viitteet(viite_lista, tagi)

        Args:
            viite_lista[string]: Lista BibTeX-muotoisia Viite Editori:n käyttämiä viiteitä.
            tagi (string): Tagi, jolla viitteitä halutaan valikoida.
        
        returns:
            [string]: Lista kaikista niistä viitteistä, jotka sisältävät halutun tagin.
        """

        viite_lista_kopio = []

        for i in viite_lista:
            viite_lista_kopio.append(i)

        for i in range(len(viite_lista_kopio)-1, -1, -1):
            if not ViiteValitsin.tagi_tiedustelu(viite_lista_kopio[i],tagi):
                viite_lista_kopio.pop(i)

        return viite_lista_kopio
