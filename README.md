# Pysynth-projekti

### Käyttöohjeet


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
Ohjelma avaa ikkunan, jolla näkyy kirjaimia. Näitä kirjaimia painamalla (tietokoneen näppäimistöllä) ohjelma soittaa eri säveliä.
Syntesoijan ääntä voi vaihtaa painamalla vasemmassa yläreunassa olevia sanoja. (Oletusarvona on kolmioaalto 'Triangle'.)

Koskettimiston oktaavia saa vaihdettua näppäimillä z (alas) ja x (ylös). *Huom! Yli 22050 Hz:n taajuudet tulevat vihreellisesti soimaan matalammalta ohjelman näytteenottotaajuuden (44100) vuoksi. Tämä ei ole virhe vaan ominaisuus.*

Mikäli haluat suorittaa ohjelman testejä, onnistuvat ne komentorivin komennolla
```bash
poetry run invoke test
```
Testikattavuusraportti puolestaan on luotavissa komennolla
```bash
poetry run invoke coverage-report
```

[vaatimusmäärittely](https://github.com/pmsainio/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/pmsainio/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

[arkkitehtuuri](https://github.com/pmsainio/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
