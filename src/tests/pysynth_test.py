import unittest
from tuner import tune
from oscillator import Oscillator
import gensound as gs


class TestTuner(unittest.TestCase):
    def setUp(self):
        self.oscillator = Oscillator()
        self.concert = tune(440)
        self.baroque = tune(415)
        self.oscillator.retune(432)
        self.big_brain = self.oscillator.frequencies

    def test_concert_pitch(self):
        self.assertEqual(self.concert, [261.6255653005985, 277.18263097687196,
                                        293.66476791740746, 311.1269837220808,
                                        329.62755691286986, 349.2282314330038,
                                        369.99442271163434, 391.99543598174927,
                                        415.3046975799451, 440, 466.1637615180899,
                                        493.8833012561241, 523.2511306011974,
                                        554.3652619537443, 587.3295358348153,
                                        622.253967444162, 659.2551138257401])

    def test_baroque_pitch(self):
        self.assertEqual(self.baroque, [246.76047636306453, 261.4336178531861,
                                        276.97926974028206, 293.44931419241715,
                                        310.89871845191135, 329.38571828340133,
                                        348.9720123302915, 369.72296802824076,
                                        391.7078397629028, 415, 439.6771841591075,
                                        465.8217500483898, 493.5209527261293,
                                        522.8672357063724, 553.9585394805644,
                                        586.8986283848345, 621.7974369038229])

    def test_retuning(self):
        self.assertEqual(self.big_brain, [256.8687368405877, 272.14294677729254,
                                        288.32540850072735, 305.47012947258844,
                                        323.6343286053631, 342.878627225131,
                                        363.2672513896046, 384.86824623662653,
                                        407.7537030784916, 432, 457.68805676321557,
                                        484.90360486964914, 513.7374736811755,
                                        544.2858935545853, 576.6508170014549,
                                        610.9402589451772, 647.2686572107266])


class TestSwitchSound(unittest.TestCase):
    def setUp(self):
        self.oscillator = Oscillator()

    def test_switch_sine(self):
        self.oscillator.switch_sound_sine()
        self.assertEqual(str(self.oscillator.waveform), "<class 'gensound.signals.Sine'>")

    def test_switch_triangle(self):
        self.oscillator.switch_sound_triangle()
        self.assertEqual(str(self.oscillator.waveform), "<class 'gensound.signals.Triangle'>")

    def test_switch_square(self):
        self.oscillator.switch_sound_square()
        self.assertEqual(str(self.oscillator.waveform), "<class 'gensound.signals.Square'>")

    def test_switch_saw(self):
        self.oscillator.switch_sound_saw()
        self.assertEqual(str(self.oscillator.waveform), "<class 'gensound.signals.Sawtooth'>")

class TestTransposing(unittest.TestCase):
    def setUp(self):
        self.oscillator = Oscillator()

    def test_transpose_down(self):
        transposed = self.oscillator.transpose(True)
        self.assertEqual(transposed, [130.81278265029925, 138.59131548843598,
                                                    146.83238395870373, 155.5634918610404,
                                                    164.81377845643493, 174.6141157165019,
                                                    184.99721135581717, 195.99771799087463,
                                                    207.65234878997256, 220.0, 233.08188075904496,
                                                    246.94165062806206, 261.6255653005987,
                                                    277.18263097687213, 293.66476791740763,
                                                    311.126983722081, 329.62755691287003])
                                    
    def test_transpose_up(self):
        transposed = self.oscillator.transpose(False)
        self.assertEqual(transposed, [523.251130601197, 554.3652619537439,
                                                    587.3295358348149, 622.2539674441616,
                                                    659.2551138257397, 698.4564628660077,
                                                    739.9888454232687, 783.9908719634985,
                                                    830.6093951598903, 880.0, 932.3275230361799,
                                                    987.7666025122483, 1046.5022612023947,
                                                    1108.7305239074885, 1174.6590716696305,
                                                    1244.507934888324, 1318.5102276514801])
