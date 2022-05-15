import pygame
from signal_prosessing.oscillator import Oscillator

def ui_action(oscillator: Oscillator):
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

        if pygame.mixer.get_busy():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    oscillator.stop(0)
                if event.key == pygame.K_w:
                    oscillator.stop(1)
                if event.key == pygame.K_s:
                    oscillator.stop(2)
                if event.key == pygame.K_e:
                    oscillator.stop(3)
                if event.key == pygame.K_d:
                    oscillator.stop(4)
                if event.key == pygame.K_f:
                    oscillator.stop(5)
                if event.key == pygame.K_t:
                    oscillator.stop(6)
                if event.key == pygame.K_g:
                    oscillator.stop(7)
                if event.key == pygame.K_y:
                    oscillator.stop(8)
                if event.key == pygame.K_h:
                    oscillator.stop(9)
                if event.key == pygame.K_u:
                    oscillator.stop(10)
                if event.key == pygame.K_j:
                    oscillator.stop(11)
                if event.key == pygame.K_k:
                    oscillator.stop(12)
                if event.key == pygame.K_o:
                    oscillator.stop(13)
                if event.key == pygame.K_l:
                    oscillator.stop(14)
                if event.key == pygame.K_p:
                    oscillator.stop(15)
                if event.key == 246:
                    oscillator.stop(16)
 
        if event.type == pygame.QUIT:
            exit()
