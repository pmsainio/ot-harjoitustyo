import pygame
from ui import ui_action
from visuals import Display
from oscillator import Oscillator
from envelope import Envelope
from waves_mixer import WaveMixer
from fx import Effects
from controls import Controls
import sql_schema

pygame.font.init()

if __name__ == "__main__":
    effects = Effects()
    envelope = Envelope(effects)
    mixer = WaveMixer()
    oscillator = Oscillator(envelope, mixer)
    controls = Controls(oscillator, envelope, effects, mixer)
    controls.set_basics()
    controls.grid()
    sql_schema.init()
    display = Display()
    pygame.mixer.init()
    display.update()
    RUNNING = True    

    while RUNNING:
        ui_action(oscillator)
        controls.root.update()
        pygame.display.update()
