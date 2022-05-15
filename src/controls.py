import tkinter as tk
from oscillator import Oscillator
from envelope import Envelope
from fx import Effects
from waves_mixer import WaveMixer
import sql_schema as sql

class Controls():
    """Ohjauspaneelista vastaava luokka. Toteuttaa käyttöliittymän toiminnallisuutta. Luokka on suuri lukuisten pienten osasten vuoksi.

    Attributes:
        oscillator: luokka, jolle välitetään viritystaajuus
        envelope: luokka, jolle välitetään alukkeiden (attack) ja lopukkeiden (release) pituudet
        effects: luokka, jolle välitetään vibraton taajuus ja amplitudi
        mixer: luokka, joka muodostaa halutunmuotoisen ääniaallon
    """
    def __init__(self, oscillator:Oscillator, envelope:Envelope, effects:Effects, mixer:WaveMixer):
        """Luo ikkunan, napit ja säätimet, joilla ohjataan muita luokkia.
        """
        self.root = tk.Tk()
        self.root.title("Controls")
        self.presets = sql.get_presets()
        self.chosen_preset = tk.StringVar(self.root)

        self.preset_menu = tk.OptionMenu(self.root, self.chosen_preset, *self.presets)
        self.load_button = tk.Button(self.root, text="Load preset", command=self.load_preset)
        self.delete_button = tk.Button(self.root, text="Delete preset", command=self.delete_preset)
        self.name_preset = tk.Entry(self.root)
        self.save_button = tk.Button(self.root, text="Save preset", command=self.save_preset)
        self.reset_button = tk.Button(self.root, text="Factory reset", command=self.factory_reset)

        self.sine_level = tk.Scale(self.root, from_=100, to=0, command=mixer.set_sine)
        self.triangle_level = tk.Scale(self.root, from_=100, to=0, command=mixer.set_triangle)
        self.square_level = tk.Scale(self.root, from_=100, to=0, command=mixer.set_square)
        self.saw_level = tk.Scale(self.root, from_=100, to=0, command=mixer.set_sawtooth)

        self.tuner = tk.Scale(self.root, from_=450, to=420, command=oscillator.retune)
        self.attack = tk.Scale(self.root, from_=0.999e3, to=0.001e3, command=envelope.set_attack)
        self.release = tk.Scale(self.root, from_=500, to=0, command=envelope.set_release)
        self.volume = tk.Scale(self.root, from_=100, to=0, command=envelope.set_gain)

        self.tuner = tk.Scale(self.root, from_=450, to=420, command=oscillator.retune)
        self.attack = tk.Scale(self.root, from_=0.999e3, to=0.001e3, command=envelope.set_attack)
        self.release = tk.Scale(self.root, from_=500, to=0, command=envelope.set_release)
        self.volume = tk.Scale(self.root, from_=100, to=0, command=envelope.set_gain)

        self.vibrato_frequency = tk.Scale(self.root, from_=20, to=0, command=effects.set_vibrato_f)
        self.vibrato_width = tk.Scale(self.root, from_=20, to=0, command=effects.set_vibrato_w)
        self.vibrato_frequency.set(0)
        self.vibrato_width.set(0)

        self.tuner_label = tk.Label(self.root, text="Tuner")
        self.sine_label = tk.Label(self.root, text="Sine")
        self.triangle_label = tk.Label(self.root, text="Triangle")
        self.square__label = tk.Label(self.root, text="Square")
        self.saw_label = tk.Label(self.root, text="Sawtooth")
        self.attack_label = tk.Label(self.root, text="Attack")
        self.release_label = tk.Label(self.root, text="Release")
        self.volume_label = tk.Label(self.root, text="Master")

        self.vibrato_frequency_label = tk.Label(self.root, text="Vibrato F")
        self.vibrato_width_label = tk.Label(self.root, text="Vibrato W")

    def set_basics(self):
        """Laittaa ohajuspaneeliin tehdasasetukset
        """
        self.tuner.set(440)
        self.sine_level.set(0)
        self.triangle_level.set(100)
        self.square_level.set(0)
        self.saw_level.set(0)
        self.attack.set(20)
        self.release.set(200)
        self.vibrato_frequency.set(0)
        self.vibrato_width.set(0)
        self.volume.set(50)
        self.chosen_preset.set(self.presets[1])

    def grid(self):
        """Asettaa säätimet ja napit paikoilleen
        """
        self.preset_menu.grid(row=0, columnspan=4)
        self.load_button.grid(row=0, column=4, columnspan=2)
        self.delete_button.grid(row=0, column=6, columnspan=2)
        self.name_preset.grid(row=1, columnspan=4)
        self.save_button.grid(row=1, column=4, columnspan=2)
        self.reset_button.grid(row=1, column=6, columnspan=2)

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

    def update_preset_list(self):
        """Tyhjentää preset-taulukon ja hakee sinne uudet arvot sql-moduulista
        """
        menu = self.preset_menu["menu"]
        menu.delete(0, "end")
        self.presets = sql.get_presets()
        for preset in self.presets:
            menu.add_command(label=preset,
                             command=lambda value=preset: self.chosen_preset.set(value))


    def load_preset(self):
        """Kutsuu sql-moduulista halutun presetin arvot ja asettaa ne liukusäätimiin
        """
        if self.chosen_preset.get() == "":
            return
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
        """Hakee liukusäätimistä arvot ja välittää ne sql-moduulille tallennettavaksi. 
           Päivittää preset-taulukon, ja asettaa juuri tallenetun presetin valituksi
        """
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
        self.name_preset.delete(0, 'end')

    def delete_preset(self):
        """Välittää poistettavan presetin sql-moduulille ja päivittää preset-taulukon
        """
        sql.delete_preset(self.chosen_preset.get())
        self.update_preset_list()
        self.chosen_preset.set("")

    def factory_reset(self):
        """Kutsuu sql-moduulia palauttamaan tehdasasetukset ja palauttaa liukusäätimet
           alkuperäisiin asemiinsa
        """
        sql.factory_reset()
        self.update_preset_list()
        self.name_preset.delete(0, 'end')
        self.set_basics()
