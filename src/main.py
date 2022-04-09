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
    black_keys_we = font.render(f"w e", 1, (25, 25, 25))
    black_keys_tyu = font.render(f"t y u", 1, (25, 25, 25))
    black_keys_op = font.render(f"o p", 1, (25, 25, 25))
    white_keys = font.render(f"a s d f g h j k l ö", 1, (255, 255, 255))
    screen.blit(black_keys_we, (width - black_keys_we.get_width()-540, 180))
    screen.blit(black_keys_tyu, (width - black_keys_tyu.get_width()-250, 180))
    screen.blit(black_keys_op, (width - black_keys_op.get_width()-40, 180))
    screen.blit(white_keys, (width - white_keys.get_width()-20, 240))
    
    pygame.draw.rect(screen, (195, 170, 87), pygame.Rect(45, 100, 65, 40))
    pygame.draw.rect(screen, (195, 170, 87), pygame.Rect(45, 145, 65, 30))
    pygame.draw.rect(screen, (195, 170, 87), pygame.Rect(115, 100, 107, 40))
    pygame.draw.rect(screen, (195, 170, 87), pygame.Rect(115, 145, 120, 32))
    
    sinebutton = wavefont.render(f"sine", 1, (30, 30, 30))
    sawbutton = wavefont.render(f"saw", 1, (30, 30, 30))
    squarebutton = wavefont.render(f"square", 1, (30, 30, 30))
    trianglebutton = wavefont.render(f"triangle", 1, (30, 30, 30))
    screen.blit(sinebutton, (50, 100))
    screen.blit(squarebutton, (120, 100))
    screen.blit(sawbutton, (50, 130))
    screen.blit(trianglebutton, (120, 130))

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
                if event.key == 246:
                    oscillate(frequencies[16], wf)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 110 > mouse[0] > 45 and 140 > mouse[1] > 100:
                    wf = gs.Sine
                if 182 > mouse[0] > 115 and 140 > mouse[1] > 100:
                    wf = gs.Square
                if 110 > mouse[0] > 45 and 180 > mouse[1] > 145:
                    wf = gs.Sawtooth
                if 200 > mouse[0] > 145 and 180 > mouse[1] > 130:
                    wf = gs.Triangle
            if event.type == pygame.QUIT:
                exit()
    
        pygame.display.update()
