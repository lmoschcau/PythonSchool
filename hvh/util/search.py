def sequ(Feld, key):
    i = 0
    while (Feld[i] != key and i < len(Feld) - 1):
        i += 1
    return (Feld[i] == key)

def sequ2(Feld, key):
    Feld.append(key)
    i = 0
    while Feld[i] != key:
        i += 1
    return (i != len(Feld) - 1)
