import pygame
from ui import ui_action
from visuals import update
from oscillator import Oscillator

sample_rate = 44100

pygame.font.init()
font = pygame.font.SysFont("comicsans", 90)
wave_font = pygame.font.SysFont("comicsans", 30)

WIDTH = 720
HEIGHT = 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))

if __name__ == "__main__":
    oscillator = Oscillator()
    running = True
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    update(screen, font, wave_font, WIDTH)
    while running:
        pygame.mixer.init()
        
        ui_action(oscillator)
        pygame.display.update()
