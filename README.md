# ohtu-miniprojekti
![GHA workflow badge](https://github.com/eetupsutinen/ohtu-miniprojekti/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/eetupsutinen/ohtu-miniprojekti/graph/badge.svg?token=2A06H0INDB)](https://codecov.io/gh/eetupsutinen/ohtu-miniprojekti)

*Definition of Done: User storyn kuvaama toiminta on mahdollista ja toteutus täyttää hyväksymiskriteerit. Koodille on tehty hyväksymiskriteerejä vastaavat 
yksikkötestit. Toiminnallisuus on esitetty asiakkaalle ja asiakas on sen hyväksynyt.*
  
- Linkki backlogeihin: https://docs.google.com/spreadsheets/d/1OICdx9NOKYG2s7hhRJc7OWvsG8d-jwwOwvamELjMztY/edit?usp=sharing
- Linkki CI-palveluun: https://github.com/eetupsutinen/ohtu-miniprojekti/actions
- Ohjelma on lisensoitu [MIT-lisenssillä](https://raw.githubusercontent.com/eetupsutinen/ohtu-miniprojekti/refs/heads/main/LICENSE).

**Asennus- ja käyttöohje:**

1. Siirry hakemistoon, johon olet ladannut ohjelman. Aja ohjelma terminaalissa (src/index.py).
2. Avaa
   - olemassaoleva bib-tiedosto komennolla 'avaa' 
   - **tai** luo uusi tiedosto komennolla 'luo'
   - kummassakin tapauksessa syötä tiedostonimi suhteessa polkuun, jossa olet.
3. Tulosta bib-tiedoston sisältö komennolla 'tulosta'.
4. Lisää lähteitä bib-muodossa komennolla 'syota'
   - voit liittää useita bib-tiedoston rivejä leikepöydältä tai kirjoittaa ne käsin
   - voit lisätä myös rivinvaihtoja haluamallasi tavalla
   - kun olet liittänyt haluamasi rivit, vahvista syötetyt rivit komennolla kirjaamalla **tyhjälle riville** ```valmis```
5. Muokkaa haluamaasi viitettä seuraavalla komennolla: ```muokkaa <muokattavan viitteen avain> <muokattavan parametrin tyyppi> <muokkauksen jälkeinen haluttu merkkijono>```
- esimerkkiviite:
```@article{kadiyala2018applications,
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
- esimerkkikomento: ```muokkaa kadiyala2018applications author "Kadiyala et al"```
- tulos:
```@article{kadiyala2018applications,
title={Applications of python to evaluate the performance of decision tree-based boosting algorithms},
author={Kadiyala et al},
journal={Environmental Progress \& Sustainable Energy},
volume={37},
number={2},
pages={618--623},
year={2018},
publisher={Wiley Online Library}
}
```
7. Poistu ohjelmasta komennolla 'exit'
