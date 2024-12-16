*** Settings ***
Library  OperatingSystem
Library   ../KomentolukijaLibrary.py
Resource  resource.robot
Test Setup  Luo Testitiedosto  ${TIEDOSTONIMI}
Test Teardown  Poista Testitiedosto  ${TIEDOSTONIMI}  

*** Variables ***
${TIEDOSTONIMI}   testi.bib

*** Test Cases ***
Haetaan Viite Avaimella
    Kaynnista Sovellus Argumenteilla  ${TIEDOSTONIMI}
    Syota Komennot  lisaatagi  CBH91  testitagi
    Syota Komento  tulosta
    Tulosteen Tulisi Sisaltaa  testitagi}
    [Teardown]  Remove File  ${TIEDOSTONIMI}