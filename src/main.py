import os
import pygame
from ui import ui_action
from visuals import Display
from oscillator import Oscillator
from tkinter import *
import controls

pygame.font.init()

if __name__ == "__main__":
    oscillator = Oscillator()
    display = Display()
    RUNNING = True
    pygame.mixer.init()
    display.update()
    controls.buttons_sliders(oscillator)

    while RUNNING:    
        ui_action(oscillator)
        controls.root.update()
        pygame.display.update()
