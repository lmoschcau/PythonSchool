# -*- coding: utf-8 -*-

import sys, os
import pickle

class Persontyp:
    def __init__( self ):
        self.Name = raw_input("Name: ")
        self.Strasse = raw_input("Straße und Hausnummer: ")
        self.Wohnort = raw_input("PLZ und Wohnort: ")
        self.Telefon = raw_input("Telefonnummer: ")
        
class Datei:
    def __init__( self, filename ):
        self.getFilename = filename
        try:
            self.Personen = pickle.load(open(filename, "rb")).Personen
        except IOError:
            print "Dateifehler"

    def close( self ):
        pickle.dump(self, open(self.getFilename, "w+"))

    def person_anmelden(self):
        Person = Persontyp()
        self.Personen.append(Person)

    def person_abmelden( self ):
        Name = raw_input("Name der abzumeldenden Person: ")
        for i in range(0, len(self.Personen) - 1):
            if (self.Personen[i].Name == Name):
                del self.Personen[i]

    def liste_sortieren( self ):
        def vertausche( Feld, i, j ):
            Feld[i], Feld[j] = Feld[j], Feld[i]
            return Feld

        def BubbleSort( Feld ):
            for grenze in range(len(Feld) - 1):
                for i in range(len(Feld) - 1, grenze, -1):
                    if ( Feld[i - 1].Name > Feld[i].Name ):
                        vertausche(Feld, i, i - 1)
            return Feld

        return BubbleSort(self.Personen)

    def einen_datensatz_ausgeben( self, Person ):
        print "{:21s}   {:21s}  {:21s}  {:21s}".format(Person.Name, Person.Strasse, Person.Wohnort, Person.Telefon)

    def liste_ausgeben( self ):
        print "{:21s}   {:21s}  {:21s}  {:21s}".format("Name", "Straße und Hausnummer", "PLZ und Wohnort", "Telefonnummer")
        for Person in self.Personen:
            self.einen_datensatz_ausgeben(Person)

    def teilnehmerdatei_erstellen( self, dateiname ):
        imax = int(raw_input("Wie viele Personen maximal?: "))
        ausgabe = []
        for i in range(min(imax, len(self.Personen))):
            ausgabe.append(self.Personen[i])
        pickle.dump(ausgabe, open(dateiname, "w+"))

    def teilnehmerdatei_sortiert_erstellen( self, dateiname ):
        imax = int(raw_input("Wie viele Personen maximal?: "))
        personen = self.liste_sortieren()
        ausgabe = []
        for i in range(min(imax, len(personen))):
            ausgabe.append(personen[i])
        pickle.dump(ausgabe, open(dateiname, "w+"))

    def teilnehmerliste_ausgeben( self, dateiname ):
        datei = pickle.load(open(dateiname, "rb"))
        print "{:21s}   {:21s}  {:21s}  {:21s}".format("Name", "Straße und Hausnummer", "PLZ und Wohnort", "Telefonnummer")
        for i in datei:
            self.einen_datensatz_ausgeben(i)

    def person_anmelden_und_einfuegen( self ):
        self.person_anmelden()
        self.Personen = self.liste_sortieren()

    def bescheide_ausgeben( self ):
        imax = int(raw_input("Wie viele Personen maximal?: "))
        for i in range(len(self.Personen)):
            if i < imax:
                zusage = "Ja"
            else:
                zusage = "Nein"
            sys.stdout.write("{:4s}: ".format(zusage))
            self.einen_datensatz_ausgeben(self.Personen[i])

def weiter():
    raw_input('Drücken Sie die <Return>-Taste')


# Hauptprogramm

ANMELDEDATEINAME = "anmelde.p"
TEILNEHMERDATEINAME = "teilnehmer.p"

Anmeldedatei = Datei(ANMELDEDATEINAME)
Antwort = 0

while Antwort != 9:
    os.system('clear')
    print 'Eine Person anmelden:               1'
    print 'Eine Person abmelden:               2'
    print 'Die Anmeldeliste ausgeben:          3'
    print 'Bescheide erstellen (1):            4'
    print 'Die Teilnehmerdatei erstellen (2):  5'
    print 'Eine Person sortiert anmelden (3):  6'
    print 'Teilnahmerdatei sortiert (8.1.4):   7'
    print 'Die Teilnehmerdatei ausgeben:       8'
    print 'Die Arbeit beenden:                 9'

    Antwort = int(raw_input('Ihre Wahl: '))

    if Antwort == 1:
        os.system('clear')
        Anmeldedatei.person_anmelden()

    elif Antwort == 2:
        os.system('clear')
        Anmeldedatei.person_abmelden()
    
    elif Antwort == 3:
        os.system('clear')
        Anmeldedatei.liste_ausgeben()
        weiter()

    elif Antwort == 4:
        os.system('clear')
        Anmeldedatei.bescheide_ausgeben()
        weiter()
    
    elif Antwort == 5:
        os.system('clear')
        Anmeldedatei.teilnehmerdatei_erstellen(TEILNEHMERDATEINAME)
        weiter()
    
    elif Antwort == 6:
        os.system('clear')
        Anmeldedatei.person_anmelden_und_einfuegen()
    
    elif Antwort == 7:
        os.system('clear')
        Anmeldedatei.teilnehmerdatei_sortiert_erstellen(TEILNEHMERDATEINAME)
        weiter()
    
    elif Antwort == 8:
        os.system('clear')
        Anmeldedatei.teilnehmerliste_ausgeben(TEILNEHMERDATEINAME)
        weiter()
        