import sys
import random
import datetime

#if not using colorama comment out the next two lines
import colorama
colorama.init()


T = 1

def test(T_):
    print(T_)
    print(T)
    T_ = 111
    print(T_)
    print(T)
    return T_


print(T)
print(test(T))
print(T)

AnzahlAufrufe = 0
AnzahlAbfragen = 0

cMax = 1000
def vertausche(VertauscheFeld, i, j):
    hilf = VertauscheFeld[i]
    VertauscheFeld[i] = VertauscheFeld[j]
    VertauscheFeld[j] = hilf
    return VertauscheFeld

def AuswahlSort(Feld):
    global AnzahlAufrufe
    global AnzahlAbfragen
    for grenze in range(len(Feld)):
        kleinstes = grenze;
        for i in range(grenze, len(Feld)):
            AnzahlAufrufe += 1                                  #Zähler
            if Feld[i] < Feld[kleinstes]:
                kleinstes = i
                AnzahlAbfragen += 1                             #Zähler
        Feld = vertausche(Feld, grenze, kleinstes)
    return Feld

def EinSort(Feld):
    def FuegeEin(Inhalt, Feld, i):
        global AnzahlAufrufe
        global AnzahlAbfragen

        while ((i > 0) & (Feld[i] > Inhalt)):
            Feld[i + 1] = Inhalt
            i-= 1
            AnzahlAbfragen += 1                                 #Zähler
        Feld[i + 1] = Inhalt
        AnzahlAufrufe += 1                                  #Zähler
        return Feld
    for grenze in range(1, len(Feld)):
        Feld = FuegeEin(Feld[grenze], Feld, grenze - 1)
    return Feld

def BubbleSort(Feld):
    global AnzahlAufrufe
    global AnzahlAbfragen

    for grenze in range(len(Feld) - 1):
        for i in range(len(Feld) - 1, grenze, -1):
            AnzahlAufrufe += 1                                  #Zähler
            if (Feld[i - 1] > Feld[i]):
                vertausche(Feld, i, i - 1)
                AnzahlAbfragen += 1                             #Zähler
    return Feld

def BubbleSort2(Feld):
    global AnzahlAufrufe
    global AnzahlAbfragen

    grenze = 1
    while (grenze < len(Feld)):
        merke = len(Feld)
        for i in range(len(Feld) - 1, grenze, -1):
            AnzahlAufrufe += 1                                  #Zähler
            if (Feld[i - 1] > Feld[i]):
                vertausche(Feld, i, i - 1)
                merke = i
                AnzahlAbfragen += 1                             #Zähler
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
    ZufallMin = Eingabe("Bitte den niedrigsten Wert angebe:", Fehler)
    ZufallMax = Eingabe("Bitte den höchsten Wert angeben:", Fehler)
    try:
        EingabeFeld = FuelleZufall(ArrayLaenge, ZufallMin, ZufallMax)
    except ValueError:
        print("\033[2J\033[1;1f" + colorama.Fore.RED + "Fehler: niedrigster Wert (" + str(ZufallMin) + ") ist größer höchster Wert (" + str(ZufallMax) + ")" + colorama.Style.RESET_ALL)

Zeiten = [None] * 4
Aufrufe = [None] * 4
Abfragen = [None] * 4

def RufeAuf(Algorithmus, AufrufFeld, i):
    print("Hello")
    global AnzahlAufrufe
    global AnzahlAbfragen
    AnzahlAufrufe = 0
    AnzahlAbfragen = 0
    StartZeit = datetime.datetime.now()
    print(Algorithmus(AufrufFeld))
    Zeiten[i] = datetime.datetime.now() - StartZeit
    Aufrufe[i] = AnzahlAufrufe
    Abfragen[i] = AnzahlAbfragen

    print("AnzahlAufrufe: " + str(AnzahlAufrufe) + " AnzahlAbfragen: " + str(AnzahlAbfragen) + " Zeit: " + str(Zeiten[i]))

    
FeldA = [10,9,7,6,5,4,3,2,1]
print (FeldA)

RufeAuf(AuswahlSort, FeldA, 0)
FeldA = [10,9,7,6,5,4,3,2,1]
print (FeldA)
RufeAuf(EinSort, FeldA, 1)
FeldA = [10,9,7,6,5,4,3,2,1]
print (FeldA)
RufeAuf(BubbleSort, FeldA, 2)
FeldA = [10,9,7,6,5,4,3,2,1]
print (FeldA)
RufeAuf(BubbleSort2, FeldA, 3)

#print (AuswahlSort(EingabeFeld))
#print (EinSort(EingabeFeld))
#print (BubbleSort(EingabeFeld))
#print (BubbleSort2(EingabeFeld))