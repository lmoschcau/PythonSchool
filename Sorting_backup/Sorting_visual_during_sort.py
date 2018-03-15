# coding=utf-8
# THIS VERSION IS VISUALIZING EVERY STEP.
# ███ USE WITH CAUTION !!! ███ 
import sys
import random
import datetime
import time
from time import sleep

#if not using colorama comment out the next two lines
import colorama
colorama.init()

# Initialisierung von Variablen:
AnzahlAufrufe = 0
AnzahlSchreiben = 0

SpaltenBreite = 16

Zeiten = [None] * 4
Aufrufe = [None] * 4
Schreiben = [None] * 4
Funktionen = [None] * 4

Beenden = False

maximumFeld = 0
maximumFaktor = 0.01
# Sortier-Algorithmen:
def vertausche( Feld, i, j ):
    Feld[i], Feld[j] = Feld[j], Feld[i]
    return Feld

def AuswahlSort( Feld ):
    global AnzahlAufrufe
    global AnzahlSchreiben
    for grenze in range(len(Feld)):
        kleinstes = grenze
        for i in range(grenze, len(Feld)):
            AnzahlAufrufe += 1                                  #Zähler
            if Feld[i] < Feld[kleinstes]:
                kleinstes = i
                AnzahlSchreiben += 1                                 #Zähler
                Visualisierung(Feld, grenze, position = i)
        Feld = vertausche(Feld, grenze, kleinstes)
    return Feld

def EinSort( Feld ):
    def FuegeEin( Feld, i ):
        global AnzahlAufrufe
        global AnzahlSchreiben
        Inhalt = Feld[i]
        while ( ( i > 0 ) & ( Feld[i - 1] > Inhalt ) ):
            Feld[i] = Feld[i - 1]
            i -= 1
            AnzahlAufrufe += 1                                     #Zähler
            Visualisierung(Feld, grenze, position = i)
        Feld[i] = Inhalt
        AnzahlSchreiben += 1                                      #Zähler
        return Feld
    for grenze in range(1, len(Feld)):
        Feld = FuegeEin(Feld, grenze)
    return Feld

def BubbleSort( Feld ):
    global AnzahlAufrufe
    global AnzahlSchreiben
    for grenze in range(len(Feld) - 1):
        for i in range(len(Feld) - 1, grenze, -1):
            AnzahlAufrufe += 1                                  #Zähler
            if ( Feld[i - 1] > Feld[i] ):
                vertausche(Feld, i, i - 1)
                AnzahlSchreiben += 1                                 #Zähler
                Visualisierung(Feld, grenze, position = i)
    return Feld

def BubbleSort2( Feld ):
    global AnzahlAufrufe
    global AnzahlSchreiben
    grenze = 0
    while ( grenze < len(Feld) ):
        merke = len(Feld)
        for i in range(len(Feld) - 1, grenze, -1):
            AnzahlAufrufe += 1                                  #Zähler
            if ( Feld[i - 1] > Feld[i] ):
                vertausche(Feld, i, i - 1)
                merke = i
                AnzahlSchreiben += 1                                 #Zähler
                Visualisierung(Feld, grenze, position = i)
        grenze = merke
    return Feld

# Zufall + arrayLänge
# InformationsAusgabe ( Zeit, #Aufrufe)
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
def FuelleZufall( ArrayLaenge, ZufallMin, ZufallMax ):
    Feld = []
    for i in range(ArrayLaenge):
        Feld.append(random.randint(ZufallMin, ZufallMax))
    return Feld
