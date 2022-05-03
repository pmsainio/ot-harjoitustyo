from gensound import test_wav, WAV
from gensound.effects import Vibrato

w = WAV(test_wav)[10e3:30e3]
w *= Vibrato(frequency=4, width=0.2)

w.play()