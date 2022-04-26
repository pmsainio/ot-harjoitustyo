def tune(tuning: int):
    freq = []
    key_f = tuning
    step = 2**(1/12)
    for i in range(9):
        key_f /= step
        freq.insert(0, key_f)
    key_f = tuning
    freq.append(tuning)
    for i in range(1, 8):
        key_f *= step
        freq.append(key_f)
    print(freq)
    return freq
    