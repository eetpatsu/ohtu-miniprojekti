*** Settings ***
Library  OperatingSystem
Library   ../KomentolukijaLibrary.py
Resource  resource.robot
Test Setup  Luo Testitiedosto  ${TIEDOSTONIMI}
Test Teardown  Poista Testitiedosto  ${TIEDOSTONIMI}  

*** Variables ***
${TIEDOSTONIMI}   testi.bib

*** Test Cases ***
Lisaa Tagi
    Kaynnista Sovellus Argumenteilla  ${TIEDOSTONIMI}
    Syota Komennot  lisaatagi  CBH91  testitagi
    Syota Komento  tulosta
    Tulosteen Tulisi Sisaltaa  testitagi}
    [Teardown]  Remove File  ${TIEDOSTONIMI}

Tagin Lisays Avaamatta Tiedostoa
    Kaynnista Sovellus
    Syota Komennot   lisaatagi  CBH91  testitagi
    Tulosteen Tulisi Sisaltaa  Ei avattua tiedostoa. Avaa tiedosto ensin komennolla 'avaa'.