import tkinter as tk
from tkinter import *
from oscillator import Oscillator
from envelope import Envelope
from fx import Effects
from waves_mixer import waveMixer
root = tk.Tk()
root.title("Controls")

def buttons_sliders(oscillator:Oscillator, envelope:Envelope, effects:Effects, mixer:waveMixer):
    """tämä funktio luo napit ja liukusäätimet syntetisaattorin ohjauspaneeliin
    """

    sine_level = Scale(root, from_=100, to=0, command=mixer.set_sine)
    triangle_level = Scale(root, from_=100, to=0, command=mixer.set_triangle)
    square_level = Scale(root, from_=100, to=0, command=mixer.set_square)
    saw_level = Scale(root, from_=100, to=0, command=mixer.set_sawtooth)
    triangle_level.set(100)


    tuner = Scale(root, from_=450, to=420, command=oscillator.retune)
    attack = Scale(root, from_=0.999e3, to=0.001e3, command=envelope.set_attack) 
    release = Scale(root, from_=500, to=0, command=envelope.set_release)
    volume = Scale(root, from_=100, to=0, command=envelope.set_gain)
    tuner.set(440)
    attack.set(20)
    release.set(200)
    volume.set(50)

    vibrato_frequency = Scale(root, from_=20, to=0, command=effects.set_vibrato_f)
    vibrato_width = Scale(root, from_=20, to=0, command=effects.set_vibrato_w)
    vibrato_frequency.set(0)
    vibrato_width.set(0)

    tuner_label = Label(root, text="Tuner")
    sine_label = Label(root, text="Sine")
    triangle_label = Label(root, text="Triangle")
    square__label = Label(root, text="Square")
    saw_label = Label(root, text="Sawtooth")
    attack_label = Label(root, text="Attack")
    release_label = Label(root, text="Release")
    volume_label = Label(root, text="Master")

    vibrato_frequency_label = Label(root, text="Vibrato F")
    vibrato_width_label = Label(root, text="Vibrato W")



    tuner.grid(row=0, column=0)
    sine_level.grid(row=0, column=1)
    triangle_level.grid(row=0, column=2)
    square_level.grid(row=0, column=3)
    saw_level.grid(row=0, column=4)
    
    tuner_label.grid(row=1, column=0)
    sine_label.grid(row=1, column=1)
    triangle_label.grid(row=1, column=2)
    square__label.grid(row=1, column=3)
    saw_label.grid(row=1, column=4)

    attack.grid(row=2, column=5)
    release.grid(row=2, column=6)
    vibrato_frequency.grid(row=2, column=7)
    vibrato_width.grid(row=2, column=8)
    volume.grid(row=2, column=9)

    attack_label.grid(row=3, column=5)
    release_label.grid(row=3, column=6)
    vibrato_frequency_label.grid(row=3, column=7)
    vibrato_width_label.grid(row=3, column=8)
    volume_label.grid(row=3, column=9)
