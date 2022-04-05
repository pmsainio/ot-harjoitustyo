import gensound.transforms as gt
from pydub.generators import Sine



def oscillate(f, wf):
    wave = wf(f, 80000)*gt.ADSR(attack=0.002e3, decay=0.3e3, sustain=0.3, release=500)
    return wave.play()

