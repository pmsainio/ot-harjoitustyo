import tkinter as tk
from tkinter import *
from oscillator import Oscillator
from envelope import Envelope
from fx import Effects
from waves_mixer import WaveMixer
import sql_schema as sql

class Controls():
    def __init__(self, oscillator:Oscillator, envelope:Envelope, effects:Effects, mixer:WaveMixer):
        self.root = tk.Tk()
        self.root.title("Controls")
        self.presets = sql.get_presets()
        self.chosen_preset = tk.StringVar(self.root)

        self.preset_menu = tk.OptionMenu(self.root, self.chosen_preset, *self.presets)
        self.load_button = tk.Button(self.root, text="Load preset", command=self.load_preset)
        self.delete_button = tk.Button(self.root, text="Delete preset", command=self.delete_preset)
        self.name_preset = tk.Entry(self.root)
        self.save_button = tk.Button(self.root, text="Save preset", command=self.save_preset)
        self.reset_button = tk.Button(self.root, text="Reset originals", command=self.reset_originals)

        self.sine_level = Scale(self.root, from_=100, to=0, command=mixer.set_sine)
        self.triangle_level = Scale(self.root, from_=100, to=0, command=mixer.set_triangle)
        self.square_level = Scale(self.root, from_=100, to=0, command=mixer.set_square)
        self.saw_level = Scale(self.root, from_=100, to=0, command=mixer.set_sawtooth)

        self.tuner = Scale(self.root, from_=450, to=420, command=oscillator.retune)
        self.attack = Scale(self.root, from_=0.999e3, to=0.001e3, command=envelope.set_attack) 
        self.release = Scale(self.root, from_=500, to=0, command=envelope.set_release)
        self.volume = Scale(self.root, from_=100, to=0, command=envelope.set_gain)

        self.tuner = Scale(self.root, from_=450, to=420, command=oscillator.retune)
        self.attack = Scale(self.root, from_=0.999e3, to=0.001e3, command=envelope.set_attack) 
        self.release = Scale(self.root, from_=500, to=0, command=envelope.set_release)
        self.volume = Scale(self.root, from_=100, to=0, command=envelope.set_gain)

        self.vibrato_frequency = Scale(self.root, from_=20, to=0, command=effects.set_vibrato_f)
        self.vibrato_width = Scale(self.root, from_=20, to=0, command=effects.set_vibrato_w)
        self.vibrato_frequency.set(0)
        self.vibrato_width.set(0)

        self.tuner_label = Label(self.root, text="Tuner")
        self.sine_label = Label(self.root, text="Sine")
        self.triangle_label = Label(self.root, text="Triangle")
        self.square__label = Label(self.root, text="Square")
        self.saw_label = Label(self.root, text="Sawtooth")
        self.attack_label = Label(self.root, text="Attack")
        self.release_label = Label(self.root, text="Release")
        self.volume_label = Label(self.root, text="Master")

        self.vibrato_frequency_label = Label(self.root, text="Vibrato F")
        self.vibrato_width_label = Label(self.root, text="Vibrato W")

    def set_basics(self):
        self.triangle_level.set(100)
        self.tuner.set(440)
        self.attack.set(20)
        self.release.set(200)
        self.volume.set(50)
        self.chosen_preset.set(self.presets[3])

    def grid(self):
        self.preset_menu.grid(row=0, columnspan=4)
        self.load_button.grid(row=0, column=4, columnspan=2)
        self.delete_button.grid(row=0, column=6, columnspan=2)
        self.name_preset.grid(row=1, columnspan=4)
        self.save_button.grid(row=1, column=4, columnspan=2)

        self.tuner.grid(row=2, column=0)
        self.sine_level.grid(row=2, column=1)
        self.triangle_level.grid(row=2, column=2)
        self.square_level.grid(row=2, column=3)
        self.saw_level.grid(row=2, column=4)
        
        self.tuner_label.grid(row=3, column=0)
        self.sine_label.grid(row=3, column=1)
        self.triangle_label.grid(row=3, column=2)
        self.square__label.grid(row=3, column=3)
        self.saw_label.grid(row=3, column=4)

        self.attack.grid(row=4, column=4)
        self.release.grid(row=4, column=5)
        self.vibrato_frequency.grid(row=4, column=6)
        self.vibrato_width.grid(row=4, column=7)
        self.volume.grid(row=4, column=8)

        self.attack_label.grid(row=5, column=4)
        self.release_label.grid(row=5, column=5)
        self.vibrato_frequency_label.grid(row=5, column=6)
        self.vibrato_width_label.grid(row=5, column=7)
        self.volume_label.grid(row=5, column=8)

    def load_preset(self):
        data = sql.load_preset_data(self.chosen_preset.get())
        self.sine_level.set(data[1])
        self.triangle_level.set(data[2])
        self.square_level.set(data[3])
        self.saw_level.set(data[4])
        self.attack.set(data[5])
        self.release.set(data[6])
        self.vibrato_frequency.set(data[7])
        self.vibrato_width.set(data[8])

    def save_preset(self):
        sql.save_preset(
            self.name_preset.get(),
            self.sine_level.get(),
            self.triangle_level.get(),
            self.square_level.get(),
            self.saw_level.get(),
            self.attack.get(),
            self.release.get(),
            self.vibrato_frequency.get(),
            self.vibrato_width.get()
            )
        self.update_preset_list()
        self.chosen_preset.set(self.name_preset.get())

    def delete_preset(self):
        sql.delete_preset(self.chosen_preset.get())
        print(sql.get_presets())
        self.update_preset_list()
        self.chosen_preset.set("")

    def reset_originals(self):
        sql.reset_originals()

    def update_preset_list(self):
        menu = self.preset_menu["menu"]
        menu.delete(0, "end")
        self.presets = sql.get_presets()
        for preset in self.presets:
            print(preset)
            menu.add_command(label=preset, 
                             command=lambda value=preset: self.chosen_preset.set(value))


