*** Settings ***
Library   ../KomentolukijaLibrary.py
Library  OperatingSystem
Library  String
Test Timeout  5s

*** Variables ***
${TIEDOSTONIMI}   test.bib

${OHJETEKSTI}     \nKomennot:\nhelp\t\ttulostaa tämän viestin\nexit\t\tpoistuu ohjelmasta\navaa\t\tavaa bib-tiedoston\nluo\t\tluo bib-tiedoston\ntulosta\t\ttulostaa aktiivisen bib-tiedoston sisällön\nsyota\t\ttallentaa bib-dataa aktiiviseen bib-tiedostoon\nmuokkaa\t\tmuokkaa valitun viitteen parametreja\nmuokkaaparam\tmuokkaa valitun viitteen haluttua parametria\nlisaatagi\tlisää halutun tagin\npoistatagi\tpoistaa halutun tagin\n


*** Test Cases ***
Help Tulostuu Ohjelman Alkuun
    Kaynnista Sovellus
    Tulosteen Tulisi Sisaltaa  ${OHJETEKSTI}

Testaa Help Komento
    Kaynnista Sovellus
    Syota Komento  help
    Tulosteen Tulisi Sisaltaa  ${OHJETEKSTI}
