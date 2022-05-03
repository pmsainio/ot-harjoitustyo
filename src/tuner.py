def tune(tuning: int):
    """ Funktiolle annetaan viritysääni, jonka pohjalta tämä luo
    listan taajuuksista koskettimiston alueella. Taajuusero on
    on 2**(1/12)-kertainen vierekkäisten kosketinten välillä.
    """
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
    return freq
