import gensound.transforms as gt
import gensound as gs



def oscillate(f, wf):
    wave = wf(f, 80000)*gt.ADSR(attack=0.002e3, decay=0.3e3, sustain=0.3, release=500)
    if wf == gs.Square or wf == gs.Sawtooth:
        wave *= 0.5
    return wave.play()

