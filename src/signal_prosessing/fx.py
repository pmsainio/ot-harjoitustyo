from gensound.effects import Vibrato

class Effects():
    """luokka, joka tuottaa vibraton
    """
    def __init__(self) -> None:
        self.vibrato_freq = 0
        self.vibrato_width = 0

    def set_vibrato_f(self, frequency):
        self.vibrato_freq = float(frequency)

    def set_vibrato_w(self, width):
        self.vibrato_width = float(width)/20

    def apply_effects(self, signal):
        """ottaa vastaan signaalin, ja asettaa siihen efektit. Vibrato on
        ehtolausessa, koska sen arvo ei saa olla 0.
        """
        if self.vibrato_freq > 0 and self.vibrato_width > 0:
            signal *= Vibrato(self.vibrato_freq, self.vibrato_width)
        return signal
