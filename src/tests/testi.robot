*** Settings ***
Library  OperatingSystem

*** Variables ***
${GREETING}  Hello world!

*** Test Cases ***
Terve maailma
    Log  ${GREETING}
    Should Be Equal As Strings  ${GREETING}  Hello world!