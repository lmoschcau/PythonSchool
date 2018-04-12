# coding=utf-8
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
    def __init__(self, Spalten=[]):

        self.Zellen = [Spalten] if Spalten != [] else []
        self.VertikalRandStiel = "0:D;1:D;"
        self.HorizontalRandStiel = "0:D;1:D;"

        self.Form = {"NSNS":"─", "SNSN":"│", "NSSN":"┌", "NNSS":"┐", "SSNN":"└", "SNNS":"┘", "SSSN":"├", "SNSS":"┤", "NSSS":"┬", "SSNS":"┴", "SSSS":"┼",
                     "NDND":"═", "DNDN":"║",
                     "NDSN":"╒", "NSDN":"╓", "NDDN":"╔", "NNSD":"╕", "NNDS":"╖", "NNDD":"╗",
                     "SDNN":"╘", "DSNN":"╙", "DDNN":"╚", "SNND":"╛", "DNNS":"╜", "DNND":"╝",
                     "SDSN":"╞", "DSDN":"╟", "DDDN":"╠", "SNSD":"╡", "DNDS":"╢", "DNDD":"╣",
                     "NDSD":"╤", "NSDS":"╥", "NDDD":"╦", "SDND":"╧", "DSNS":"╨", "DDND":"╩",
                     "SDSD":"╪", "DSDS":"╫", "DDDD":"╬"}
        #─│┌┐└┘├┤┬┴┼ ═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬

    def ZeileHinzufügen(self, Zeile):
        self.Zellen.append(Zeile)

    def DefiniereForm(self, Form):
        self.Form = Form

    def Get_VertikalRandStiel(self):
        return self.VertikalRandStiel

    def Set_VertikalRandStiel(self, value):
        self.VertikalRandStiel = value

    VertikalRandStiel = property(Get_VertikalRandStiel, SSet_VertikalRandStiel)

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
                if x <= len(self.Zellen):
                    if len(self.Zellen[y][x]) > SpaltenLaenge[x]: SpaltenLaenge[x] = len(self.Zellen[x][y])

        return {"Spalten":[(elem + 2 * Rand) for elem in SpaltenLaenge]}

    def GebeTabelleAus(Außenrand="D", ErsteSpalteTrenner="D", ErsteZeileTrenner="D", SpalteTrenner="S", ZeileTrenner="S"):
        pass


# ╔═════════╦═════════╤═════════╗ ===>X
# ║         ║         │         ║
# ╠═════════╬═════════╪═════════╣
# ║         ║         │         ║
# ╟─────────╫─────────┼─────────╢
# ║         ║         │         ║
# ╟─────────╫─────────┼─────────╢
# ║         ║         │         ║
# ╟─────────╫─────────┼─────────╢
# ║         ║         │         ║
# ╟─────────╫─────────┼─────────╢
# ║         ║         │         ║
# ╚═════════╩═════════╧═════════╝
# ║
# ║
# \/
