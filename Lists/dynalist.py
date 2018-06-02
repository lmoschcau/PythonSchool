# -*- coding: utf-8 -*-

import sys, os
import pickle

class Listentyp:
    class Listenknotentyp:
        def __init__(self):
            self.Inhalt = None
            self.Nachfolgezeiger = None
#        def __init__(self, Inhalt):
#            self.Inhalt = Inhalt
#            self.Nachfolgezeiger = None

    def __init__(self):
        self.Kopfzeiger = self.Listenknotentyp()
        self.Aktuellzeiger = self.Kopfzeiger

    def Liste_leer(self):
        return self.Kopfzeiger.Nachfolgezeiger == None

    def Liste_zuende(self):
        return self.Aktuellzeiger.Nachfolgezeiger == None

    def Beginne_am_Listenanfang(self):
        self.Aktuellzeiger = self.Kopfzeiger

    def Ruecke_in_der_Liste_vor(self):
        if not self.Liste_zuende():
            self.Aktuellzeiger = self.Aktuellzeiger.Nachfolgezeiger

    def Lies_Listenelement(self):
        if not self.Liste_zuende():
            return self.Aktuellzeiger.Nachfolgezeiger.Inhalt
    
    def Fuege_Listenelement_ein(self, Inhalt):
        Neuzeiger = self.Listenknotentyp()
        Neuzeiger.Inhalt = Inhalt
        Neuzeiger.Nachfolgezeiger = self.Aktuellzeiger.Nachfolgezeiger
        self.Aktuellzeiger.Nachfolgezeiger = Neuzeiger

    def Loesche_Listenelement(self):
        if not self.Liste_zuende():
            self.Aktuellzeiger.Nachfolgezeiger = self.Aktuellzeiger.Nachfolgezeiger.Nachfolgezeiger

    def Listenknotenzahl(self):
        self.Beginne_am_Listenanfang()
        zaehler = 0
        while not self.Liste_zuende():
            zaehler += 1
            self.Ruecke_in_der_Liste_vor()
        return zaehler

    def Entferne_Liste(self):
        self.Beginne_am_Listenanfang()
        while not self.Liste_zuende():
            self.Loesche_Listenelement()
    
    def Sichere_Liste(self, Dateiname):
        pickle.dump(self, open(Dateiname, 'wb'))
    
    def Lade_Liste(self, Dateiname):
        return pickle.load(open(Dateiname, "rb"))