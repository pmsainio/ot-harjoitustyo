import pygame
import gensound as gs
from oscillator import oscillate
from tuner import tune
samplerate = 44100

pygame.font.init()
font = pygame.font.SysFont("comicsans", 90)
wavefont = pygame.font.SysFont("comicsans", 30)

pygame.init()
width = 720
height = 640
screen = pygame.display.set_mode((width, height))



if __name__=="__main__":

    tuning = 440
    frequencies = []
    tune(tuning, frequencies)
    
    wf = gs.Triangle

    keys = "awsedftgyhjikolp"

    running = True
    screen = pygame.display.set_mode((width, height))
    screen.fill((210, 185, 100))
    black_keys = font.render(f"w e  t y u  o p", 1, (25, 25, 25))
    white_keys = font.render(f"a s d f g h j k l", 1, (255, 255, 255))
    screen.blit(black_keys, (width - black_keys.get_width() - 140, 200))
    screen.blit(white_keys, (width - white_keys.get_width() - 155, 240))
    sinebutton = wavefont.render(f"sine", 1, (30, 30, 30))
    sawbutton = wavefont.render(f"saw", 1, (30, 30, 30))
    squarebutton = wavefont.render(f"square", 1, (30, 30, 30))
    trianglebutton = wavefont.render(f"triangle", 1, (30, 30, 30))
    screen.blit(sinebutton, (50, 100))
    screen.blit(squarebutton, (100, 100))
    screen.blit(sawbutton, (50, 130))
    screen.blit(trianglebutton, (100, 130))

    while running:
        pygame.mixer.init()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_a:
                    oscillate(frequencies[0], wf)
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
                # if event.key == pygame.K_ö:
                    #oscillate(frequencies[16])"""
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 100 > mouse[0] > 50 and 130 > mouse[1] > 100:
                    wf = gs.Sine
                if 180 > mouse[0] > 100 and 130 > mouse[1] > 100:
                    wf = gs.Square
                if 100 > mouse[0] > 50 and 180 > mouse[1] > 130:
                    wf = gs.Sawtooth
                if 180 > mouse[0] > 100 and 180 > mouse[1] > 130:
                    wf = gs.Triangle
            if event.type == pygame.QUIT:
                exit()
    
        pygame.display.update()

        
            
                    
            