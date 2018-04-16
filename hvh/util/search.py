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

def bin(Feld, key):
    return binFunktion(Feld, 0, len(Feld), key)

def binFunktion(Feld, erstes, letztes, key):
    if (letztes < erstes):
        return False
    else:
        mitte = (erstes + letztes) / 2;
        if (key == Feld[mitte]):
            return True
        else:
            if (key < Feld[mitte]):
                return binFunktion(Feld, erstes, mitte - 1, key)
            else:
                return binFunktion(Feld, mitte + 1, letztes, key)