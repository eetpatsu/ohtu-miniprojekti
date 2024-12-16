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
    Tulosteen Tulisi Sisaltaa  @comment{testitagi}
    [Teardown]  Remove File  ${TIEDOSTONIMI}

Tagin Lisays Avaamatta Tiedostoa
    Kaynnista Sovellus
    Syota Komennot  lisaatagi  CBH91  testitagi
    Tulosteen Tulisi Sisaltaa  Ei avattua tiedostoa. Avaa tiedosto ensin komennolla 'avaa'.
    [Teardown]  Remove File  ${TIEDOSTONIMI}
      
Poista Tagi
    Kaynnista Sovellus Argumenteilla  ${TIEDOSTONIMI}
    Syota Komennot  lisaatagi  CBH91  eka
    Syota Komento  tulosta
    Tulosteen Tulisi Sisaltaa  @comment{eka}
    Syota Komennot  lisaatagi  CBH91  toka
    Syota Komento  tulosta
    Tulosteen tulisi sisaltaa   @comment{eka, toka}
    Syota Komennot  poistatagi  CBH91  toka
    Syota Komento  tulosta
    Tulosteen tulisi sisaltaa   @comment{eka}
    [Teardown]  Remove File  ${TIEDOSTONIMI}