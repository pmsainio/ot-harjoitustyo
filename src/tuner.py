def tune(tuning:int, freq:list):
    f = tuning
    step = 2**(1/12)
    for i in range(9):
        f /= step
        freq.insert(0, f)
    f = tuning
    freq.append(tuning)
    for i in range(1, 8):
        f *= step
        freq.append(f)
    return(freq)
