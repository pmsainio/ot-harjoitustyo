import pygame
from ui import ui_action
from visuals import Display
from oscillator import Oscillator
from envelope import Envelope
from fx import Effects
import controls

pygame.font.init()

if __name__ == "__main__":
    effects = Effects()
    envelope = Envelope(effects)
    oscillator = Oscillator(envelope)
    display = Display()
    RUNNING = True
    pygame.mixer.init()
    display.update()
    controls.buttons_sliders(oscillator, envelope, effects)

    while RUNNING:
        ui_action(oscillator)
        controls.root.update()
        pygame.display.update()
