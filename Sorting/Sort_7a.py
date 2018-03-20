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

def QuickSort( Feld):
    return QuickSortFunktion(Feld, 0, len(Feld) - 1)
def QuickSortFunktion( Feld, erstes, letztes ):
 
    global AnzahlFeldLesen
    global AnzahlFeldSchreiben
    if ( erstes < letztes ):
        mitte = ( erstes + letztes ) // 2
        vergleichselement = Feld[mitte]
        vonlinks = erstes
        vonrechts = letztes
        while ( vonlinks <= vonrechts ):
            while ( Feld[vonlinks] < vergleichselement ):
                vonlinks += 1
                AnzahlFeldLesen += 1                                 #Zähler
            while ( Feld[vonrechts] > vergleichselement ):
                vonrechts -= 1
                AnzahlFeldLesen += 1                                 #Zähler
            if ( vonlinks <= vonrechts ):
                vertausche(Feld, vonlinks, vonrechts)
                AnzahlFeldSchreiben += 1                                 #Zähler
                vonlinks += 1
                vonrechts -= 1
        Feld = QuickSortFunktion(Feld, erstes, vonrechts)
        Feld = QuickSortFunktion(Feld, vonlinks, letztes)
    return Feld

# Zufall + arrayLänge
# InformationsAusgabe ( Zeit, #Lesen)
# 1 Datei Sort 7a, 7b, 7c

#███ Universelle Funktionen:
# Eine universelle Funktion für die Eingabe eines Wertes eines bestimmten
# Wertes.  Bei falscher Eingabe Erfolgt Eine Fehlermeldung
def Eingabe( Nachricht, typ, Fehlermeldung ):
    print(colorama.Fore.GREEN + Nachricht + colorama.Fore.CYAN)
    Eingabe = None
    while ( Eingabe == None ):
        try:
            Eingabe = typ(input(">"))
        except ValueError:
            print(colorama.Fore.RED + Fehlermeldung + colorama.Fore.CYAN)
    return Eingabe
# Universelle Funktion für die Eingabe eines Eintrags aus einer Auswahl.
def Auswahl( Auswaehlbar, Nachricht ):
    Ausgewaehlt = None
    while ( Ausgewaehlt == None ):
        NutzerEingabe = Eingabe(Nachricht, str, "Bitte einen Eintrag aus der auswahl angeben.")
        NutzerEingabe = NutzerEingabe.lower()[:1]
        try:
            Ausgewaehlt = Auswaehlbar[NutzerEingabe]
        except KeyError:
            print("\033[2J\033[1;1f" + colorama.Fore.RED + "Fehler: Die Eingabe (" + str(NutzerEingabe) + ") ist keine gültige Auswahl!" + colorama.Style.RESET_ALL)
    return Ausgewaehlt

#███ Eingabe Zufälliges Feld Funktionen:
# Ein Feld mit Zufälligen Zahlen zwischen min und max erstellen
# ==> random.shuffle(range(100))
def EingabeMinMax(Fehler):
    ZufallMin = Eingabe("Bitte den niedrigsten Wert angeben:", int, Fehler)
    ZufallMax = Eingabe("Bitte den höchsten Wert angeben:", int, Fehler)
    return ZufallMin, ZufallMax

def ZufallMinMax(Fehler):
    ArrayLaenge = Eingabe("Bitte die Länge des Feldes angeben:", int, Fehler)
    EingabeFeld = None
    while ( EingabeFeld == None ):
        ZufallMin, ZufallMax = EingabeMinMax(Fehler)
        try:
            EingabeFeld = FuelleZufall(ArrayLaenge, ZufallMin, ZufallMax)
        except ValueError:
            print("\033[2J\033[1;1f" + colorama.Fore.RED + "Fehler: niedrigster Wert (" + str(ZufallMin) + ") ist größer höchster Wert (" + str(ZufallMax) + ")!" + colorama.Style.RESET_ALL)
    return EingabeFeld

def MischenMinMax(Fehler):
    ZufallMin, ZufallMax = EingabeMinMax(Fehler)
    EingabeFeld = list(range(ZufallMin, ZufallMax + 1))
    random.shuffle(EingabeFeld)
    return EingabeFeld

