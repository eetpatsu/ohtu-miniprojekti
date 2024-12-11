*** Settings ***
Library   ../ViiteLibrary.py
Library  OperatingSystem
Library  String  # Tarvitaan tulosteen tarkistamiseen
Test Timeout  5s

*** Variables ***
${TIEDOSTONIMI}   test.bib

*** Test Cases ***
Luo Bib Tiedosto
    Luo Bib Tiedosto  ${TIEDOSTONIMI}
    File Should Exist  ${TIEDOSTONIMI}
    [Teardown]  Remove File  ${TIEDOSTONIMI}

Luo Bib Tiedosto Syottamalla
    Syotetaan Komento  luo
    Syotetaan Komento  ${TIEDOSTONIMI}
    Syotetaan Komento  exit
    File Should Exist  ${TIEDOSTONIMI}
    [Teardown]  Remove File  ${TIEDOSTONIMI}

*** Keywords ***
Syotetaan Komento
    [Arguments]  ${komento}  ${syote}=None
    Run Keyword  syota_komento  ${komento}  ${syote}
