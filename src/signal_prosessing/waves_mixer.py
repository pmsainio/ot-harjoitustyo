from gensound import Sine, Triangle, Square, Sawtooth

class WaveMixer():
    """Palauttaa signaalin, joka on yhdistelmä eri aaltomuotoja.
    Luokka myös kompensoi kantti- ja saha-aaltojen kovaäänisyyttä.
    """
    def __init__(self):
        self.sine = 0
        self.triangle = 1
        self.square = 0
        self.sawtooth = 0

    def set_sine(self, level):
        self.sine = int(level) / 100

    def set_triangle(self, level):
        self.triangle = int(level) / 100

    def set_square(self, level):
        self.square = int(level) / 200

    def set_sawtooth(self, level):
        self.sawtooth = int(level) / 200

    def mix(self, freq):
        return self.sine * Sine(freq) \
             + self.triangle * Triangle(freq) \
             + self.square * Square(freq) \
             + self.sawtooth * Sawtooth(freq)
