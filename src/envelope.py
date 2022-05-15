import pygame
import gensound.transforms as gt

class Envelope():
    """luokka, joka vastaa äänen alukkeiden ja lopukkeiden pituuksista ja äänen toistamisesta

    Attributes:
        effects: luokka, josta kutsutaan efektejä, kuten vibratoa
    """
    def __init__(self, effects):
        self.attack = float(20)
        self.release = 200
        self.gain = 0.3
        self.effects = effects

    def set_attack(self, value):
        self.attack = float(value) + 1

    def set_release(self, value):
        self.release = int(value) * 10 + 1

    def set_gain(self, value):
        self.gain = (float(value)+10)/100

    def apply_attack(self, waveform):
        """asettaa ensin äänelle halutun alukkeen (attack), kutsuu effects-luokasta
        mahdollisia efektejä ja toistaa sitten äänen.
        """
        sound = self.gain * waveform
        sound *= gt.ADSR(attack=self.attack, decay=0.3e3, sustain=1, release=0.3e3)
        sound = self.effects.apply_effects(sound)
        return sound.play()

    def apply_release(self):
        """sammuttaa äänen halutulla nopeudella
        """
        pygame.mixer.fadeout(self.release)
