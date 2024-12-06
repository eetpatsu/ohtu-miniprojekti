from viite_editori import ViiteEditori
from console_io import ConsoleIO


def main():
    '''Importtaa tarvittavat luokat ja käynnistää sovelluksen.'''
    console_io = ConsoleIO()
    viite_editori = ViiteEditori(console_io)
    viite_editori.run()


if __name__ == "__main__":
    main()
