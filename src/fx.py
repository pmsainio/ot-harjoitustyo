from gensound.filters import SimpleLPF
from gensound.effects import Vibrato

class Effects():
    """luokka, joka filtteröi ääntä ja tuottaa vibraton
    """
    def __init__(self) -> None:
        self.filter = 20000
        self.vibrato_freq = 0
        self.vibrato_width = 0

    def set_filter(self, frequency):
        self.filter = float(frequency)

    def set_vibrato_f(self, frequency):
        self.vibrato_freq = float(frequency)

    def set_vibrato_w(self, width):
        self.vibrato_width = float(width)/20

    def apply_effects(self, signal):
        """ottaa vastaan signaalin, ja asettaa siihen Lowpass-filtterin ja vibraton. Vibrato on
        ehtolausessa, koska kirjasto edellyttää sitä.
        """
        signal *= SimpleLPF(self.filter)
        if self.vibrato_freq > 0 and self.vibrato_width > 0:
            signal *= Vibrato(self.vibrato_freq, self.vibrato_width)
        return signal
