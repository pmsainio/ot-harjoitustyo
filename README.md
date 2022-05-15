# Pysynth-projekti

## Käyttöohjeet

Ohjelma avaa kaksi ikkunaa: toisella on kirjaimia ja toisella säätimiä. Oranssin ikkunan kirjaimet edustavat pianon koskettimia: painamalla näitä tietokoneen näppäimistöllä ohjelma soittaa säveliä. (Huomaa, että fokus pitää ensin siirtää ikkunaan klikkaamalla ko. ikkunaa.) Näppäimet z ja x siirtävät koskettimiston oktaavia ylemmäs (x) tai alemmas (z)

Säädinikkunassa on syntetisaattorin ohjauspaneeli, jossa on kaksi tekstikenttää ja kymmenen liukusäädintä.

### Presetit
Ylin kenttä näyttää kullakin hetkellä valittuna olevan presetin. (Lähtoarvona on '{2 Triangle}'.) Nappia painamalla avautuu valikko, josta voi valita toisen presetin. Asetukset tulevat voimaan painikkeella 'Load preset'.

Mikäli käyttäjä haluaa tallentaa itse tekemiään säädöksiä, onnistuu se kirjoittamalla tyhjään tekstikenttään nimi uudelle presetille ja painamalla 'Save preset' -nappia kentän vieressä. Jos presetin nimi on jo käytössä, korvataan vanha preset uudella. Nimetön preset ei rekisteröidy.

Halutessaan siistiä valikoimaa, voi käyttäjä poistaa presetin valitsemalla sen valikosta ja painamalla 'Delete preset' -painiketta. Kaikki omat presetit voi poistaa ja alkuperäispresetteihin tehdyt muutokset kumota 'Factory reset' -painikkeella.

### Liukusäätimet

Ylärivi:
- *Tuner* muuttaa syntetisaattorin viritystä. Säätimen numero vastaa yksiviivaisen a:n hertsimäärää.
- *Sine* määrittää, kuinka paljon äänessä kuuluu siniaaltoa.
- *Triangle* on hieman siniaaltoa kirkkaampi.
- *Square* on äänistä säröisin.
- *Sawtooth* on kaikista kirkkain ääni.

Alarivi:
- *Attack* määrittää kuinka nopea aluke syttyvällä äänellä on. Suurempi arvo hidastaa aluketta ja näin ollen pehmentää ääntä.
- *Release* määrittää lopukkeen pituuden. Suurempi arvo saa äänen soimaan kauemmin, kun näppäintä ei enää paineta.
- *Vibrato F* säätää vibraton taajuutta (frequency). Suurempi arvo tarkoittaa nopeampaa vibratoa.
- *Vibrato W* säätää vibraton leveyttä (width). Arvon kasvaessa äänen värinä muuttuu voimakkaammaksi. **Mikäli sekä *Vibrato F*- että *Vibrato W*-säätimet ovat nollassa, ei vibratoa ilmene.**
- *Master*-säädin asettaa lopullisen äänenvoimakkuuden.

Jos olet tehnyt säädöksiä paneelissa, muista klikata taas koskettimistoikkunaa soittaaksesi jotain.

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

[release 1](https://github.com/pmsainio/ot-harjoitustyo/releases/tag/viikko5)

[release 2](https://github.com/pmsainio/ot-harjoitustyo/releases/tag/viikko6)

[final release](https://github.com/pmsainio/ot-harjoitustyo/releases/tag/viikko7)
