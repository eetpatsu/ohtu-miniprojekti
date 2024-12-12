*** Settings ***
Library   ../ViiteLibrary.py
Library  OperatingSystem
Library  String

*** Variables ***
${TIEDOSTONIMI}   testi.bib

*** Test Cases ***
Haetaan Viite Avaimella
    Syota Komento   muokkaa
    Output Should Contain    Anna muokattan viitteen avain

*** Keywords ***
Luo Testi Tiedosto
    Create File  ${TIEDOSTONIMI}