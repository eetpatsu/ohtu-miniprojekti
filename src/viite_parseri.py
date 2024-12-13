

class ViiteParseri:


    def __init__(self, viite_teksti):
        self.viite_teksti = viite_teksti
        self.viitteen_tyyppi = ''
        self.viitteen_avain = ''
        self.viitteen_tiedot = []
        self.viitteen_tagit = []

        self.parse()


    def parse(self):
        """
        Metodi jäsentää viite_teksit-attribuutin sisältämän bibTeX-viitteen tiedeot
        ja tallentaa ne olion attribuutteihin. Viitteen oikeallisuutta, vaan se on
        olion käyttäjän vastuulla.

        Tämä metodi on tarkoitettu ainoastaan luokan sisäiseen toimintalogiikkaan ja 
        sen käyttö objektin ulkopuolelta ei pitäisi olla tarpeellista.
        """

        viite_teksti_lista = self.viite_teksti.splitlines()

        self.viitteen_tyyppi = viite_teksti_lista[0][1:viite_teksti_lista[0].index("{")].strip()
        self.viitteen_avain = viite_teksti_lista[0][viite_teksti_lista[0].index("{")+1:viite_teksti_lista[0].index(",")].strip() # pylint: disable=line-too-long

        def siivoa_rivi(rivi):
            jaettu_rivi = rivi.split('=')
            jaettu_rivi[0] = jaettu_rivi[0].strip()
            jaettu_rivi[1] = jaettu_rivi[1][jaettu_rivi[1].index("{")+1:jaettu_rivi[1].index("}")].strip()
            self.viitteen_tiedot.append(jaettu_rivi)

        for i in range(1,len(viite_teksti_lista)-1):
            siivoa_rivi(viite_teksti_lista[i])

        def lue_tagit(viimeinen_rivi):
            viimeinen_rivi = viimeinen_rivi[viimeinen_rivi.index("@comment")+8:]
            viimeinen_rivi = viimeinen_rivi[viimeinen_rivi.index("{")+1:viimeinen_rivi.index("}")]

            jaettu_viimeinen_rivi = viimeinen_rivi.split(",")

            for tagi in jaettu_viimeinen_rivi:
                self.viitteen_tagit.append(tagi.strip())

        if "@comment" in viite_teksti_lista[-1]:
            lue_tagit(viite_teksti_lista[-1])


    def update(self):
        """
        Tallentaa objektin attribuuttien arvot BibTeX-muotoiseen merkkijonoon.
        Luotu merkkijono tallennetaan objektin viite_teksti attribuuttiin, josta
        se voidaan palauttaa __str__(self)-metodilla.

        Tämä metodi on tarkoitettu ainoastaan luokan sisäiseen toimintalogiikkaan ja 
        sen käyttö objektin ulkopuolelta ei pitäisi olla tarpeellista.
        """

        self.viite_teksti = ('@'
                             + self.viitteen_tyyppi
                             + '{'
                             + self.viitteen_avain
                             )

        suurin_pituus = 0

        for k in self.viitteen_tiedot:
            suurin_pituus = max(suurin_pituus, len(k))

        def whitespace_fuller (kentta):
            whitespace_pituus = suurin_pituus - len(kentta)
            whitespace = ''
            while whitespace_pituus > 0:
                whitespace += ' '
                whitespace_pituus -= 1
            return whitespace

        for k in self.viitteen_tiedot:
            self.viite_teksti += (',\n  '
                                  + k[0]
                                  + whitespace_fuller(k[0])
                                  + ' = {'
                                  + k[1] + '}')

        self.viite_teksti += '\n}'

        if len(self.viitteen_tagit) > 0:
            self.viite_teksti += '@comment{'

            for i in range( len(self.viitteen_tagit) - 1 ):
                self.viite_teksti += (self.viitteen_tagit[i] + ', ')

            self.viite_teksti += self.viitteen_tagit[-1]


    def muokkaa(self, field, uusi_tieto):
        """"
        Asettaa annetun nimisen kentän arvoksi uuden tiedon.

        Args:
            field (string): Kenttä, jonka tieto halutaan vaihtaa
            uusi_tieto (string): Tieto miksi kyseisen kentän arvo halutaan vaihtaa

        Returns:
            int: -1 mikäli kyseistä kentää ei ole olemassa ja päivity epäonnistui.
                >= 0 mikäli päivitys onnistui.
        """

        field_numero = -1

        for i in range(len(self.viitteen_tiedot)):
            if field == self.viitteen_tiedot[i][0]:
                self.viitteen_tiedot[i][1] = uusi_tieto
                field_numero = i
                break

        self.update()

        return field_numero


    def tagaa(self,tagi):
        """""
        Lisää uuden tagin viitteeseen.

        Args:
            tagi (string): Lisättävän tagin nimi
        """

        self.viitteen_tagit.append(tagi.strip())

        self.update()


    def poista_tagi(self,tagi):
        """"
        Poistaa jo olemassaolevan tagin ja palauttaa tiedon onnistuko poisto.

        Args:
            tagi (string): Poistettavan tagin nimi

        Returns:
            boolean: 'true' mikäli tagi oli olemassa ja poisto onnistui
                'false' mikäli kyseistä tagia ei ollut olemassa
        """

        olemassa = False

        if tagi in self.viitteen_tagit:
            olemassa = True

            self.viitteen_tagit.remove(tagi)

        self.update()

        return olemassa


    def __str__(self):
        return self.viite_teksti
