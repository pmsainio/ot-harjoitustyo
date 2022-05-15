import unittest
from signal_prosessing.fx import Effects
from signal_prosessing.waves_mixer import WaveMixer
from signal_prosessing.envelope import Envelope
from signal_prosessing.tuner import tune
from signal_prosessing.oscillator import Oscillator
import sql.sql_schema as sql
import gensound as gs
import pygame
import time

class TestTuner(unittest.TestCase):
    def setUp(self):
        self.oscillator = Oscillator(envelope=Envelope, mixer=WaveMixer)
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

class TestTransposing(unittest.TestCase):
    def setUp(self):
        self.oscillator = Oscillator(envelope=Envelope, mixer=WaveMixer)

    def test_transpose_down(self):
        self.oscillator.transpose(True)
        self.assertEqual(self.oscillator.frequencies, [130.81278265029925, 138.59131548843598,
                                                        146.83238395870373, 155.5634918610404,
                                                        164.81377845643493, 174.6141157165019,
                                                        184.99721135581717, 195.99771799087463,
                                                        207.65234878997256, 220.0, 233.08188075904496,
                                                        246.94165062806206, 261.6255653005987,
                                                        277.18263097687213, 293.66476791740763,
                                                        311.126983722081, 329.62755691287003])
    def test_transpose_up(self):
        self.oscillator.transpose(False)
        self.assertEqual(self.oscillator.frequencies, [523.251130601197, 554.3652619537439,
                                                        587.3295358348149, 622.2539674441616,
                                                        659.2551138257397, 698.4564628660077,
                                                        739.9888454232687, 783.9908719634985,
                                                        830.6093951598903, 880.0, 932.3275230361799,
                                                        987.7666025122483, 1046.5022612023947,
                                                        1108.7305239074885, 1174.6590716696305,
                                                        1244.507934888324, 1318.5102276514801])

class TestSound(unittest.TestCase):
    def setUp(self):
        self.effects = Effects()
        self.envelope = Envelope(self.effects)

    def test_sound_on(self):
        self.envelope.apply_attack(gs.Triangle(440))
        sound_status = pygame.mixer.get_busy()
        self.assertEqual(sound_status, True)

    def test_sound_off(self):
        self.envelope.apply_attack(gs.Triangle(420))
        self.envelope.set_release(0)
        self.envelope.apply_release()
        time.sleep(1)
        sound_status = pygame.mixer.get_busy()
        self.assertEqual(sound_status, False)

class TestSQL(unittest.TestCase):
    def setUp(self):
        sql.factory_reset()
        self.presumed_presets = [('1 Sine',), ('2 Triangle',), ('3 Square',), ('4 Sawtooth',), ('Bee',), ('Cat',), ('Skeleton',), ('Snake',)]

    def test_presets(self):
        self.assertEqual(self.presumed_presets, sql.get_presets())

    def test_insert_and_update(self):
        sql.save_preset("test", 0, 0, 0, 0, 0, 0, 0, 0)
        self.assertEqual(sql.load_preset_data("test"), ("test", 0, 0, 0, 0, 0, 0, 0, 0))
        sql.save_preset("test", 0, 0, 0, 0, 0, 0, 0, 1)
        self.assertEqual(sql.load_preset_data("test"), ("test", 0, 0, 0, 0, 0, 0, 0, 1))

    def test_reset(self):
        sql.save_preset("test", 0, 0, 0, 0, 0, 0, 0, 0)
        self.assertNotEqual(self.presumed_presets, sql.get_presets())
        sql.factory_reset()
        self.assertEqual(self.presumed_presets, sql.get_presets())

    def test_delete(self):
        sql.save_preset("test", 0, 0, 0, 0, 0, 0, 0, 0)
        self.assertNotEqual(self.presumed_presets, sql.get_presets())
        sql.delete_preset("('test',)")
        self.assertEqual(self.presumed_presets, sql.get_presets())

class TestMixer(unittest.TestCase):
    def setUp(self):
        sql.init()
        self.mixer = WaveMixer()

    def test_levels_affected(self):
        self.mixer.set_sine(100)
        self.mixer.set_triangle(0)
        self.mixer.set_square(100)
        self.mixer.set_sawtooth(100)
        self.assertEqual([self.mixer.sine, self.mixer.triangle, self.mixer.square, self.mixer.sawtooth], [1, 0, 0.5, 0.5])

class TestEffects(unittest.TestCase):
    def setUp(self):
        self.effects = Effects()
        
    def test_vibrato_appliance(self):
        self.effects.set_vibrato_f(1)
        self.effects.set_vibrato_w(0)
        self.assertEqual(str(self.effects.apply_effects(gs.Sine(400))), "Sine")

        self.effects.set_vibrato_f(0)
        self.effects.set_vibrato_w(1)
        self.assertEqual(str(self.effects.apply_effects(gs.Sine(400))), "Sine")

        self.effects.set_vibrato_f(1)
        self.effects.set_vibrato_w(1)
        self.assertEqual(str(self.effects.apply_effects(gs.Sine(400))), "Sine*(Vibrato)")