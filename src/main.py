import pygame
import gensound as gs
from tuner import tune
from ui import ui_action
from visuals import update

sample_rate = 44100

pygame.font.init()
font = pygame.font.SysFont("comicsans", 90)
wave_font = pygame.font.SysFont("comicsans", 30)

WIDTH = 720
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

if __name__=="__main__":

    WAVEFORM = gs.Triangle
    octave_shift = 1
    os_screen = 0
    TUNING = 440
    frequencies = []
    tune(TUNING, frequencies)

    running = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    update(screen, font, wave_font, WIDTH)

    while running:
        pygame.mixer.init()
        ui_action()
        pygame.display.update()
