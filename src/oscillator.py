import gensound.transforms as gt
import gensound as gs
from tuner import tune
import pygame

class Oscillator():
    def __init__(self):
        self.waveform = gs.Triangle
        self.octave_shift = 1
        self.os_screen = 0
        self.tuning = 440
        self.frequencies = tune(self.tuning)
        self.attack = 0.5
        self.release = 200
        self.gain = 0.3
        self.last_note = None

    def oscillate(self, frequency, waveform):
        sound = waveform(frequency)*gt.ADSR(attack=0.002e3,
                                                decay=0.3e3, sustain=1, release=self.release)
        sound *= self.gain 
        return sound.play(max_amplitude=1)

    def play(self, n):
        self.last_note = self.frequencies[n]
        self.oscillate(self.last_note, self.waveform)

    def stop(self, n):
        if self.last_note == self.frequencies[n]:
            pygame.mixer.fadeout(self.release)

    def switch_sound_sine(self):
        self.waveform = gs.Sine

    def switch_sound_triangle(self):
        self.waveform = gs.Triangle

    def switch_sound_square(self):
        self.waveform = gs.Square

    def switch_sound_saw(self):
        self.waveform = gs.Sawtooth

    def transpose(self, down: bool):
        if down:
            self.octave_shift /= 2
            self.os_screen -= 1
            self.frequencies = []
            tune(self.tuning*self.octave_shift, self.frequencies)

        else:
            self.octave_shift *= 2
            self.os_screen += 2
            self.frequencies = []
            tune(self.tuning*self.octave_shift, self.frequencies)

    def retune(self, frequency):
        self.frequencies = tune(int(frequency))

    def set_attack(self, value):
        self.attack = int(value)

    def set_release(self, value):
        self.release = int(value) * 10 + 1

    def set_gain(self, value):
        self.gain = int(value) * 0.004