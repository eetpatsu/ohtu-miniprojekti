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
    Syota Data  CBH91
    Syota Data  year
    Syota Data  0000
    Syota Komento  muokkaaparam
    Tulosteen Tulisi Sisaltaa  Anna muokattavan viitteen avain:
    Tulosteen Tulisi Sisaltaa  Anna parametrin tyyppi:
    Tulosteen Tulisi Sisaltaa  Anna muokattu parametri:
    Tulosteen Tulisi Sisaltaa  Muokkaus onnistui
    Syota Komento  tulosta
    Tulosteen Tulisi Sisaltaa  year = {0000}
    [Teardown]  Remove File  ${TIEDOSTONIMI}