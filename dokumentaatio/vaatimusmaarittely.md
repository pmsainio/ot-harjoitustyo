# Vaatimusmäärittely

### Sovelluksen tarkoitus
Sovelluksen tarkoitus on mallintaa yksinkertaista syntetisaattoria koskettimistolla ja säätimillä. Käyttäjä voi soittaa soitinta näppäimistöllä.

### Suunnitellut toiminnallisuudet
- [x] Muutamia eri aaltomuotoja, kuten siniaalto, saha-aalto, kanttiaalto ja kolmioaalto
- [x] Attack, Decay, Sustain, Release -säätimistö (ADSR)
- [ ] Lowpass-filtteri [luovuttu latenssiongelman vuoksi]
- [x] Äänikirjasto, jossa valmiita asetuksia ja mahdollisuus tallentaa omia asetuksia.

### Toteutetut toiminnallisuudet
- Neljä aaltomuotoa
  - Sini, kolmio, kantti ja saha
  - Käyttäjän on mahdollista säätää jokaisen aaltomuodon tasoa erikseen. (Tämä korvaa filtteriä.)
- Attack- ja release-säätimet.
- Presetit:
  - Neljä perusaaltomuotoa
  - Muutama kehittäjän itse laatima preset
  - Käyttäjän mahdollisuus tallentaa omia presettejä ja muokata olemassaolevia
  - Yksittäisen presetin poistomahdollisuus ja tehdasasetusten palauttaminen.
- Low Frequency Oscillator (LFO) joka tuottaa vibraton
  - LFO:n taajuus ja amplitudi käyttäjän säädettävissä
- Viritin, joka operoi välillä 420 Hz -- 450 Hz

### Jatkokehitysideoita
- [ ] Säädettävä mono- vs. polyfonisuus
- [ ] Kustomoitava pitch-bend
- [x] Hidas oskillattori (LFO) modulointia varten
