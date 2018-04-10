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
    for i in range(max(Feld), min(Feld) - 1, -1):
        horizontal = ' '
        for j in range(len(Feld)):
            if Feld[j] >= i:
                horizontal += '█'
            else:
                horizontal += ' '
        print(horizontal)

def VisualisierungHorizontal( Feld ):
    for i in range(len(Feld)):
        horizontal = '■' * Feld[i]
        print(horizontal)

def VisualisierungFeld( Feld ):
    print(colorama.Fore.BLUE + str(Feld) + colorama.Style.RESET_ALL)

class Table:
    """Eine einfache Tabelle"""
    def __init__(self, Spalten):
        self.Spalten = Spalten
        self.Zeilen = []
        self.Zellen = []

        self.Form = {"┌":"┌", "─":"─", "┬":"┬", "┐":"┐", "│":"│", "├":"├", "┼":"┼", "┤":"┤", "└":"└", "┴":"┴", "┘":"┘"}

    def ZeileHinzufügen(self, ZeileName, ZeileInhalt):
        self.Zeilen.append(ZeileName)
        self.Zellen.append(ZeileInhalt)

    def DefiniereForm(self, Form):
        self.Form = Form
        #─│┌┐└┘├┤┬┴┼═║╒╓╔╕╖╗╘╙╚╛╜╝╞╟╠╡╢╣╤╥╦╧╨╩╪╫╬
        #─│┌┐└┘├┤┬┴┼
        #┌─┬┐
        #├─┼┤
        #└─┴┘