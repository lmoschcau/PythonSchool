# coding=utf-8
import sys
import random
import datetime
#if not using colorama comment out the next two lines
import colorama
colorama.init()

# Sortier-Algorithmen:
def vertausche( Feld, i, j ):
    Feld[i], Feld[j] = Feld[j], Feld[i]
    return Feld

def AuswahlSort( Feld ):
    for grenze in range(len(Feld)):
        kleinstes = grenze
        for i in range(grenze, len(Feld)):
            if Feld[i] < Feld[kleinstes]:
                kleinstes = i
        Feld = vertausche(Feld, grenze, kleinstes)
    return Feld

def EinSort( Feld ):
    def FuegeEin( Feld, i ):
        Inhalt = Feld[i]
        while ( ( i > 0 ) & ( Feld[i - 1] > Inhalt ) ):
            Feld[i] = Feld[i - 1]
            i -= 1
        Feld[i] = Inhalt
        return Feld
    for grenze in range(1, len(Feld)):
        Feld = FuegeEin(Feld, grenze)
    return Feld

def BubbleSort( Feld ):
    for grenze in range(len(Feld) - 1):
        for i in range(len(Feld) - 1, grenze, -1):
            if ( Feld[i - 1] > Feld[i] ):
                vertausche(Feld, i, i - 1)
    return Feld

def BubbleSort2( Feld ):
    grenze = 0
    while ( grenze < len(Feld) ):
        merke = len(Feld)
        for i in range(len(Feld) - 1, grenze, -1):
            if ( Feld[i - 1] > Feld[i] ):
                vertausche(Feld, i, i - 1)
                merke = i
        grenze = merke
    return Feld

# Zufall + arrayLänge
# InformationsAusgabe ( Zeit, #Aufrufe)
# 1 Datei Sort 7a, 7b, 7c

#███ Funktionen für Aufruf
# Funktion für das aufrufen von einem Sortieralgorithmus.
def RufeAuf( Algorithmus, AufrufFeld):
    sortiertesFeld = Algorithmus(AufrufFeld)
    print(sortiertesFeld)
    return sortiertesFeld

#███ Aufruf ( Hauptprogramm ):
print('\033[2J\033[1;1f', end='')
EingabeFeld = [10,8,6,9,3,5,2,1]
print(colorama.Fore.BLUE + '\033[2J\033[1;1funsortiertes Feld:' + colorama.Fore.CYAN)
print(EingabeFeld)

print(colorama.Fore.BLUE + '\nsortiertes Feld (Auswahl):' + colorama.Fore.CYAN)
RufeAuf(AuswahlSort, list(EingabeFeld))
print(colorama.Fore.BLUE + '\nsortiertes Feld (Einfügen):' + colorama.Fore.CYAN)
RufeAuf(EinSort, list(EingabeFeld))
print(colorama.Fore.BLUE + '\nsortiertes Feld (Bubble-Sort):' + colorama.Fore.CYAN)
RufeAuf(BubbleSort, list(EingabeFeld))
print(colorama.Fore.BLUE + '\nsortiertes Feld (Bubble+):' + colorama.Fore.CYAN)
RufeAuf(BubbleSort2, list(EingabeFeld))