def AufsteigenMinMax(Fehler):
    ZufallMin, ZufallMax = EingabeMinMax(Fehler)
    return list(range(ZufallMin, ZufallMax + 1))

def AbsteigenMinMax(Fehler):
    ZufallMin, ZufallMax = EingabeMinMax(Fehler)
    return list(range(ZufallMax, ZufallMin - 1, -1))

def InitialisierungFeld( ):
    ZufallModus = Auswahl({"z":ZufallMinMax, "m":MischenMinMax, "a":AufsteigenMinMax, "d":AbsteigenMinMax}, "Auf welche Weise soll das Feld befüllt werden?\n  zufällige Zahlen von Min bis Max[Z]\n  gemischtes Feld von Min bis Max[M]\n  aufsteigend von Min bis Max[A]\n  absteigend von Min bis Max[D]")
    Fehler = "Bitte Geben Sie eine ganze natürliche Zahl an."
    return ZufallModus(Fehler)
#███ Funktionen für Aufruf und Überprüfung
# Funktion für das aufrufen von einem Sortieralgorithmus.
# Setzt die Werte für die Statistik in einem Feld auf die Werte des aktuellen
# Algorithmus.
def RufeAuf( Algorithmus, AufrufFeld, i ):
    sortiertesFeld = Algorithmus(AufrufFeld)
    print('\n')
    print(sortiertesFeld)
    return sortiertesFeld

# Funktion für das Überprüfen der Richtigkeit der Felder inerhalb eines Feldes
# Schema: FeldFeld[Feld, Feld, Feld, Feld]
def Ueberpruefen( FeldFeld ):

    def HinzufuegenWennNichtLetztes( Text, Index, Laenge ):
        if ( Index != Laenge - 1 ):
            return Text
        return ""

    FeldFehler = False
    AusgabeString = colorama.Fore.BLUE + "["
    for i in range(len(FeldFeld[0])):
        gleich = True
        for j in range(0, len(FeldFeld)):
            if ( ( FeldFeld[j][i] != FeldFeld[0][i] ) | ( FeldFeld[j][max(i - 1, 0)] > FeldFeld[j][i] ) ):
                gleich = False

        if ( gleich == False ):
            FeldFehler = True
            for j in range(0, len(FeldFeld)):
                AusgabeString += colorama.Fore.RED + str(FeldFeld[j][i]) + HinzufuegenWennNichtLetztes("/ ", j, len(FeldFeld))
            AusgabeString += colorama.Fore.BLUE + HinzufuegenWennNichtLetztes(", ", i, len(FeldFeld[0]))
        else:
            AusgabeString += colorama.Fore.GREEN + str(FeldFeld[0][i]) + colorama.Fore.BLUE + HinzufuegenWennNichtLetztes(", ", i, len(FeldFeld[0]))
    AusgabeString += colorama.Fore.BLUE + "]"
    print(AusgabeString)
    return FeldFehler

#███ Aufruf ( Hauptprogramm ):
print('\033[2J\033[1;1f', end='')
EingabeFeld = InitialisierungFeld()
print(colorama.Fore.BLUE + '\033[2J\033[1;1funsortiertes Feld:' + colorama.Fore.CYAN)
print(EingabeFeld)

print(colorama.Fore.BLUE + '\nsortiertes Feld (Auswahl):' + colorama.Fore.CYAN)
res1 = RufeAuf(AuswahlSort, list(EingabeFeld), 0)
print(colorama.Fore.BLUE + '\nsortiertes Feld (Einfügen):' + colorama.Fore.CYAN)
res2 = RufeAuf(EinSort, list(EingabeFeld), 1)
print(colorama.Fore.BLUE + '\nsortiertes Feld (Bubble-Sort):' + colorama.Fore.CYAN)
res3 = RufeAuf(BubbleSort, list(EingabeFeld), 2)
print(colorama.Fore.BLUE + '\nsortiertes Feld (Bubble+):' + colorama.Fore.CYAN)
res4 = RufeAuf(BubbleSort2, list(EingabeFeld), 3)
print(colorama.Fore.BLUE + '\nsortiertes Feld (Quick):' + colorama.Fore.CYAN)
res5 = RufeAuf(QuickSort, list(EingabeFeld), 4)
                                                                                                                                            
Ueberpruefen([res1, res2, res3, res4, res5])
