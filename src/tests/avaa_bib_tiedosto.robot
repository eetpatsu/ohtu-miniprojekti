*** Settings ***
Library  ../ViiteLibrary.py
Library  OperatingSystem

*** Variables ***
${TIEDOSTONIMI}  test.bib
${TIEDOSTON_SISALTO}  @article{example,\n  author = {John Doe},\n  title = {Example Title},\n  year = {2024}\n}

*** Test Cases ***
#Avaa Bib Tiedosto
    #Luo Testi Tiedosto
    #Avaa Bib Tiedosto  ${TIEDOSTONIMI}
    #[Teardown]  Remove File  ${TIEDOSTONIMI}

*** Keywords ***
Luo Testi Tiedosto
    Create File  ${TIEDOSTONIMI}  ${TIEDOSTON_SISALTO}

Varmista Tiedoston Sisältö
    ${sisalto}=  Get File  ${TIEDOSTONIMI}
    Should Contain  ${sisalto}  ${TIEDOSTON_SISALTO}