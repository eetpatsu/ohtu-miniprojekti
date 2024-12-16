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

Avain Ei Kelpaa
    Kaynnista Sovellus Argumenteilla  ${TIEDOSTONIMI}
    Syota Komennot  muokkaaparam  Akuankka
    Tulosteen Tulisi Sisaltaa  Anna muokattavan viitteen avain:
    Tulosteen Tulisi Sisaltaa  Anna parametrin tyyppi:
    Tulosteen Tulisi Sisaltaa  Anna muokattu parametri:
    Tulosteen Tulisi Sisaltaa  Viitettä avaimella 'Akuankka' ei löytynyt.
    [Teardown]  Remove File  ${TIEDOSTONIMI}

Parametrin Tyyppi Ei Kelpaa
    Kaynnista Sovellus Argumenteilla  ${TIEDOSTONIMI}
    Syota Komennot  muokkaaparam  CBH91  yaer
    Tulosteen Tulisi Sisaltaa  Anna muokattavan viitteen avain:
    Tulosteen Tulisi Sisaltaa  Anna parametrin tyyppi:
    Tulosteen Tulisi Sisaltaa  Anna muokattu parametri:
    Tulosteen Tulisi Sisaltaa  Muokkaus epäonnistui tarkista parametrin tyyppi
    [Teardown]  Remove File  ${TIEDOSTONIMI}

Muokataan Viite Avaimella
    Kaynnista Sovellus Argumenteilla  ${TIEDOSTONIMI}
    Syota Data  CBH91
    Syota Data  Lorem
    Syota Data  Ipsum
    Syota Data  Dolor
    Syota Data  2000
    Syota Data  10
    Syota Data  20--25
    Syota Komento  muokkaa
    Tulosteen Tulisi Sisaltaa  Anna muokattavan viitteen avain:
    Tulosteen Tulisi Sisaltaa  Parametrin author nykyinen arvo on: Allan Collins and John Seely Brown and Ann Holum 
    Tulosteen Tulisi Sisaltaa  Anna uusi arvo parametriin author
    Tulosteen Tulisi Sisaltaa  Muokkaus onnistui
    Tulosteen Tulisi Sisaltaa  Parametrin pages nykyinen arvo on: 38--46
    Tulosteen Tulisi Sisaltaa  Anna uusi arvo parametriin pages
    Tulosteen Tulisi Sisaltaa  Muokkaus onnistui
    Syota Komento  tulosta
    Tulosteen Tulisi Sisaltaa  author = {Lorem}
    Tulosteen Tulisi Sisaltaa  title = {Ipsum}
    Tulosteen Tulisi Sisaltaa  journal = {Dolor}
    Tulosteen Tulisi Sisaltaa  year = {2000}
    Tulosteen Tulisi Sisaltaa  volume = {10}
    Tulosteen Tulisi Sisaltaa  pages = {20--25}
    [Teardown]  Remove File  ${TIEDOSTONIMI}
