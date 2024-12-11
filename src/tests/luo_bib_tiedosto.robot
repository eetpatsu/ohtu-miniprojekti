*** Settings ***
Library   ../ViiteLibrary.py
Library  OperatingSystem
Library  String  # Tarvitaan tulosteen tarkistamiseen

*** Variables ***
${TIEDOSTONIMI}   test.bib

*** Test Cases ***
#Luo Bib Tiedosto
    #Luo Bib Tiedosto  ${TIEDOSTONIMI}
    #File Should Exist  ${TIEDOSTONIMI}
    #[Teardown]  Remove File  ${TIEDOSTONIMI}

Luo Bib Tiedosto Syottamalla
    Syota Komento  luo
    Syota Komento  ${TIEDOSTONIMI}
    Syota Komento  exit
    File Should Exist  ${TIEDOSTONIMI}
    [Teardown]  Remove File  ${TIEDOSTONIMI}
