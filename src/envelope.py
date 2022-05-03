import pygame
import gensound.transforms as gt

class Envelope():
    def __init__(self):
        self.attack = float(20)
        self.release = 200
        self.gain = 0.3

    def set_attack(self, value):
        self.attack = float(value)

    def set_release(self, value):
        self.release = int(value) * 10 + 1

    def set_gain(self, value):
        self.gain = float(value)+1 * 0.005

    def apply_attack(self, frequency, waveform):
            sound = waveform(frequency)*gt.ADSR(attack=self.attack,
                                                decay=0.3e3,
                                                sustain=1,
                                                release=0.3e3)
            sound *= float(self.gain)
            return sound.play(max_amplitude=1)

    def apply_release(self):
        pygame.mixer.fadeout(self.release)