*** Settings ***
Library  ../ViiteLibrary.py
Library  OperatingSystem
Library  String  # Tarvitaan tulosteen tarkistamiseen

*** Variables ***
${TIEDOSTONIMI}  test.bib

${ODOTETTU_TULOSTUS}  Avattiin tiedosto:

*** Test Cases ***
Luo Bib Tiedosto
    Syota Komento  luo
    Syota Komento  ${TIEDOSTONIMI}
    File Should Exist  ${TIEDOSTONIMI}
    [Teardown]  Remove File  ${TIEDOSTONIMI}

Avaa Bib Tiedosto
    Luo Testi Tiedosto
    Syota Komento  avaa
    Syota Komento  ${TIEDOSTONIMI}
    Output Should Contain  ${ODOTETTU_TULOSTUS}
    Output Should Contain  ${TIEDOSTONIMI}
    [Teardown]  Remove File  ${TIEDOSTONIMI}

*** Keywords ***
Luo Testi Tiedosto
    Create File  ${TIEDOSTONIMI}
