# Pysynth-projekti

### Käyttöohjeet

Ohjelma avaa kaksi ikkunaa: toisella on kirjaimia ja toisella säätimiä. Oranssin ikkunan kirjaimet edustavat pianon koskettimia: painamalla näitä tietokoneen näppäimistöllä ohjelma soittaa säveliä. (Huomaa, että fokus pitää ensin siirtää ikkunaan klikkaamalla ko. ikkunaa.) Näppäimet z ja x siirtävät koskettimiston oktaavia ylemmäs (x) tai alemmas (z)

Säädinikkunassa on syntetisaattorin ohjauspaneeli. Sine-, Triangle-, Square- tai Sawtooth-näppäintä painamalla saat vaihdettua syntikan ääntä. (Oletusarvona on Triangle). *Huomaa, että äänenvoimakkuus kasvaa ääntä vaihdettaessa.* Tuner-säädin vaihtaa syntikan viritystä.

Muita säätimiä: Attack ja Release muuttavat äänen syttymis- ja sammumisnopeutta. HPF eli HiPassFilter suodattaa korkeita taajuuksia pois. Vibrato F säätää vibraton taajuutta (Frequency) ja Vibrato W säätää vibraton leveyttä (Width)

Jos olet tehnyt säädöksiä paneelissa, muista klikata taas koskettimistoikkunaa soittaaksesi jotain.

Hauskoja soittohetkiä!

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

[käyttöohje (sama kuin alussa)](https://github.com/pmsainio/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

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

### Releaset

[release 1] (https://github.com/pmsainio/ot-harjoitustyo/releases/tag/viikko5)
[release 2] (https://github.com/pmsainio/ot-harjoitustyo/releases/tag/viikko6)
