import sqlite3

db = sqlite3.connect("presets.db")
db.isolation_level = None

def init():
    
    try:
        db.execute("CREATE TABLE Presets (name TEXT,\
                                          values INTEGER")
    except:
        pass

    try:
        db.execute("INSERT INTO Presets (name, values)\
                    VALUES ('Sine', [100, 0, 0, 0, 0, 0, 0, 0])")
        db.execute("INSERT INTO Presets (name, values)\
                    VALUES ('Triangle', [0, 100, 0, 0, 0, 0, 0, 0])")
        db.execute("INSERT INTO Presets (name, values)\
                    VALUES ('Square', [0, 0, 100, 0, 0, 0, 0, 0])")
        db.execute("INSERT INTO Presets (name, values)\
                    VALUES ('Sawtooth', [0, 0, 0, 100, 0, 0, 0, 0])")
    except:
        pass

def save_preset(name, values:list):
    try:
        db.execute("INSERT INTO Presets (name, values) \
                                         VALUES (?, ?)",
                                        [name, [values[0], values[1], 
                                         values[2], values[3], values[4], 
                                         values[5], values[6], values[7]]])
    except:
        # if name in presets:
        # db.execute("UPDATE
        #else:
            pass

def load_preset(name):
    db.execute("SELECT * FROM Presets WHERE name=:?", [name]).fetchone()