from viite_editori import ViiteEditori
from komentolukija import Komentolukija
from console_io import ConsoleIO


def main():
    '''Importtaa tarvittavat luokat ja käynnistää sovelluksen.'''
    console_io = ConsoleIO()
    viite_editori = ViiteEditori(console_io)
    komentolukija = Komentolukija(console_io, viite_editori)
    komentolukija.run()


if __name__ == "__main__":
    main()
