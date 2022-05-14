import pygame
from ui import ui_action
from visuals import Display
from oscillator import Oscillator
from envelope import Envelope
from waves_mixer import WaveMixer
from fx import Effects
import controls
import sql_schema

pygame.font.init()

if __name__ == "__main__":
    effects = Effects()
    envelope = Envelope(effects)
    mixer = WaveMixer()
    oscillator = Oscillator(envelope, mixer)
    display = Display()
    RUNNING = True
    pygame.mixer.init()
    display.update()
    sql_schema.init()
    controls.buttons_sliders(oscillator, envelope, effects, mixer)

    while RUNNING:
        ui_action(oscillator)
        controls.root.update()
        pygame.display.update()
