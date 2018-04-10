# coding=utf-8
import sys
import colorama
import math as m
import inspect
colorama.init()

#███ Universelle Funktionen:
# Eine universelle Funktion für die Eingabe eines Wertes eines bestimmten
# Wertes.  Bei falscher Eingabe Erfolgt Eine Fehlermeldung

def Eingabe( Nachricht, typ, Fehlermeldung ):
    print(colorama.Fore.GREEN + Nachricht + colorama.Fore.CYAN)
    NutzerEingabe = None
    while ( NutzerEingabe == None ):
        try:
            NutzerEingabe = typ(input(">"))
        except ValueError:
            print(colorama.Fore.RED + Fehlermeldung + colorama.Fore.CYAN)
    return NutzerEingabe
# Universelle Funktion für die Eingabe eines Eintrags aus einer Auswahl.
def Auswahl( Auswaehlbar, Nachricht ):
    Ausgewaehlt = None
    while ( Ausgewaehlt == None ):
        NutzerEingabe = Eingabe(Nachricht, str, "Bitte einen Eintrag aus der Auswahl angeben.")
        NutzerEingabe = NutzerEingabe.lower()[:1]
        try:
            Ausgewaehlt = Auswaehlbar[NutzerEingabe]
        except KeyError:
            print("\033[2J\033[1;1f" + colorama.Fore.RED + "Fehler: Die Eingabe (" + str(NutzerEingabe) + ") ist keine gültige Auswahl!" + colorama.Style.RESET_ALL)
    return Ausgewaehlt

def Verarbeiten(minimum, maximum):
    Bereich = range(minimum, maximum)
    Ergebnisse = []
    for x in Bereich:
        Ergebnisse.append(int(BerechneFunktion(Funktion, x)))
    return Ergebnisse

def BerechneFunktion(FunktionString, x):
    return eval(FunktionString)

def AufMathModulVerweisen(Funktion):
    for i in range(len(NutzbarDict)):
        Funktion = Funktion.replace(NutzbarDict[i][0], "m." + NutzbarDict[i][0])
    return Funktion

def Visualisiere(Feld):
    for y in range(max(Feld), min(Feld) - 1, -1):
        horizontal = ' '
        for x in range(len(Feld)):
            try:
                if (Feld[x] >= y > Feld[x - 1]) | (Feld[x] < y <= Feld[x - 1]):
                    horizontal += '█'
                else:
                    horizontal += ' '
            except(IndexError):
                if Feld[x] == y:
                    horizontal += '█'
                else:
                    horizontal += ' '

        print(horizontal)

NutzbarDict = inspect.getmembers(m, predicate=inspect.isbuiltin)
if (Auswahl({"j":True, "n":False, "t":True, "f":False, "1":True, "0":False}, "Sollen alle nutzbaren mathematischen Operatoren einmal angezeigt werden Ja[J] Nein[N]") == True):
    for i in range(len(NutzbarDict)):
        print(str(i) + ".] " + NutzbarDict[i][0] + ": " + NutzbarDict[i][1].__doc__)



Funktion = Eingabe("Bitte die Funktion f(x) eingeben.", str, "Die Eingabe ist nicht gültig")
FunktionAbleitung = Eingabe("Bitte die erste Ableitung f'(x) der Funktion f(x) eingeben.", str, "Die Eingabe ist nicht gültig")

Funktion = AufMathModulVerweisen(Funktion)
FunktionAbleitung = AufMathModulVerweisen(FunktionAbleitung)

print(Funktion)
print(FunktionAbleitung)

Feld = Verarbeiten(-10, 20)
Visualisiere(Feld)
x0 = 5
for Nullstelle in range(10):
    x0 = x0 - (BerechneFunktion(Funktion, x0) / BerechneFunktion(FunktionAbleitung, x0))
print(str(x0))
input('exit?')