# Funktion für die Eingabe der Werte eines Zufälligen Feldes.
# Eingabe von: Anzahl der Einträge, niedrigster und höchster Wert.
def InitialisierungFeld( ):
    Fehler = "Bitte Geben Sie eine ganze natürliche Zahl an."
    EingabeFeld = None

    while ( EingabeFeld == None ):
        ArrayLaenge = Eingabe("Bitte die Länge des Feldes angeben (kleiner als das für Schritt-für-Schritt Visualisierung errechnete Maximum " + str(maximumFeld) + ":", int, Fehler)
        if (ArrayLaenge < maximumFeld):
            ZufallMin = Eingabe("Bitte den niedrigsten Wert angeben:", int, Fehler)
            ZufallMax = Eingabe("Bitte den höchsten Wert angeben:", int, Fehler)
            try:
                EingabeFeld = FuelleZufall(ArrayLaenge, ZufallMin, ZufallMax)
            except ValueError:
                print("\033[2J\033[1;1f" + colorama.Fore.RED + "Fehler: niedrigster Wert (" + str(ZufallMin) + ") ist größer als der höchste Wert (" + str(ZufallMax) + ")!" + colorama.Style.RESET_ALL)
        else:
            print("\033[2J\033[1;1f" + colorama.Fore.RED + "Fehler: Die Länge des Feldes (" + str(ArrayLaenge) + ") ist größer als das für Schritt-für-Schritt Visualisierung errechnete Maximum (" + str(maximumFeld) + ")!" + colorama.Style.RESET_ALL)
    return EingabeFeld
#███ Funktionen für die Visualisierung von Feldern.
# Wenn eine weitere Funktionen ergänzt wird muss sie bei der Eingabe der
# visualisierung ergänzt werden.
def TesteGeschwindigkleit():
    global maximumFeld
    print( colorama.Fore.RED + "Teste Geschwindikeit des Computers. Bitte warten" + colorama.Style.RESET_ALL)
    start = time.time()
    for i in range(10000):
        print( colorama.Fore.RED + ".", end="")
    millis = int(round((time.time() - start) * 1000))
    print("Der Computer hat " + str(millis) + "ms gebraucht.")
    maximumFeld = int(maximumFaktor * millis) + 1
    sleep(2)
    print('\033[2J\033[1;1f', end='')

def VisualisierungVertikal( Feld, Grenze, **kwargs ):
    print('\033[2J\033[1;1f', end='')
    for i in range(max(Feld), min(Feld) - 1, -1):
        horizontal = ' '
        for j in range(len(Feld)):
            if Feld[j] >= i:
                if (j < Grenze):
                    horizontal += colorama.Fore.GREEN
                else:
                    horizontal += colorama.Fore.RED
                horizontal += '█'
            else:
                horizontal += ' '
        print(horizontal, flush=True)
    if (kwargs.get('position', None)):
        print((" " * kwargs.get('position', None)) + colorama.Fore.WHITE + "^")
    sleep(0.08) # Time in seconds.

def VisualisierungHorizontal( Feld, Grenze, **kwargs ):
    print('\033[2J\033[1;1f', end='')
    for i in range(len(Feld)):
        if (kwargs.get('position', None) == i):
            horizontal = colorama.Fore.WHITE + "›"
        else:
            horizontal = " "
        if (i < Grenze):
            horizontal += colorama.Fore.GREEN
        else:
            horizontal += colorama.Fore.RED
        horizontal += '■' * Feld[i]
        print(horizontal, flush=True)
    sleep(0.08) # Time in seconds.

def VisualisierungFeld( Feld, Grenze, **kwargs ):
    print('\033[2J\033[1;1f', end='')
    print(colorama.Fore.BLUE + str(EingabeFeld) + colorama.Style.RESET_ALL)
    
#███ Ausgabe
# Funktion für die Ausgabe einer Zeile einer Tabelle
def GebeTabellenZeileAus( Name, Feld ):
    AusgabeZeile = ( str(Name) + "                                  " )[:SpaltenBreite]
    for i in range(len(Feld)):
        AusgabeZelle = str(Feld[i]) + "                                  "
        AusgabeZeile += AusgabeZelle[:SpaltenBreite]
    print(AusgabeZeile)

