# coding=utf-8
#if not using colorama comment out the next two lines
import colorama
colorama.init()
import importdy
import dynalist

def Suche_Einfuegestelle(neu):
    Vergleichsinhalt = importdy.listeninfotyp()
    Abbruch = False
    Skiliste.Beginne_am_Listenanfang
    if not Skiliste.Liste_leer():
        Vergleichsinhalt = Skiliste.Lies_Listenelement()
        Abbruch = Skiliste.Liste_zuende() or Vergleichsinhalt.zeit > neu.zeit
        while not Abbruch:
            Skiliste.Ruecke_in_der_Liste_vor()
            if not Skiliste.Liste_zuende():
                Vergleichsinhalt = Skiliste.Lies_Listenelement()
                Abbruch = Skiliste.Liste_zuende() or Vergleichsinhalt.zeit > neu.zeit

def Einen_Skifahrer_hinzufuegen():
    Skifahrer = importdy.listeninfotyp()
    Skifahrer.name = input("Name des Skifahrers: ")
    Skifahrer.zeit = input("Gelaufene Zeit :     ")
    Suche_Einfuegestelle(Skifahrer)
    Skiliste.Fuege_Listenelement_ein(Skifahrer)

def Einen_Skifahrer_streichen():

    def Suche(Inhalt):
        Abbruch = False

        Skiliste.Beginne_am_Listenanfang()
        Gefunden = False
        stelle = 0
        if not Skiliste.Liste_leer():
            VergleichsInhalt = Skiliste.Lies_Listenelement()
            stelle += 1
            Gefunden = VergleichsInhalt.name  = Inhalt.name
            Abbruch = Gefunden or Skiliste.Liste_zuende()
            while not Abbruch:
                Skiliste.Ruecke_in_der_Liste_vor()
                stelle += 1
                if not Skiliste.Liste_zuende():
                    Gefunden = VergleichsInhalt.name  = Inhalt.name
                    Abbruch = Gefunden or Skiliste.Liste_zuende()
        return stelle if Gefunden else None

    Skifahrer = importdy.listeninfotyp()
    Skifahrer.name = input("Name des Skifahrers: ")
    Skifahrer.zeit = input("Gelaufene Zeit :     ")
    stelle = Suche(Skifahrer)
    Skiliste.Beginne_am_Listenanfang()
    if (stelle != None):
        for i in range(stelle - 1):
            Skiliste.Ruecke_in_der_Liste_vor()
    Skiliste.Loesche_Listenelement()

def Ski_Bestenliste_ausgeben():
   print()
   Skiliste.Beginne_am_Listenanfang()
   while not Skiliste.Liste_zuende():
        Skifahrer = Skiliste.Lies_Listenelement()
        print(Skifahrer.name + ": " + str(Skifahrer.zeit))
        Skiliste.Ruecke_in_der_Liste_vor()
   print()
   input('Weiter mit RETURN')

Skiliste = dynalist.Listentyp()
while True:
    Antwort = ""
    while True:
        print('\033[2J\033[1;1f', end='')
        print('A : Einen Skifahrer hinzufgen')
        print('B : Einen Skifahrer streichen')
        print('C : Ski-Bestenliste ausgeben')
        print('D : Ende')
        print('E : Liste laden')
        print('F : Liste speicher')
        print
        Antwort = input('Ihre Wahl: ')[:1].lower()
        if (Antwort in set(map(chr, range(ord('a'), ord('f') + 1)))): break
    if Antwort == 'a': Einen_Skifahrer_hinzufuegen()
    if Antwort == 'b': Einen_Skifahrer_streichen()
    if Antwort == 'c': Ski_Bestenliste_ausgeben()
    if Antwort == 'd': break
    if Antwort == 'e': Skiliste = Skiliste.Lade_Liste("Ski.p")
    if Antwort == 'f': Skiliste.Sichere_Liste("Ski.p")