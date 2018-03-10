# coding=utf-8

import sys
import random
import datetime

#if not using colorama comment out the next two lines
import colorama
colorama.init()


cMax = 1000
def vertausche(Feld, i, j):
    Feld[i], Feld[j] = Feld[j], Feld [i]
    return Feld

def AuswahlSort(Feld):
    for grenze in range(len(Feld)):
        kleinstes = grenze;
        for i in range(grenze, len(Feld)):
            if Feld[i] < Feld[kleinstes]:
                kleinstes = i
        Feld = vertausche(Feld, grenze, kleinstes)
    return Feld

def EinSort(Feld):
    def FuegeEin(Feld, i):
        Inhalt = Feld[i]
        while ((i > 0) & (Feld[i - 1] > Inhalt)):
            Feld[i] = Feld[i - 1]
            i -= 1
        Feld[i] = Inhalt
        return Feld
    for grenze in range(1, len(Feld) - 1):
        Feld = FuegeEin(Feld, grenze)
    return Feld

def BubbleSort(Feld):
    for grenze in range(len(Feld) - 1):
        for i in range(len(Feld) - 1, grenze, -1):
            if (Feld[i - 1] > Feld[i]):
                vertausche(Feld, i, i - 1)
    return Feld

def BubbleSort2(Feld):
    grenze = 0
    while (grenze < len(Feld)):
        merke = len(Feld)
        for i in range(len(Feld) - 1, grenze, -1):
            if (Feld[i - 1] > Feld[i]):
                vertausche(Feld, i, i - 1)
                merke = i
        grenze = merke
    return Feld

# Zufall + arrayLänge
# InformationsAusgabe ( Zeit, #Aufrufe)

# 1 Datei Sort 7a, 7b, 7c

def FuelleZufall(ArrayLaenge, ZufallMin, ZufallMax):
    Feld = []
    for i in range(ArrayLaenge):
        Feld.append(random.randint(ZufallMin, ZufallMax))
    return Feld

def Eingabe(Nachricht, Fehlermeldung):
    print(colorama.Fore.GREEN + Nachricht + colorama.Fore.CYAN)
    Eingabe = None
    while (Eingabe == None):
        try:
            Eingabe = int(input(">"))
        except ValueError:
            print(colorama.Fore.RED + Fehlermeldung + colorama.Style.RESET_ALL)
    return Eingabe

Fehler = "Bitte Geben Sie eine ganze natürliche Zahl an."

UserFeld = None

ArrayLaenge = Eingabe("Bitte die Länge des Feldes angeben:", Fehler)
while (UserFeld == None):
    ZufallMin = Eingabe("Bitte den niedrigsten Wert angebe:", Fehler)
    ZufallMax = Eingabe("Bitte den höchsten Wert angeben:", Fehler)
    try:
        UserFeld = FuelleZufall(ArrayLaenge, ZufallMin, ZufallMax)
    except ValueError:
        print("\033[2J\033[1;1f" + colorama.Fore.RED + "Fehler: niedrigster Wert (" + str(ZufallMin) + ") ist größer höchster Wert (" + str(ZufallMax) + ")" + colorama.Style.RESET_ALL)

Zeiten = []
Aufrufe = []

def RufeAuf(Algorithmus, i):
    StartZeit = datetime.datetime.now()
    Algorithmus(UserFeld)
    Zeiten[i] = datetime.datetime.now() - StartZeit

print (UserFeld)
print (AuswahlSort(UserFeld))
print (EinSort(UserFeld))
print (BubbleSort(UserFeld))
print (BubbleSort2(UserFeld))
        