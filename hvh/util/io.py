# coding=utf-8
from msvcrt import getch
import colorama

colorama.init()
# Input
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

def AuswahlHorizontal( Auswaehlbar, Nachricht, pos=[1, 1], clear=True ):
    """Auswahl aus einer Liste (mit Pfeiltasten)
    
    Auswählbar: List/Array/Tuple
    Nachricht:  String"""
    if (clear): print("\033[2J", end="")
    print(colorama.Fore.GREEN + Nachricht + colorama.Style.RESET_ALL)
    Laenge = len(Auswaehlbar)
    Position = 0
    Ausgewaehlt = None
    while ( Ausgewaehlt == None ):
        Ausgabe = '\033[' + str(pos[0] + 1) + ';' + str(pos[1]) + 'f'
        for i in range(Laenge):
            if (i == Position):
                Ausgabe += colorama.Back.WHITE + colorama.Fore.BLACK + Auswaehlbar[i] + colorama.Style.RESET_ALL + " "
            else:
                Ausgabe += Auswaehlbar[i] + " "
        print(Ausgabe)
        key = ord(getch())
        if (key == 224):
            key = ord(getch())
            if (key == 75):
                Position -= 1
            if (key == 77):
                Position += 1
        Position = (Position + Laenge) % Laenge
        if (key == 13):
            Ausgewaehlt = Auswaehlbar[Position]
    return Ausgewaehlt


# Output
def VisualisierungVertikal( Feld ):
    """Work in progress. Use with caution!"""
    for i in range(max(Feld), min(Feld) - 1, -1):
        horizontal = ' '
        for j in range(len(Feld)):
            if Feld[j] >= i:
                horizontal += '█'
            else:
                horizontal += ' '
        print(horizontal)

def VisualisierungHorizontal( Feld ):
    """Work in progress. Use with caution!"""
    for i in range(len(Feld)):
        horizontal = '■' * Feld[i]
        print(horizontal)

def VisualisierungFeld( Feld ):
    """Work in progress. Use with caution!"""
    print(colorama.Fore.BLUE + str(Feld) + colorama.Style.RESET_ALL)

