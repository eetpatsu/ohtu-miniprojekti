*** Settings ***
Library  OperatingSystem
Library   ../ViiteLibrary.py

*** Variables ***
${TIEDOSTONIMI}   testi.bib

*** Test Cases ***
Haetaan Viite Avaimella
    Syota Komento   muokkaa
    Output Should Contain    Anna muokattan viitteen avain
    [Teardown]  Remove File  ${TIEDOSTONIMI}