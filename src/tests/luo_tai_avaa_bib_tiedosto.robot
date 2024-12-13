*** Settings ***
Resource  resource.robot
Library  ../ViiteLibrary.py
Library  OperatingSystem
Library  String  # Tarvitaan tulosteen tarkistamiseen

*** Variables ***
${TIEDOSTONIMI}  test.bib

*** Test Cases ***
Luo Bib Tiedosto
    Syota Komento  luo
    Syota Komento  ${TIEDOSTONIMI}
    File Should Exist  ${TIEDOSTONIMI}
    [Teardown]  Remove File  ${TIEDOSTONIMI}

Yritä Luoda Tiedosto Joka On Jo Olemassa
    Syota Komento  luo
    Syota Komento  ${TIEDOSTONIMI}
    File Should Exist  ${TIEDOSTONIMI}
    Syota Komento  luo
    Syota Komento  ${TIEDOSTONIMI}
    Output Should Contain  Tapahtui virhe:
    [Teardown]  Remove File  ${TIEDOSTONIMI}

Avaa Bib Tiedosto
    Luo Testitiedosto
    Syota Komento  avaa
    Syota Komento  ${TIEDOSTONIMI}
    Output Should Contain  Avattiin tiedosto:
    Output Should Contain  ${TIEDOSTONIMI}
    [Teardown]  Remove File  ${TIEDOSTONIMI}

Yrita Avata Tiedosto Jota Ei Ole Olemassa
    Syota Komento  avaa
    Syota Komento  ${TIEDOSTONIMI}
    Output Should Contain  Tapahtui virhe:
