import tkinter as tk
from tkinter import *
import gensound as gs
from oscillator import Oscillator

root = tk.Tk()
root.title("Controls")

def buttons_sliders(oscillator:Oscillator):
    sine_button = Button(root, text="Sine", padx=30, command=oscillator.switch_sound_sine)
    triangle_button = Button(root, text="Triangle", padx=25, command=oscillator.switch_sound_triangle)
    square_button = Button(root, text="Square", padx=25, command=oscillator.switch_sound_square)
    saw_button = Button(root, text="Sawtooth", padx=20, command=oscillator.switch_sound_saw)


    tuner = tk.Scale(root, from_=450, to=420, command=oscillator.retune)
    attack = tk.Scale(root, from_=0.999e3, to=0.001e3) # command=oscillator.set_attack
    release = tk.Scale(root, from_=500, to=0, command=oscillator.set_release)
    volume = tk.Scale(root, from_=100, to=0, command=oscillator.set_gain)
    tuner.set(440)

    tuner_label = Label(root, text="Tuner")
    attack_label = Label(root, text="Attack")
    release_label = Label(root, text="Release")
    volume_label = Label(root, text="Master")


    tuner.grid(row=0, column=0)
    sine_button.grid(row=0, column=1)
    triangle_button.grid(row=0, column=2)
    attack.grid(row=0, column=3)
    release.grid(row=0, column=4)
    volume.grid(row=0, column=5)

    tuner_label.grid(row=1, column=0)
    square_button.grid(row=1, column=1)
    saw_button.grid(row=1, column=2)
    attack_label.grid(row=1, column=3)
    release_label.grid(row=1, column=4)
    volume_label.grid(row=1, column=5)