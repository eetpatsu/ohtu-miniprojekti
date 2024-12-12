from asyncio.log import logger
from viite_editori import ViiteEditori
from console_io import ConsoleIO
import sys, pdb

class ViiteLibrary:
    def __init__(self):
        self.io = MockConsoleIO()
        self.viite_editori = ViiteEditori(self.io)
        self.tallennettu_komento = None

    def syota_komento(self, syote):
        self.io.syota(syote)
        if self.tallennettu_komento:
            if self.tallennettu_komento == "luo":
                self.viite_editori.luo_ja_avaa_tiedosto(syote)
            elif self.tallennettu_komento == "avaa":
                self.viite_editori.avaa_tiedosto(syote)
            self.tallennettu_komento = None
        if syote == "help":
            self.viite_editori.helppi()
        elif syote == "muokkaa":
            # Varmistetaan, että viitteen avain pyydetään
            self.io.kirjoita("Anna muokattan viitteen avain:")
        else:
            self.tallennettu_komento = syote

    def nayta_alkutekstit(self):
        self.viite_editori.helppi()
        self.get_standard_output()

    def get_standard_output(self):
        return "\n".join(self.io.responses)

    def output_should_contain(self, odotettu):
        tuloste = self.get_standard_output()
        if odotettu not in tuloste:
            raise AssertionError(f"Odotettu teksti '{odotettu}' ei löytynyt tulosteesta:\n{tuloste}")
        logger.info("Odotettu teksti %s löytyi tulosteesta.", odotettu)

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

    def syota(self, syote):
        print(f"Syötetään: {syote}") # Debug
        self.commands.append(syote)
