# coding=utf-8

import sys
import random
import datetime

#if not using colorama comment out the next two lines
import colorama
colorama.init()

AnzahlAufrufe = 0
AnzahlAbfragen = 0

cMax = 1000
def vertausche(Feld, i, j):
    Feld[i], Feld[j] = Feld[j], Feld [i]
    return Feld

def AuswahlSort(Feld):
    global AnzahlAufrufe
    global AnzahlAbfragen
    for grenze in range(len(Feld)):
        kleinstes = grenze;
        for i in range(grenze, len(Feld)):
            AnzahlAufrufe += 1                                  #Zähler
            if Feld[i] < Feld[kleinstes]:
                kleinstes = i
                AnzahlAbfragen += 1                                 #Zähler
        Feld = vertausche(Feld, grenze, kleinstes)
    return Feld

def EinSort(Feld):
    def FuegeEin(Feld, i):
        global AnzahlAufrufe
        global AnzahlAbfragen
        Inhalt = Feld[i]
        while ((i > 0) & (Feld[i - 1] > Inhalt)):
            Feld[i] = Feld[i - 1]
            i -= 1
            AnzahlAbfragen += 1                                     #Zähler
        Feld[i] = Inhalt
        AnzahlAufrufe += 1                                      #Zähler
        return Feld
    for grenze in range(1, len(Feld)):
        Feld = FuegeEin(Feld, grenze)
    return Feld

def BubbleSort(Feld):
    global AnzahlAufrufe
    global AnzahlAbfragen
    for grenze in range(len(Feld) - 1):
        for i in range(len(Feld) - 1, grenze, -1):
            AnzahlAufrufe += 1                                  #Zähler
            if (Feld[i - 1] > Feld[i]):
                vertausche(Feld, i, i - 1)
                AnzahlAbfragen += 1                                 #Zähler
    return Feld

def BubbleSort2(Feld):
    global AnzahlAufrufe
    global AnzahlAbfragen
    grenze = 0
    while (grenze < len(Feld)):
        merke = len(Feld)
        for i in range(len(Feld) - 1, grenze, -1):
            AnzahlAufrufe += 1                                  #Zähler
            if (Feld[i - 1] > Feld[i]):
                vertausche(Feld, i, i - 1)
                merke = i
                AnzahlAbfragen += 1                                 #Zähler
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

EingabeFeld = None

ArrayLaenge = Eingabe("Bitte die Länge des Feldes angeben:", Fehler)
while (EingabeFeld == None):
    ZufallMin = Eingabe("Bitte den niedrigsten Wert angeben:", Fehler)
    ZufallMax = Eingabe("Bitte den höchsten Wert angeben:", Fehler)
    try:
        EingabeFeld = FuelleZufall(ArrayLaenge, ZufallMin, ZufallMax)
    except ValueError:
        print("\033[2J\033[1;1f" + colorama.Fore.RED + "Fehler: niedrigster Wert (" + str(ZufallMin) + ") ist größer höchster Wert (" + str(ZufallMax) + ")" + colorama.Style.RESET_ALL)

Zeiten = [None] * 4
Aufrufe = [None] * 4
Abfragen = [None] * 4

def Visualisierung(Feld):
    for i in range(max(Feld), min(Feld) - 1, -1):
        horizontal = ' '
        for j in range(len(Feld)):
            if Feld[j] >= i:
                horizontal += '#'
            else:
                horizontal += ' '
        print horizontal

def RufeAuf(Algorithmus, AufrufFeld, i):
    global AnzahlAufrufe
    global AnzahlAbfragen
    AnzahlAufrufe = 0
    AnzahlAbfragen = 0
    StartZeit = datetime.datetime.now()
    sortiertesFeld = Algorithmus(AufrufFeld)
    Zeiten[i] = datetime.datetime.now() - StartZeit
    Aufrufe[i] = AnzahlAufrufe
    Abfragen[i] = AnzahlAbfragen
    print '\n'
    Visualisierung(sortiertesFeld)
    print("AnzahlAufrufe: " + str(AnzahlAufrufe) + " AnzahlAbfragen: " + str(AnzahlAbfragen) + " Zeit: " + str(Zeiten[i]))

    return sortiertesFeld

    
print (colorama.Fore.BLUE + str(EingabeFeld) + colorama.Style.RESET_ALL)

print '\nunsortiertes Feld:\n'
Visualisierung(list(EingabeFeld))

print '\nsortiertes Feld (Auswahl):'
RufeAuf(AuswahlSort, list(EingabeFeld), 0)
print '\nsortiertes Feld (Einfügen):'
RufeAuf(EinSort, list(EingabeFeld), 1)
print '\nsortiertes Feld (Bubble-Sort):'
RufeAuf(BubbleSort, list(EingabeFeld), 2)
print '\nsortiertes Feld (Bubble+):'
RufeAuf(BubbleSort2, list(EingabeFeld), 3)
result = AuswahlSort( list(EingabeFeld))
        