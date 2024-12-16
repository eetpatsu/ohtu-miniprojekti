*** Settings ***
Library  OperatingSystem
Library  ../KomentolukijaLibrary.py

*** Keywords ***
Luo Testitiedosto
    [Arguments]  ${tiedostonimi}
    Create File  ${tiedostonimi}  @article{CBH91,\nauthor = {Allan Collins and John Seely Brown and Ann Holum},\ntitle = {Cognitive apprenticeship: making thinking visible},\njournal = {American Educator},\nyear = {1991},\nvolume = {6},\npages = {38--46}\n}\n\n@book{Martin09,\nauthor = {Martin, Robert},\ntitle = {Clean Code: A Handbook of Agile Software Craftsmanship},\nyear = {1888},\npublisher = {Prentice Hall}\n}@comment{testi,tunniste2,ohjelmointi}

Poista Testitiedosto
    [Arguments]  ${tiedostonimi}
    Remove File  ${tiedostonimi}

Syota Komennot
    [Arguments]  ${komento1}  @{komennot}
    FOR  ${komento}  IN  @{komennot}
        Syota Data  ${komento}
    END
    Syota Komento  ${komento1}