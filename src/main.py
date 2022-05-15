import pygame
from user_interface.keyboard import ui_action
from user_interface.visuals import Display
from user_interface.controls import Controls
from signal_prosessing.oscillator import Oscillator
from signal_prosessing.envelope import Envelope
from signal_prosessing.waves_mixer import WaveMixer
from signal_prosessing.fx import Effects
import sql.sql_schema as sql
 
pygame.font.init()

if __name__ == "__main__":
    sql.init()
    effects = Effects()
    envelope = Envelope(effects)
    mixer = WaveMixer()
    oscillator = Oscillator(envelope, mixer)
    controls = Controls(oscillator, envelope, effects, mixer)
    controls.set_basics()
    controls.grid()
    display = Display()
    pygame.mixer.init()
    display.update()
    RUNNING = True

    while RUNNING:
        ui_action(oscillator)
        controls.root.update()
        pygame.display.update()