class Table:
    """Eine einfache Tabelle"""

    def ZellenZuString(self, Zeile):
        return [str(Zelle) for Zelle in Zeile]

    def __init__(self, Spalten=[]):

        Spalten = self.ZellenZuString(Spalten)
        self.Zellen = [Spalten] if Spalten != [] else []
        self.RandStielVertikal = {0:"D", 1:"D"}
        self.RandStielHorizontal = {0:"D", 1:"D"}
        self.Form = {"NSNS":"─", "SNSN":"│", "NSSN":"┌", "NNSS":"┐", "SSNN":"└", "SNNS":"┘", "SSSN":"├", "SNSS":"┤", "NSSS":"┬", "SSNS":"┴", "SSSS":"┼",
                     "NDND":"═", "DNDN":"║",
                     "NDSN":"╒", "NSDN":"╓", "NDDN":"╔", "NNSD":"╕", "NNDS":"╖", "NNDD":"╗",
                     "SDNN":"╘", "DSNN":"╙", "DDNN":"╚", "SNND":"╛", "DNNS":"╜", "DNND":"╝",
                     "SDSN":"╞", "DSDN":"╟", "DDDN":"╠", "SNSD":"╡", "DNDS":"╢", "DNDD":"╣",
                     "NDSD":"╤", "NSDS":"╥", "NDDD":"╦", "SDND":"╧", "DSNS":"╨", "DDND":"╩",
                     "SDSD":"╪", "DSDS":"╫", "DDDD":"╬",
                     "NNNN":" ",
                     "SNNN":"│", "NNSN":"│", "DNNN":"║", "NNDN":"║", "NSNN":"─", "NNNS":"─", "NDNN":"═", "NNND":"═"}
        #─│┌┐└┘├┤┬┴┼ ═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬

    def ZeileHinzufügen(self, Zeile):
        Zeile = self.ZellenZuString(Zeile)
        self.Zellen.append(Zeile)

    def DefiniereForm(self, Form):
        self.Form = Form
        
    def BerechneTabellenGroeße(self):
        Breite = 0
        Hoehe = len(self.Zellen)
        for y in range(Hoehe):
            if len(self.Zellen[y]) > Breite: Breite = len(self.Zellen[y])
        return (Breite, Hoehe)

    def BerechneZellenLaenge(self, Rand):
        TabellenGroeße = self.BerechneTabellenGroeße()
        SpaltenLaenge = [0] * TabellenGroeße[0]
        for y in range(TabellenGroeße[1]):
            for x, Zelle in enumerate(self.Zellen[y]):
                if x <= len(self.Zellen[y]):
                    if len(self.Zellen[y][x]) > SpaltenLaenge[x]: SpaltenLaenge[x] = len(self.Zellen[y][x])
        return [(elem + 2 * Rand) for elem in SpaltenLaenge]

    def FuelleStiel(self, Stiel, Laenge):
        return [(Stiel[i] if i in Stiel else "S") for i in range(Laenge)]

    def BerechneRandFeld(self, Groeße):
        RStielH = self.FuelleStiel(self.RandStielHorizontal, Groeße[1] + 1)
        RStielV = self.FuelleStiel(self.RandStielVertikal, Groeße[0] + 1)
        Feld = [[(self.Form[
                            (RStielV[x//2] if x % 2 == 0 and y > 0 else "N") + # 
                            (RStielH[y//2] if y % 2 == 0 and x < Groeße[0] * 2 else "N") + # 
                            (RStielV[x//2] if x % 2 == 0 and y < Groeße[1] * 2 else "N") + # 
                            (RStielH[y//2] if y % 2 == 0 and x > 0 else "N")   # 
                        ]) for x in range(Groeße[0] * 2 + 1)] for y in range(Groeße[1] * 2 + 1)]
        return Feld

    def GibTabelleAus(self, Rand, flush=False, RandPrefix="", InhaltPrefix=""):
        TabellenGroeße = self.BerechneTabellenGroeße()
        SpaltenLaenge = self.BerechneZellenLaenge(Rand)
        RandFeld = self.BerechneRandFeld(TabellenGroeße)

        def GibRandAus(Zeile):
            Rueckgabe = RandPrefix
            for i in range(TabellenGroeße[0]):
                Rueckgabe += RandFeld[Zeile * 2][i * 2]
                Rueckgabe += RandFeld[Zeile * 2][i * 2 + 1] * SpaltenLaenge[i]
            Rueckgabe += RandFeld[Zeile * 2][-1]
            return Rueckgabe

        def GibTextAus(Zeile):
            Rueckgabe = ""
            for i in range(TabellenGroeße[0]):
                Rueckgabe += RandPrefix + RandFeld[Zeile * 2 + 1][i * 2]
                Rueckgabe += InhaltPrefix + (Rand * " " + (self.Zellen[Zeile][i] if i < len(self.Zellen[Zeile]) else "") + (" " * 100))[:SpaltenLaenge[i]]
            Rueckgabe += RandPrefix + RandFeld[Zeile * 2 + 1][-1]
            return Rueckgabe

        Ergebniss = ""

        for y in range(TabellenGroeße[1]):
            Ergebniss += GibRandAus(y) + "\n"
            Ergebniss += GibTextAus(y) + "\n"
        Ergebniss += GibRandAus(TabellenGroeße[1])

        print(Ergebniss, flush=flush)


# ╔═════════╦═════════╤═════════╗ ===>X     ═
# ║         ║         │         ║
# ╠═════════╬═════════╪═════════╣           ═
# ║         ║         │         ║
# ╟─────────╫─────────┼─────────╢           ─
# ║         ║         │         ║
# ╟─────────╫─────────┼─────────╢           ─
# ║         ║         │         ║
# ╟─────────╫─────────┼─────────╢           ─
# ║         ║         │         ║
# ╟─────────╫─────────┼─────────╢           ─
# ║         ║         │         ║
# ╚═════════╩═════════╧═════════╝           ─
# ║                                         ^ BorderVertikalStyle
# ║
# \/

# ▀▄█▌▐░▒▓■□▬ ▌▐

def progressHorizontal(value, width, pos, text="", flush=False, ProgressPrefix="", TextPrefix=""):
    print('\033[' + str(pos[0]) + ';' + str(pos[1]) + 'f' + ProgressPrefix + (int( value) * "█") + (int(width - value) * "░") + TextPrefix + " " + text)


