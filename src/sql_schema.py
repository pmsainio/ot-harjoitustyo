import sqlite3

db = sqlite3.connect("presets.db")
db.isolation_level = None

def init():
    #db.execute("drop TABLE if exists Presets;")
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
    except:
        pass

    try:
        db.execute("INSERT INTO Presets VALUES ('Sine', 100, 0, 0, 0, 1, 0, 0, 0)")
        db.execute("INSERT INTO Presets VALUES ('Triangle', 0, 100, 0, 0, 1, 0, 0, 0)")
        db.execute("INSERT INTO Presets VALUES ('Square', 0, 0, 100, 0, 0, 1, 0, 0)")
        db.execute("INSERT INTO Presets VALUES ('Sawtooth', 0, 0, 0, 100, 1, 0, 0, 0)")
    except:
        pass

def get_presets():
    presets = db.execute("SELECT name FROM Presets").fetchall()
    return presets

def load_preset_data(name):
    preset = db.execute("SELECT * FROM Presets WHERE name=?", [name[2:-3]]).fetchone()
    return preset

def save_preset(name, sine, triangle, square, sawtooth, attack, release, vibrato_f, vibrato_w):
    if name == "":
        return

    try:
        db.execute("INSERT INTO Presets (name, sine, triangle, square, sawtooth, \
                                         attack, release, vibrato_f, vibrato_w) \
                                         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                        [name, sine, triangle, square, sawtooth,
                                         attack, release, vibrato_f, vibrato_w])
    except:
        db.execute("UPDATE Presets SET sine=?, triangle=?, square=?, sawtooth=?, \
                                       attack=?, release=?, vibrato_f=?, vibrato_w=? \
                                       WHERE name=?", [sine, triangle, square, sawtooth,
                                       attack, release, vibrato_f, vibrato_w, name])

def delete_preset(name):
    db.execute("DELETE FROM Presets WHERE name=?", [name[2:-3]])

    
