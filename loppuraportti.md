# Miniprojektin loppuraportti
Opintojakso: TEKA3003 Ohjelmistotuotanto

Työryhmä:
 - Hintikka Olli-Antti
 - Kalliokoski Lasse
 - Laajala Lauri
 - Lehtinen Elias
 - Slutbäck Harri
 - Sutinen Eetu

## Kohdatut ongelmat

Vaikka merkittäviin ongelmiin ei ajauduttu, projektiamme väritti hieman se,
että osalla tiimin jäsenistä oli varsin niukka kokemus Pythonista ja sen
testaamisesta. Ohjelmointikieli valittiin CI-prosessin ja muiden teknisten
syiden takia, koska myös kurssin harjoitustehtävät olivat perustuneet Pythoniin.
Lähtökohta johti muutamia kertoja tilanteisiin, joissa työtunnit hupenivat
yksittäisissä taskeissa uuden opetteluun yrityksen ja erehdyksen kautta.
  
Orientoituminen storysta toiseen ei ollut kaikissa tilanteissa kivutonta.
Pitkälti kukin erikoistui tiimin sisällä niihin aiheisiin joihin rutiinia
muodostui. Se oli monella tapaa hyväkin valinta. Toki pidemmällä aikavälillä
olisi syytä pohtia mahdollisia tilanteeseen liittyviä riskejä - ja menetettyjä
mahdollisuuksia tiimin kokonaisosaamisen parantamiseen.

Ohjelman rakenne ei osoittautunut täysin optimaaliseksi testaamisen kannalta. Se
edellytti refaktorointia, joka olisi osin ollut vältettävissä rakenteen ja
testaustapojen yhteisellä suunnittelulla. Eri tiimiläisillä oli erilaisia
lähestymistapoja varsinkin testaamiseen (yksikkötestaus ja Robot Framework).
Myös tiedostorakenteen suunnitteluun
olisi tullut käyttää hieman aikaa projektin alussa.

## Hyvät käytänteet ja onnistumiset

Fokusoituminen toimivaan ohjelmistoversioon jokaisen sprintin lopussa oli hyvä
periaate. Välillä motivaatiota olisi ollut suuriinkiin määriin muutoksia, mutta
katselmuksen lähestyessä työaikaa hupeni väistämättä testaamiseen ja
projektinhallintaan. 

Livetyöskentely todettiin hyväksi valinnaksi. Siihen varattiin aikaa sekä
sprintin alussa että keskivaiheilla. Projektin loppuvaiheessa kehittyi myös
rohkeus yhteydenottoihin puheella. Jos tiedossa oli, että toisella tiimin
jäsenellä oli aikaisempaa kokemusta tietystä toiminnallisuudesta, muutaman
minuutin keskustelulla saattoi säästyä merkittävästi työaikaa "itseopiskelun"
sijaan. 

Jatkuvan integraation voi todeta onnistuneen hyvin. Yksittäisiä kertoja
CI-palvelu toimi juuri kuten pitääkin, eli ilmoitti syntyneistä ristiriidoista.
Valtaosin kyse oli pienistä staattisen analyysin havaitsemista puutteista. Myös
viimeisessä sprintissä toteutettu rakenteellinen refaktorointi onnistui
aiheuttamatta merkittäviä muutoksia aikaisemmin toteutettuun ohjelmakoodiin.

## Kehittämiskohteet

Vaikka kommunikaatio oli varsin toimivaa, totesimme, että vieläkin rohkeammin
olisi voinut hyödyntää muiden tiimiläisten tukea omassa työskentelyssä. Viestejä
parempana vaihtoehtona voi pitää keskustelua livenä tai puheyhteydellä, vaikka
monissa tilanteissa myös chat oli hyvä valinta.

Ohjelmakoodin dokumentaatioon olisi ollut hyvä sisällyttää selkeämmin metodien
"käyttöohjeita", vaikka uusiin ominaisuuksiin perehdytettiinkin tiimiläisiä
viestien välityksellä. Aika- tai työmääräarviointi hiipui projektin edetessä.
Myös työn edistymisen raportoinnissa oli osin kehitettävää.

Backlogin ajantasaisuudesta voitiin varmistua vastuuhenkilöistä sopimalla.
Toisaalta jokaisen oma-aloitteisuutta olisi voinut lisätäkin, erityisesti työn
edistymisen seurannassa.

## Mitä opittiin, oltaisiin haluttu oppia tai koettiin turhaksi

Pääosalle tuli uutta ja tarpeellista kokemusta Git-projektin toteutuksesta
kollaboraattoreina. Monille kyseessä oli ensimmäinen kokemus ohjelmistotiimin
toimintaperiaatteista. Projekti opetti hahmottamaan muiden tiimiläisten
tuottamaa ohjelmakoodia. Samalla opimme sen, että yksityiskohtien sijaan
tärkeintä oli peruslogiikan ymmärtäminen yhtenäisellä tavalla. Etenkin
yksittäisille henkilöille kokemusta tuli myös backlogin hallinnoinnista ja
sprintin tavoitteiden loppuunsaattamisesta projektinhallinnan näkökulmasta. 

Toisaalta enemmän olisimme voineet oppia Git-versionahallinnasta kehityshaaroja
tai pull request -ominaisuuksia käyttämällä. On selvää, että aikarajoitteiden
vuoksi myös ohjelmointityössä jäi toteuttamatta joitakin kiinnostavia
toiminnallisuuksia (esimerkiksi viitteiden tuonti rajapinnalla). Toisaalta
varsinaisen prosessin näkökulmasta tärkeimmät opit saatiin, eikä päällimmäisenä
ollutkaan tuote itsessään.

Turhaksi koettiin Codecov-toiminto, jossa ilmeni myös epäjohdonmukaisia teknisiä
ongelmia silloin tällöin. Kattavuuden seuranta onnistui 
toki sujuvasti, kun kattavuustestit suoritettiin jokaisen testin jälkeen omilta
työasemilta. Kävimme yksittäisten tiimiläisten kanssa keskusteluja myös Robot
Frameworkin perusideasta. Sen todellista hyötyä oli hieman vaikea sisäistää
syvällisellä tasolla, vaikka projekti olikin hyvä tilaisuus harjaantua
hyväksymistestien laatimisessa.
