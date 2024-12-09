*** Settings ***
Library  ../ViiteLibrary.py
Library  OperatingSystem

*** Variables ***
${TIEDOSTONIMI}  test.bib

*** Test Cases ***
Luo Bib Tiedosto
    Luo Bib Tiedosto  ${TIEDOSTONIMI}
    File Should Exist  ${TIEDOSTONIMI}
    [Teardown]  Remove File  ${TIEDOSTONIMI}
