from asyncio.log import logger
from viite_editori import ViiteEditori
from console_io import ConsoleIO

class ViiteLibrary:
    def __init__(self):
        self.io = MockConsoleIO()
        self.viite_editori = ViiteEditori(self.io)
        self.next_command = None

    def luo_bib_tiedosto(self, tiedostonimi):
        print(f"Luo Bib Tiedosto kutsuttu: {tiedostonimi}")  # Debug-tuloste
        self.viite_editori.luo_ja_avaa_tiedosto(tiedostonimi)

    def avaa_bib_tiedosto(self, tiedostonimi):
        self.viite_editori.avaa_tiedosto(tiedostonimi)

    def syota_komento(self, komento, syote=None):
        print(f"Syötetään komento: {komento}, syöte: {syote}")
        self.io.syota_komento(komento, syote)
        if komento == "help":
            self.viite_editori.helppi()
        elif self.next_command == "luo":
            self.luo_bib_tiedosto(komento)
            self.next_command = None
        elif komento == "luo":
            self.next_command = "luo"
        elif komento == "avaa":
            tiedostonimi = self.io.lue("Anna avattava tiedosto muodossa sijainti/nimi: ")
            self.avaa_bib_tiedosto(tiedostonimi)
        elif komento == "exit":
            print("Komento 'exit' vastaanotettu.")
        else:
            self.next_command = komento

    #def get_responses(self):
    #    return self.io.responses
    
    def get_standard_output(self):
        return "\n".join(self.io.responses)

    def output_should_contain(self, odotettu):
        tuloste = self.get_standard_output()
        if odotettu not in tuloste:
            raise AssertionError(f"Odotettu teksti '{odotettu}' ei löytynyt tulosteesta:\n{tuloste}")
        logger.info(f"Odotettu teksti '{odotettu}' löytyi tulosteesta.")
        
class MockConsoleIO(ConsoleIO):
    def __init__(self):
        self.commands = []
        self.responses = []

    def kirjoita(self, teksti):
        self.responses.append(teksti)
        print(teksti)  # Debug-tuloste

    def lue(self, kehote):
        if self.commands:
            print(f"Luetaan komento: {self.commands[0]}")  # Debug tuloste
            return self.commands.pop(0)
        return ""

    def syota_komento(self, komento, syote=None):
        print(f"Syötetään komento: {komento}, syöte: {syote}")
        self.commands.append(komento)
        if syote:
            self.commands.append(syote)
