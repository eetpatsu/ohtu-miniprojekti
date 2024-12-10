*** Settings ***
Library   ../ViiteLibrary.py
Library   OperatingSystem
Test Timeout   5s

*** Variables ***
${TIEDOSTONIMI}   test.bib

*** Test Cases ***
Help Komento Tulostaa Oikein
    Syotetaan Komento  help
    Varmista Tulostus Sisaltaa  Komennot:
    Varmista Tulostus Sisaltaa  help\t\ttulostaa tämän viestin
    Varmista Tulostus Sisaltaa  exit\t\tpoistuu ohjelmasta
    Varmista Tulostus Sisaltaa  avaa\t\tavaa bib-tiedoston
    Varmista Tulostus Sisaltaa  luo\t\tluo bib-tiedoston
    Varmista Tulostus Sisaltaa  tulosta\t\ttulostaa aktiivisen bib-tiedoston sisällön
    Varmista Tulostus Sisaltaa  syota\t\ttallentaa bib-dataa aktiiviseen bib-tiedostoon
    Varmista Tulostus Sisaltaa  muokkaa\t\tmuokkaa valitun viitteen haluttua parametria

*** Keywords ***
Syotetaan Komento
    [Arguments]  ${komento}  ${syote}=None
    ViiteLibrary.syota_komento  ${komento}  ${syote}

Varmista Tulostus Sisaltaa
    [Arguments]  ${teksti}
    ${responses}=  Get Responses
    Should Not Be Empty  ${responses}  # Varmistetaan, että responses ei ole tyhjä
    Should Contain  ${responses[-1]}  ${teksti}
