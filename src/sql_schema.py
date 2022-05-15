import sqlite3

db = sqlite3.connect("presets.db")
db.isolation_level = None

def init():
    """Luo taulukon ja presetit, mikäli niitä ei ole.
    """
    try:
        db.execute("CREATE TABLE Presets (name TEXT UNIQUE,\
                                          sine INTEGER,\
                                          triangle INTEGER,\
                                          square INTEGER, \
                                          sawtooth INTEGER, \
                                          attack INTEGER, \
                                          release INTEGER, \
                                          vibrato_f INTEGER, \
                                          vibrato_w INTEGER)")
    except sqlite3.OperationalError:
        pass

    try:
        db.execute("INSERT INTO Presets VALUES ('1 Sine', 100, 0, 0, 0, 1, 0, 0, 0)")
        db.execute("INSERT INTO Presets VALUES ('2 Triangle', 0, 100, 0, 0, 1, 0, 0, 0)")
        db.execute("INSERT INTO Presets VALUES ('3 Square', 0, 0, 100, 0, 0, 1, 0, 0)")
        db.execute("INSERT INTO Presets VALUES ('4 Sawtooth', 0, 0, 0, 100, 1, 0, 0, 0)")
        db.execute("INSERT INTO Presets VALUES ('Bee', 0, 60, 70, 35, 20, 200, 20, 14)")
        db.execute("INSERT INTO Presets VALUES ('Cat', 80, 60, 15, 30, 120, 50, 0, 0)")
        db.execute("INSERT INTO Presets VALUES ('Skeleton', 100, 15, 45, 30, 1, 0, 20, 20)")
        db.execute("INSERT INTO Presets VALUES ('Snake', 0, 100, 30, 65, 20, 200, 3, 7)")

    except sqlite3.IntegrityError:
        pass

def get_presets():
    presets = db.execute("SELECT name FROM Presets").fetchall()
    return presets

def load_preset_data(name):
    """Ottaa presetin nimen ja palauttaa sen mukaiset asetukset. Joskus nimi on muodossa "('nimi,')",
    mistä ehtolause.
    """
    if name[0] == "(":
        name = name[2:-3]
    preset = db.execute("SELECT * FROM Presets WHERE name=?", [name]).fetchone()
    return preset

def save_preset(name, sine, triangle, square, sawtooth, attack, release, vibrato_f, vibrato_w):
    """Tallentaa presetin arvot taulukkoon tai, jos nimi on varattu, päivittää olemassa olevan rivin.
    """
    if name == "":
        return

    try:
        db.execute("INSERT INTO Presets (name, sine, triangle, square, sawtooth, \
                                         attack, release, vibrato_f, vibrato_w) \
                                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                        [name, sine, triangle, square, sawtooth,
                                         attack, release, vibrato_f, vibrato_w])
    except sqlite3.IntegrityError:
        db.execute("UPDATE Presets SET sine=?, triangle=?, square=?, sawtooth=?, \
                                       attack=?, release=?, vibrato_f=?, vibrato_w=? \
                                       WHERE name=?", [sine, triangle, square, sawtooth,
                                       attack, release, vibrato_f, vibrato_w, name])

def delete_preset(name):
    db.execute("DELETE FROM Presets WHERE name=?", [name[2:-3]])

def factory_reset():
    """Tuhoaa taulukon sisältöineen ja alustaa sen uudestaan.
    """
    db.execute("drop TABLE if exists Presets")
    init()
