
class ViiteValitsin:

    @staticmethod
    def hae_tagit(viite):

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

        tagit = ViiteValitsin.hae_tagit(viite)

        for tagi in tagit:
            if tiedusteltu_tagi == tagi:
                return True

        return False

    @staticmethod
    def tagi_seulo_viitteet(viite_lista,tagi): # TODO: Tämä metodi ei toimi oikein. Loopin logiikka rikki.

        indeksi = 0

        while indeksi<len(viite_lista):
            if ViiteValitsin.tagi_tiedustelu(viite_lista[indeksi],tagi):
                indeksi += 1
            else:
                viite_lista.pop(indeksi)

        return viite_lista
