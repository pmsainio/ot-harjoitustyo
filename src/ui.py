import pygame
import gensound as gs
from oscillator import oscillate
from tuner import tune


def ui_action(TUNING, octave_shift, os_screen):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_a:
                oscillate(frequencies[0], WAVEFORM).play()
            if event.key == pygame.K_w:
                oscillate(frequencies[1], WAVEFORM).play()
            if event.key == pygame.K_s:
                oscillate(frequencies[2], WAVEFORM).play()
            if event.key == pygame.K_e:
                oscillate(frequencies[3], WAVEFORM).play()
            if event.key == pygame.K_d:
                oscillate(frequencies[4], WAVEFORM).play()
            if event.key == pygame.K_f:
                oscillate(frequencies[5], WAVEFORM).play()
            if event.key == pygame.K_t:
                oscillate(frequencies[6], WAVEFORM).play()
            if event.key == pygame.K_g:
                oscillate(frequencies[7], WAVEFORM).play()
            if event.key == pygame.K_y:
                oscillate(frequencies[8], WAVEFORM).play()
            if event.key == pygame.K_h:
                oscillate(frequencies[9], WAVEFORM).play()
            if event.key == pygame.K_u:
                oscillate(frequencies[10], WAVEFORM).play()
            if event.key == pygame.K_j:
                oscillate(frequencies[11], WAVEFORM).play()
            if event.key == pygame.K_k:
                oscillate(frequencies[12], WAVEFORM).play()
            if event.key == pygame.K_o:
                oscillate(frequencies[13], WAVEFORM).play()
            if event.key == pygame.K_l:
                oscillate(frequencies[14], WAVEFORM).play()
            if event.key == pygame.K_p:
                oscillate(frequencies[15], WAVEFORM).play()
            if event.key == 246:
                oscillate(frequencies[16], WAVEFORM).play()

            if event.key == pygame.K_z:
                octave_shift /= 2
                os_screen -=1
                frequencies = []
                tune(TUNING*octave_shift, frequencies)

            if event.key == pygame.K_x:
                octave_shift *= 2
                os_screen +=2
                frequencies = []
                tune(TUNING*octave_shift, frequencies)

            """if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                pygame.mixer.Sound.fadeout(wave.play(), 300)
            if event.key == pygame.K_w:
                oscillate(frequencies[1], wf)
            if event.key == pygame.K_s:
                oscillate(frequencies[2], wf)
            if event.key == pygame.K_e:
                oscillate(frequencies[3], wf)
            if event.key == pygame.K_d:
                oscillate(frequencies[4], wf)
            if event.key == pygame.K_f:
                oscillate(frequencies[5], wf)
            if event.key == pygame.K_t:
                oscillate(frequencies[6], wf)
            if event.key == pygame.K_g:
                oscillate(frequencies[7], wf)
            if event.key == pygame.K_y:
                oscillate(frequencies[8], wf)
            if event.key == pygame.K_h:
                oscillate(frequencies[9], wf)
            if event.key == pygame.K_u:
                oscillate(frequencies[10], wf)
            if event.key == pygame.K_j:
                oscillate(frequencies[11], wf)
            if event.key == pygame.K_k:
                oscillate(frequencies[12], wf)
            if event.key == pygame.K_o:
                oscillate(frequencies[13], wf)
            if event.key == pygame.K_l:
                oscillate(frequencies[14], wf)
            if event.key == pygame.K_p:
                oscillate(frequencies[15], wf)
            if event.key == 246:
                oscillate(frequencies[16], wf)"""

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 110 > mouse[0] > 45 and 140 > mouse[1] > 100:
                WAVEFORM = gs.Sine
            if 182 > mouse[0] > 115 and 140 > mouse[1] > 100:
                WAVEFORM = gs.Square
            if 110 > mouse[0] > 45 and 180 > mouse[1] > 145:
                WAVEFORM = gs.Sawtooth
            if 200 > mouse[0] > 145 and 180 > mouse[1] > 130:
                WAVEFORM = gs.Triangle
        if event.type == pygame.QUIT:
            exit()
