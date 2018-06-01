# -*- coding: utf-8 -*-

class HashTabelle:
    FREI = 0
    BESETZT = 1
    GELOESCHT = 2

    def __init__( self, max, method, key ):
        self.SPEICHERGROESSE = max
        self.METHOD = method
        self.KEY = key
        self.Tabelle = []
        for _ in  range(0, self.SPEICHERGROESSE):
            self.Tabelle.append({"Schluessel": "", "Status": self.FREI})
        
    def hash( self, schluessel ):
        if (self.METHOD == 0) or (self.METHOD == 3):
            return (ord(schluessel[0]) - ord("A")) % self.SPEICHERGROESSE
        
        elif self.METHOD == 1:
            helper = 0
            for buchstabe in schluessel:
                if (ord(buchstabe) >= ord("A")) and (ord(buchstabe) <= ord("z")):
                    break
                helper += ord(buchstabe)
            return helper % self.SPEICHERGROESSE

        elif self.METHOD == 2:
            helper = 0
            increment = iter(range(len(schluessel)))
            for i in increment:
                buchstabe = schluessel[i]
                if (ord(buchstabe) >= ord("A")) and (ord(buchstabe) <= ord("z")):
                    break
                helper += ord(buchstabe)
                next(increment, None)
            return helper % self.SPEICHERGROESSE

    def rehash( self, adresse ):
        if 0 <= self.METHOD <= 2:
            return (adresse + 1) % self.SPEICHERGROESSE
        
        elif self.METHOD == 3:
            return (adresse + ord(self.KEY[1]) - ord(self.KEY[0])) % self.SPEICHERGROESSE

    def finde( self, schluessel ):
        adresse = self.hash(schluessel)
        i = 0
        while (self.Tabelle[adresse]["Schluessel"] != schluessel) and (self.Tabelle[adresse]["Status"] != self.FREI) and i <self.SPEICHERGROESSE:
            adresse = self.rehash(adresse)
            i += 1
        if (self.Tabelle[adresse]["Schluessel"] == schluessel) and (self.Tabelle[adresse]["Status"] == self.BESETZT):
            return adresse
        else:
            return -1

    def fuegeein( self, schluessel ):
        if self.finde(schluessel) < 0:
            adresse = self.hash(schluessel)
            while self.Tabelle[adresse]["Status"] == self.BESETZT:
                adresse = self.rehash(adresse)
            self.Tabelle[adresse]["Schluessel"] = schluessel
            self.Tabelle[adresse]["Status"] = self.BESETZT

    def loesche( self, schluessel ):
        adresse = self.finde(schluessel)
        if adresse >= 0:
            self.Tabelle[adresse]["Status"] = self.GELOESCHT

    def leer( self ):
        for eintrag in self.Tabelle:
            if eintrag["Status"] == self.BESETZT:
                break
        return eintrag["Status"] != self.BESETZT
        
    def voll( self ):
        freie = 0
        for eintrag in self.Tabelle:
            if eintrag["Status"] != self.BESETZT:
                freie += 1
                if freie > 2:
                    break
        return freie < 2

Tabelle = HashTabelle(20, 3, "ftz")

Tabelle.fuegeein("Nundhjtjtktktkah")
Tabelle.fuegeein("Nundhjtjtktkrj")
Tabelle.fuegeein("Fjj")
print Tabelle.Tabelle