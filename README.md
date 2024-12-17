# ohtu-miniprojekti
![GHA workflow badge](https://github.com/eetupsutinen/ohtu-miniprojekti/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/eetupsutinen/ohtu-miniprojekti/graph/badge.svg?token=2A06H0INDB)](https://codecov.io/gh/eetupsutinen/ohtu-miniprojekti)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

*Definition of Done: User storyn kuvaama toiminta on mahdollista ja toteutus täyttää hyväksymiskriteerit. Koodille on tehty hyväksymiskriteerejä vastaavat 
yksikkötestit. Toiminnallisuus on esitetty asiakkaalle ja asiakas on sen hyväksynyt.*
  
- Linkki backlogeihin: https://docs.google.com/spreadsheets/d/1OICdx9NOKYG2s7hhRJc7OWvsG8d-jwwOwvamELjMztY/edit?usp=sharing
- Linkki CI-palveluun: https://github.com/eetupsutinen/ohtu-miniprojekti/actions
- Linkki hyväksymistestausraporttiin: https://raw.githack.com/eetupsutinen/ohtu-miniprojekti/main/report.html
- Linkki retrospektiivin muistioon: https://github.com/eetupsutinen/ohtu-miniprojekti/blob/main/retro.md
- Ohjelma on lisensoitu [MIT-lisenssillä](https://raw.githubusercontent.com/eetupsutinen/ohtu-miniprojekti/refs/heads/main/LICENSE).

**Asennus- ja käyttöohje:**

1. Siirry hakemistoon, johon olet ladannut ohjelman. Aja ohjelma terminaalissa (src/index.py).
   - Voit suorittaa kohdan 2 myös antamalla em. komennon argumentiksi haluamasi tiedostonimen (ml. polku tarvittaessa).
2. Avaa
   - olemassaoleva bib-tiedosto komennolla 'avaa' 
   - **tai** luo uusi tiedosto komennolla 'luo'
   - kummassakin tapauksessa syötä tiedostonimi suhteessa polkuun, jossa olet.
3. Käytettävät komennot tulostuvat terminaaliin ohjelman käynnistyessä. Saat ne uudelleen näkyviin komennolla ```help```.
4. Tulosta bib-tiedoston sisältö komennolla 'tulosta'.
5. Lisää lähteitä bib-muodossa komennolla 'syota'
   - voit liittää useita bib-tiedoston rivejä leikepöydältä tai kirjoittaa ne käsin
   - voit lisätä myös rivinvaihtoja haluamallasi tavalla
   - kun olet liittänyt haluamasi rivit, vahvista syötetyt rivit komennolla kirjaamalla **tyhjälle riville** ```valmis```
6. Muokkaa haluamaasi parametria komennolla: ```muokkaaparam```. Seuraa terminaalin ohjeita. (Viitteen "avaimella" tarkoitetaan ensimmäisen rivin '{' ja ',' -symbolien välistä merkkijonoa.)
- esimerkkiviite:
```
@article{kadiyala2018applications,
title={Applications of python to evaluate the performance of decision tree-based boosting algorithms},
author={Kadiyala, Akhil and Kumar, Ashok},
journal={Environmental Progress \& Sustainable Energy},
volume={37},
number={2},
pages={618--623},
year={2018},
publisher={Wiley Online Library}
}
```
7. Ohjattu viitteen muokkaus komennolla: ```muokkaa```. Seuraa terminaalin ohjeita.
8. Lisää haluamasi tunniste viiteelle komennolla: ```lisaatagi```. Ohjeet tulostuvat terminaaliin.
9. Poista tunniste komennolla: ```poistatagi```.
10. Hae viitteitä tunnisteen perusteella: ```etsitagi```.
11. Poistu ohjelmasta komennolla 'exit'
