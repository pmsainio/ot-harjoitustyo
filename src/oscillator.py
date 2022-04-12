import gensound.transforms as gt
import gensound as gs

def oscillate(FREQUENCY, WAVEFORM):
    SOUND = WAVEFORM(FREQUENCY, 80000)*gt.ADSR(attack=0.002e3, decay=0.3e3, sustain=0.3, release=1)
    if WAVEFORM == gs.Square or WAVEFORM == gs.Sawtooth:
        SOUND *= 0.4
    return SOUND

def hold(FREQUENCY, WAVEFORM):
    SOUND = WAVEFORM(FREQUENCY, 80000)*gt.ADSR(attack=0, decay=0, sustain=0.3, release=0)
    if WAVEFORM == gs.Square or WAVEFORM == gs.Sawtooth:
        SOUND *= 0.4
    return SOUND

def release(FREQUENCY, WAVEFORM):
    SOUND = WAVEFORM(FREQUENCY, 80000)*gt.ADSR(attack=0, decay=0, sustain=0.3, release=0)
    if WAVEFORM == gs.Square or WAVEFORM == gs.Sawtooth:
        SOUND *= 0.4
    return SOUND