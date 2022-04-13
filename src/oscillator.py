import gensound.transforms as gt
import gensound as gs
from tuner import tune


def oscillate(FREQUENCY, WAVEFORM):
    SOUND = WAVEFORM(FREQUENCY, 80000)*gt.ADSR(attack=0.002e3,
                                               decay=0.3e3, sustain=0.3, release=1)
    if WAVEFORM == gs.Square or WAVEFORM == gs.Sawtooth:
        SOUND *= 0.4
    return SOUND.play()

class Oscillator():
    def __init__(self):
        self.WAVEFORM = gs.Triangle
        self.octave_shift = 1
        self.OS_SCREEN = 0
        self.TUNING = 440
        self.frequencies = []
        self.frequencies = tune(self.TUNING, self.frequencies)

    def play(self, n):
        oscillate(self.frequencies[n], self.WAVEFORM)
        
    def switch_sound(self, WAVEFORM):
        self.WAVEFORM = WAVEFORM

    def transpose(self, down:bool):
        if down:
            self.octave_shift /= 2
            self.OS_SCREEN -= 1
            self.frequencies = []
            print(self.octave_shift)
            tune(self.TUNING*self.octave_shift, self.frequencies)
            print(self.frequencies)

        else:
            self.octave_shift *= 2
            self.OS_SCREEN += 2
            self.frequencies = []
            tune(self.TUNING*self.octave_shift, self.frequencies)

    def switch_sound(self, sound):
        self.WAVEFORM = sound

    def retune(self, frequency):
        self.TUNING = frequency
"""
def hold(FREQUENCY, WAVEFORM):
    SOUND = WAVEFORM(FREQUENCY, 80000)*gt.ADSR(attack=0,
                                               decay=0, sustain=0.3, release=0)
    if WAVEFORM == gs.Square or WAVEFORM == gs.Sawtooth:
        SOUND *= 0.4
    return SOUND


def release(FREQUENCY, WAVEFORM):
    SOUND = WAVEFORM(FREQUENCY, 80000)*gt.ADSR(attack=0,
                                               decay=0, sustain=0.3, release=0)
    if WAVEFORM == gs.Square or WAVEFORM == gs.Sawtooth:
        SOUND *= 0.4
    return SOUND"""