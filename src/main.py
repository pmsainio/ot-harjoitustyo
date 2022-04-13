import pygame
from ui import ui_action
from visuals import Display
from oscillator import Oscillator

sample_rate = 44100

pygame.font.init()



if __name__ == "__main__":
    oscillator = Oscillator()
    display = Display()
    running = True

    display.update()
    while running:
        pygame.mixer.init()
        display.variables()
        
        ui_action(oscillator)
        pygame.display.update()
