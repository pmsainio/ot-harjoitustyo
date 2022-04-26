## Sovellusarkkitehtuuri

### Rakenne

Sovellus koostuu tällä hetkellä main-ohjelmasta ja viidestä sitä tukevasta moduulista:
- *ui* käsittelee näppäimistöltä tulevat komennot
- *tuner* laskee oikeat taajuudet viritysäänen pohjalta
- *oscillator* tuottaa äänet halutuilla äänenväreillä
- *visuals* vastaa käyttöliittymän staattisesta ikkunasta ja
- *controls* käsittelee käyttäjän muutettavat arvot

![Pakkausrakenne](./kuvat/pysynth.drawio.png)

### Sovelluslogiikka

Seuraava kaavio kuvastaa syntetisaattorin virittymistä ja äänen soittamista:

![sekvenssikaavio](./kuvat/sequence_map.png)
