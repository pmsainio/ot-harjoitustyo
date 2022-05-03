import gensound as gs
from tuner import tune

class Oscillator():
    def __init__(self, envelope):
        self.envelope = envelope
        self.waveform = gs.Triangle
        self.octave_shift = 1
        self.tuning = 440
        self.frequencies = tune(self.tuning)
        self.last_note = None

    def play(self, note:int):
        self.last_note = self.frequencies[note]
        self.envelope.apply_attack(self.last_note, self.waveform)

    def stop(self, note:int):
        if self.last_note == self.frequencies[note]:
            self.envelope.apply_release()

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
            self.frequencies = tune(self.tuning * self.octave_shift)
        
        else:
            self.octave_shift *= 2
            self.frequencies = tune(self.tuning * self.octave_shift)

    def retune(self, frequency):
        self.frequencies = tune(int(frequency))
