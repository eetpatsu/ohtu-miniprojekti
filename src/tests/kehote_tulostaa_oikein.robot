*** Settings ***
Library   ../ViiteLibrary.py
Library  OperatingSystem
Library  String  # Tarvitaan tulosteen tarkistamiseen
Test Timeout  5s

*** Variables ***
${TIEDOSTONIMI}   test.bib

${OHJETEKSTI}     \nKomennot:\n\help\t\ttulostaa tämän viestin\n\exit\t\tpoistuu ohjelmasta\n\avaa\t\tavaa bib-tiedoston\n\luo\t\tluo bib-tiedoston\ntulosta\t\ttulostaa aktiivisen bib-tiedoston sisällön\n\syota\t\ttallentaa bib-dataa aktiiviseen bib-tiedostoon\n\muokkaa\t\tmuokkaa valitun viitteen haluttua parametria\n\

*** Test Cases ***
Testaa Help Komento
    Syotetaan Komento  help
    Output Should Contain  ${OHJETEKSTI}

*** Keywords ***
Syotetaan Komento
    [Arguments]  ${syote}
    Run Keyword  syota_komento  ${syote}

