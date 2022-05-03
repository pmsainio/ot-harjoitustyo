from sqlite3 import Row
import tkinter as tk
from tkinter import *
from oscillator import Oscillator
from envelope import Envelope
from fx import Effects

root = tk.Tk()
root.title("Controls")

def buttons_sliders(oscillator:Oscillator, envelope:Envelope, effects:Effects):
    sine_button = Button(root, text="Sine", padx=30, command=oscillator.switch_sound_sine)
    triangle_button = Button(root, text="Triangle", padx=25, command=oscillator.switch_sound_triangle)
    square_button = Button(root, text="Square", padx=25, command=oscillator.switch_sound_square)
    saw_button = Button(root, text="Sawtooth", padx=20, command=oscillator.switch_sound_saw)


    tuner = tk.Scale(root, from_=450, to=420, command=oscillator.retune)
    attack = tk.Scale(root, from_=0.999e3, to=0.001e3, command=envelope.set_attack) 
    release = tk.Scale(root, from_=500, to=0, command=envelope.set_release)
    volume = tk.Scale(root, from_=100, to=0, command=envelope.set_gain)
    tuner.set(440)
    attack.set(20)
    release.set(200)
    volume.set(50)

    hipass_filter = tk.Scale(root, from_=20000, to=10, command=effects.set_filter)
    vibrato_frequency = tk.Scale(root, from_=20, to=0, command=effects.set_vibrato_f)
    vibrato_width = tk.Scale(root, from_=20, to=0, command=effects.set_vibrato_w)
    hipass_filter.set(20000)
    vibrato_frequency.set(0)
    vibrato_width.set(0)

    tuner_label = Label(root, text="Tuner")
    attack_label = Label(root, text="Attack")
    release_label = Label(root, text="Release")
    volume_label = Label(root, text="Master")

    hp_filter_label = Label(root, text="HPF")
    vibrato_frequency_label = Label(root, text="Vibrato F")
    vibrato_width_label = Label(root, text="Vibrato W")



    tuner.grid(row=0, column=0)
    sine_button.grid(row=0, column=1)
    triangle_button.grid(row=0, column=2)
    attack.grid(row=0, column=3)
    release.grid(row=0, column=4)
    hipass_filter.grid(row=0, column=5)
    vibrato_frequency.grid(row=0, column=7)
    vibrato_width.grid(row=0, column=8)
    volume.grid(row=0, column=9)

    tuner_label.grid(row=1, column=0)
    square_button.grid(row=1, column=1)
    saw_button.grid(row=1, column=2)
    attack_label.grid(row=1, column=3)
    release_label.grid(row=1, column=4)
    hp_filter_label.grid(row=1, column=5)
    vibrato_frequency_label.grid(row=1, column=7)
    vibrato_width_label.grid(row=1, column=8)
    volume_label.grid(row=1, column=9)