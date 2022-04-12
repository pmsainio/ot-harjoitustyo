import unittest
from pygame import mixer
from tuner import tune
from oscillator import oscillate
import gensound as gs

class TestTuner(unittest.TestCase):
    def setUp(self):
        freqa = []
        freqb = []
        self.concert = tune(440, freqa)
        self.baroque = tune(415, freqb)

    def test_concert_pitch(self):
        self.assertEqual(self.concert, [261.6255653005985, 277.18263097687196,
            293.66476791740746, 311.1269837220808, 329.62755691286986,
            349.2282314330038, 369.99442271163434, 391.99543598174927,
            415.3046975799451, 440, 466.1637615180899, 493.8833012561241,
            523.2511306011974, 554.3652619537443, 587.3295358348153,
            622.253967444162, 659.2551138257401])

    def test_baroque_pitch(self):
        self.assertEqual(self.baroque, [246.76047636306453, 261.4336178531861,
            276.97926974028206, 293.44931419241715, 310.89871845191135,
            329.38571828340133, 348.9720123302915, 369.72296802824076,
            391.7078397629028, 415, 439.6771841591075, 465.8217500483898,
            493.5209527261293, 522.8672357063724, 553.9585394805644,
            586.8986283848345, 621.7974369038229])

class TestOscillator(unittest.TestCase):
    def test_oscillate(self):
        oscillate(400, gs.Triangle).play() == mixer.get_busy()

        self.assertEqual(self.sound, True)