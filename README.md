# Pysynth-projekti

### Käyttöohjeet

Ohjelma avaa kaksi ikkunaa: toisella on kirjaimia ja toisella säätimiä. Oranssin ikkunan kirjaimet edustavat pianon koskettimia: painamalla näitä tietokoneen näppäimistöllä ohjelma soittaa säveliä. (Huomaa, että fokus pitää ensin siirtää ikkunaan klikkaamalla ko. ikkunaa.) Näppäimet z ja x siirtävät koskettimiston oktaavia ylemmäs (x) tai alemmas (z)

Säädinikkunassa on syntetisaattorin ohjauspaneeli. Sine-, Triangle-, Square- tai Sawtooth-näppäintä painamalla saat vaihdettua syntikan ääntä. (Oletusarvona on Triangle). *Huomaa, että äänenvoimakkuus kasvaa ääntä vaihdettaessa. Saha-aallossa on loputon määrä siniaaltoja päällekkäin.* Tuner-säädin vaihtaa syntikan viritystä. Lisäksi paneelista löytyvät Attack-, Release- sekä Master-liukusäätimet. Valitettavasti näistä ainoastaan Release on toiminnassa. Säätin vaikuttaa äänen sammumisnopeuteen.

### Asentaminen
Ohjelman saa toimintaan komennoilla

```bash
poetry install
```
```bash
poetry run invoke build
```
```bash
poetry run invoke start
```

### Dokumentaatio

[vaatimusmäärittely](https://github.com/pmsainio/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/pmsainio/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[arkkitehtuuri](https://github.com/pmsainio/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[changelog](https://github.com/pmsainio/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

### Komentorivitoimintoja

Mikäli haluat suorittaa ohjelman testejä, onnistuvat ne komentorivin komennolla
```bash
poetry run invoke test
```
Testikattavuusraportti puolestaan on luotavissa komennolla
```bash
poetry run invoke coverage-report
```
Koodin laadun voi tarkistaa komennolla
```bash
poetry run invoke lint
```
