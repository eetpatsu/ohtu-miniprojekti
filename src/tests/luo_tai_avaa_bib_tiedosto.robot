*** Settings ***
Resource  resource.robot
Library  ../KomentolukijaLibrary.py
Library  OperatingSystem
Test Teardown  Remove File  ${TIEDOSTONIMI}

*** Variables ***
${TIEDOSTONIMI}  testi.bib

*** Test Cases ***
Luo Bib Tiedosto
    Kaynnista Sovellus
    Syota Komennot  luo  ${TIEDOSTONIMI}
    File Should Exist  ${TIEDOSTONIMI}

Yritä Luoda Tiedosto Joka On Jo Olemassa
    Luo Testitiedosto  ${TIEDOSTONIMI}
    File Should Exist  ${TIEDOSTONIMI}
    Kaynnista Sovellus
    Syota Komennot  luo  ${TIEDOSTONIMI}
    Tulosteen Tulisi Sisaltaa  Tapahtui virhe:

Avaa Bib Tiedosto
    Luo Testitiedosto  ${TIEDOSTONIMI}
    Kaynnista Sovellus
    Syota Komennot  avaa  ${TIEDOSTONIMI}
    Tulosteen Tulisi Sisaltaa  Avattiin tiedosto:
    Tulosteen Tulisi Sisaltaa  ${TIEDOSTONIMI}

Yrita Avata Tiedosto Jota Ei Ole Olemassa
    Kaynnista Sovellus
    Syota Komennot  avaa  ${TIEDOSTONIMI}
    Tulosteen Tulisi Sisaltaa  Tapahtui virhe:
