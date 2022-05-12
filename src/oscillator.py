import gensound as gs
from tuner import tune

class Oscillator():
    """oskillaattoriluokka vastaa nuottien vireestä ja aaltomuodosta

    Attributes:
        envelope: luokka, josta kutsutaan alukkeita (attack) ja lopukkeita (release)
    """
    def __init__(self, envelope, mixer):
        self.envelope = envelope
        self.mixer = mixer
        self.waveform = gs.Triangle
        self.octave_shift = 1
        self.tuning = 440
        self.frequencies = tune(self.tuning)
        self.last_note = None

    def play(self, note:int):
        """"kutsuu envelope-luokkaa, joka soittaa äänen
        """
        self.last_note = self.frequencies[note]
        self.waveform = self.mixer.mix(self.last_note)
        self.envelope.apply_attack(self.waveform)

    def stop(self, note:int):
        """sammuttaa äänen, mikäli käyttäjä nostaa sormensa näppäimeltä
        """
        if self.last_note == self.frequencies[note]:
            self.envelope.apply_release()

    def transpose(self, down: bool):
        """puolittaa tai kaksinkertaistaa koskettimien vireet, eli siirtää koskettimistoa
        oktaavilla ylös tai alaspäin
        """
        if down:
            self.octave_shift /= 2
            self.frequencies = tune(self.tuning * self.octave_shift)

        else:
            self.octave_shift *= 2
            self.frequencies = tune(self.tuning * self.octave_shift)

    def retune(self, frequency):
        """laskee koskettimille uudet taajuudet halutun viritystaajuuden pohjalta
        """
        self.frequencies = tune(int(frequency))
