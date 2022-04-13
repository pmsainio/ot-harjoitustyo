import pygame
import gensound as gs
from oscillator import Oscillator
from tuner import tune


def ui_action(oscillator:Oscillator):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_a:
                oscillator.play(0)
            if event.key == pygame.K_w:
                oscillator.play(1)
            if event.key == pygame.K_s:
                oscillator.play(2)
            if event.key == pygame.K_e:
                oscillator.play(3)
            if event.key == pygame.K_d:
                oscillator.play(4)
            if event.key == pygame.K_f:
                oscillator.play(5)
            if event.key == pygame.K_t:
                oscillator.play(6)
            if event.key == pygame.K_g:
                oscillator.play(7)
            if event.key == pygame.K_y:
                oscillator.play(8)
            if event.key == pygame.K_h:
                oscillator.play(9)
            if event.key == pygame.K_u:
                oscillator.play(10)
            if event.key == pygame.K_j:
                oscillator.play(11)
            if event.key == pygame.K_k:
                oscillator.play(12)
            if event.key == pygame.K_o:
                oscillator.play(13)
            if event.key == pygame.K_l:
                oscillator.play(14)
            if event.key == pygame.K_p:
                oscillator.play(15)
            if event.key == 246:
                oscillator.play(16)

            if event.key == pygame.K_z:
                oscillator.transpose(True)

            if event.key == pygame.K_x:
                oscillator.transpose(False)

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
                oscillator.switch_sound(gs.Sine)
            if 182 > mouse[0] > 115 and 140 > mouse[1] > 100:
                oscillator.switch_sound(gs.Square)
            if 110 > mouse[0] > 45 and 180 > mouse[1] > 145:
                oscillator.switch_sound(gs.Sawtooth)
            if 200 > mouse[0] > 145 and 180 > mouse[1] > 130:
                oscillator.switch_sound(gs.Triangle)
        if event.type == pygame.QUIT:
            exit()
