# Pysynth-projekti

### Käyttöohjeet

<<<<<<< HEAD
Ohjelman saa toimintaan komennoilla ```bash
poetry install
```
ja 
```bash
poetry run invoke build
```
```bash
poetry run invoke start
```
Ohjelma avaa ikkunan, jolla näkyy kirjaimia. Näitä kirjaimia painamalla (tietokoneen näppäimistöllä) ohjelma soittaa eri säveliä.
Syntesoijan ääntä voi vaihtaa painamalla vasemmassa yläreunassa olevia sanoja. (Oletusarvona on kolmioaalto 'Triangle'.) *Huom! Ohjelman äänenvoimakkuutta ei ole normalisoitu. Varo siis korviasi, kun kokeilet eri aaltomuotoja.* 

Testiympäristö ja versinainen ohjelma ovat toimineet eri fonteilla. Tämän vuoksi aaltomuotoa vaihtaessa on helppoa klikata ohi, ja vaihtotoimenpide saattaa vaatia kärsivällisyyttä.


Mikäli haluat suorittaa ohjelman testejä, onnistuvat ne komentorivin komennolla ```bash
poetry run invoke test
```
Testikattavuusraportti puolestaan on luotavissa komennolla ```bash
poetry run invoke coverage-report
```