#███ Funktionen für Aufruf und Überprüfung
# Funktion für das aufrufen von einem Sortieralgorithmus.
# Setzt die Werte für die Statistik in einem Feld auf die Werte des aktuellen
# Algorithmus.
def RufeAuf( Algorithmus, AufrufFeld, i ):
    global AnzahlAufrufe
    global AnzahlSchreiben
    AnzahlAufrufe = 0
    AnzahlSchreiben = 0
    StartZeit = datetime.datetime.now()
    sortiertesFeld = Algorithmus(AufrufFeld)
    Zeiten[i] = datetime.datetime.now() - StartZeit
    Aufrufe[i] = AnzahlAufrufe
    Schreiben[i] = AnzahlSchreiben
    Funktionen[i] = Algorithmus.__name__
    Visualisierung( sortiertesFeld, len(sortiertesFeld) )
    print('\n')
    print("AnzahlAufrufe: " + str(AnzahlAufrufe) + " AnzahlSchreiben: " + str(AnzahlSchreiben) + " Zeit: " + str(Zeiten[i]))
    # weitergabe des sortierten Feldes für Weiterverarbeitung / Informationen
    return sortiertesFeld

# Funktion für das Überprüfen der Richtigkeit der Felder inerhalb eines Feldes
# Schema: FeldFeld[Feld, Feld, Feld, Feld]
def Ueberpruefen( FeldFeld ):

    def HinzufuegenWennNichtLetztes(Text, Index, Laenge):
        if (Index != Laenge - 1):
            return Text
        return ""

    FeldFehler = False
    AusgabeString = colorama.Fore.BLUE + "["
    for i in range(len(FeldFeld[0])):
        gleich = True
        for j in range(0, len(FeldFeld)):
            if (( FeldFeld[j][i] != FeldFeld[0][i] ) | (FeldFeld[j][max(i - 1, 0)] > FeldFeld[j][i])):
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
TesteGeschwindigkleit();
while (Beenden == False):
    print('\033[2J\033[1;1f', end='')
    EingabeFeld = InitialisierungFeld()
    Visualisierung = Auswahl({"v":VisualisierungVertikal, "h":VisualisierungHorizontal, "f":VisualisierungFeld}, "Visualisierung bitte auswählen: Vertikal[V] Horizontal[H] Feld[F]")
    print(colorama.Fore.BLUE + '\033[2J\033[1;1funsortiertes Feld:\n' + colorama.Fore.CYAN)
    Visualisierung(list(EingabeFeld), 0)

    print(colorama.Fore.BLUE + '\nsortiertes Feld (Auswahl):' + colorama.Fore.CYAN)
    res1 = RufeAuf(AuswahlSort, list(EingabeFeld), 0)
    print(colorama.Fore.BLUE + '\nsortiertes Feld (Einfügen):' + colorama.Fore.CYAN)
    res2 = RufeAuf(EinSort, list(EingabeFeld), 1)
    print(colorama.Fore.BLUE + '\nsortiertes Feld (Bubble-Sort):' + colorama.Fore.CYAN)
    res3 = RufeAuf(BubbleSort, list(EingabeFeld), 2)
    print(colorama.Fore.BLUE + '\nsortiertes Feld (Bubble+):' + colorama.Fore.CYAN)
    res4 = RufeAuf(BubbleSort2, list(EingabeFeld), 3)
                                                                                                                                            
    Ueberpruefen([res1, res2, res3, res4])

    print('\nStatistiken:\n')
    print(colorama.Fore.LIGHTGREEN_EX + colorama.Back.LIGHTBLACK_EX + "Das Sortieren von einem Feld mit " + str(len(res1)) + " Einträgen war erfolgreich." + colorama.Fore.GREEN + colorama.Back.RESET)

    GebeTabellenZeileAus("Algorithmus", Funktionen)
    GebeTabellenZeileAus("Aufrufe", Aufrufe)
    GebeTabellenZeileAus("Schreiben", Schreiben)
    GebeTabellenZeileAus("Zeiten", Zeiten)

    Beenden = Auswahl({"j":True, "n":False, "t":True, "f":False, "1":True, "0":False}, "Wollen sie das Programm beenden? Ja[J] Nein[N]")