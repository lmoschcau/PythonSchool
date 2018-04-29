# types
TOrt = set([-1, 0, 1, 2, 3, 4, 5])

class StreckeSimpel:
    def __init__( self, distanz, geschwindigkeit=30 ):
        """Stellt die Strecke in eine Richtung in der Adjazemsmatrix dar.
        
        distanz:            int(in km)
        geschwindigkeit     int(in km/h; standard=30)"""
        self.dist = distanz
        self.geschw = geschwindigkeit

    def getMinZeit(self):
        return self.dist / self.geschw

    def __str__(self):
        return str(self.dist)

class StreckeWeg(StreckeSimpel):
    def __init__( self, von=None, nach=None, dist=None, geschw=None ):
        self.von = von
        self.nach = nach
        self.dist = dist
        self.geschw = geschw

class Weg:
    def __init__(self):
        self.strecken = [StreckeWeg() for i in range(12)]
        self.distanz = None
        self.index = -1
            
# BackTrackSimple

class BackTrackSimple:
    def __init__(self):
        self.cMaxIndex = 5
        self.cStartort = 0
        self.cZielort = 3
        self.aWeg = Weg()
        self.kWeg = Weg()
        self.aWeg.index = -1
        self.kWeg.index = 0
        self.aWeg.distanz = 0
        self.kWeg.distanz = 100000
        self.Karte = [[(None) for i in TOrt] for j in TOrt]
        self.erfolgreich = False

    def Succ(original):
        return original + 1

    def FuegeStreckeHinzu(self, von, nach, distanz, geschwindigkeit=30):
        self.Karte[von][nach] = StreckeSimpel(distanz, geschwindigkeit=geschwindigkeit)

    def FuegeStreckenHinzu(self, Strecken):
        for iStrecke in Strecken:
            self.FuegeStreckeHinzu(iStrecke[0], iStrecke[1], iStrecke[2], iStrecke[3] if len(iStrecke) == 4 else 30)

    def Track(self, von, nach):
            self.cStartort = von
            self.cZielort = nach
            self.Reise(self.cStartort)
            return self.kWeg
            
    def InitialisiereAuswahl(self):
        nach = -1

    def NaechsterKandidat(self, nach):
        return (nach + 1)

    def Annehmbar(self, von, nach):
        def Gefahren(von, nach):
            if (self.aWeg.index == -1):
                return False
            else:
                i = 0
                while not (((self.aWeg.strecken[i].von == von) and (self.aWeg.strecken[i].nach == nach)) or (i == self.aWeg.index)):
                    i  = i + 1
                return (self.aWeg.strecken[i].von == von) and ( self.aWeg.strecken[i].nach == nach)
        return (self.Karte[von][nach] != None ) and ( not Gefahren(von, nach))
  
    def ZeichneSchrittAuf(self, von, nach):
        self.aWeg.index = self.aWeg.index + 1
        self.aWeg.strecken[self.aWeg.index].von = von
        self.aWeg.strecken[self.aWeg.index].nach = nach
        self.aWeg.strecken[self.aWeg.index].dist = self.Karte[von][nach].dist
        self.aWeg.distanz = self.aWeg.distanz + self.Karte[von][nach].dist
        self.erfolgreich = nach == self.cZielort

    def LoescheSchritt(self, von, nach):
       self.aWeg.index = self.aWeg.index - 1
       self.aWeg.distanz = self.aWeg.distanz - self.Karte[von][nach].dist

    def KeinKandidatMehr(self, nach):
       return nach == self.cMaxIndex

    def Reise(self, von):
        nach = -1
        self.InitialisiereAuswahl()
        while True:
            nach = self.NaechsterKandidat(nach)
            if self.Annehmbar(von, nach):
                self.ZeichneSchrittAuf(von, nach)
                if not self.erfolgreich:
                    self.Reise(nach)
                    if not self.erfolgreich:
                        self.LoescheSchritt(von, nach)
            if (self.erfolgreich or self.KeinKandidatMehr(nach)): break
        self.kWeg.distanz = self.aWeg.distanz
        self.kWeg.strecken = [StreckeWeg(von=self.aWeg.strecken[i].von, nach=self.aWeg.strecken[i].nach, dist=self.aWeg.strecken[i].dist) for i in range(self.aWeg.index + 1)]
        self.kWeg.index = self.aWeg.index

# BackTrackBester

class BackTrackBester(BackTrackSimple):
  
    def ZeichneSchrittAuf(self, von, nach):
        self.aWeg.index = self.aWeg.index + 1
        self.aWeg.strecken[self.aWeg.index].von = von
        self.aWeg.strecken[self.aWeg.index].nach = nach
        self.aWeg.strecken[self.aWeg.index].dist = self.Karte[von][nach].dist
        self.aWeg.distanz = self.aWeg.distanz + self.Karte[von][nach].dist
        self.erfolgreich = nach == self.cZielort
        if (self.erfolgreich):
            if self.aWeg.distanz < self.kWeg.distanz:
                self.kWeg.distanz = self.aWeg.distanz
                self.kWeg.strecken = [StreckeWeg(von=self.aWeg.strecken[i].von, nach=self.aWeg.strecken[i].nach, dist=self.aWeg.strecken[i].dist) for i in range(self.aWeg.index + 1)]
                self.kWeg.index = self.aWeg.index

    def Reise(self, von):
        nach = -1
        self.InitialisiereAuswahl()
        while True:
            nach = self.NaechsterKandidat(nach)
            if self.Annehmbar(von, nach):
                self.ZeichneSchrittAuf(von, nach)
                self.Reise(nach)
                self.LoescheSchritt(von, nach)
            if self.KeinKandidatMehr(nach): break

class BackTrackBesucht(BackTrackBester):

    def Track(self, von, nach, zuBesuchendeOrte=set(TOrt)):
            self.cStartort = von
            self.cZielort = nach
            self.zuBesuchendeOrte = zuBesuchendeOrte
            self.Reise(self.cStartort)
            return self.kWeg
            
    def AlleBesucht(self):
           Orte  = set(self.zuBesuchendeOrte)
           Orte.add(-1)
           for ZaehlerStr in range(self.aWeg.index + 1):
                Orte.discard(self.aWeg.strecken[ZaehlerStr].von)
                Orte.discard(self.aWeg.strecken[ZaehlerStr].nach)
           if (Orte == {-1}):
               return True
           else:
               return False
  
    def ZeichneSchrittAuf(self, von, nach):
        self.aWeg.index = self.aWeg.index + 1
        self.aWeg.strecken[self.aWeg.index].von = von
        self.aWeg.strecken[self.aWeg.index].nach = nach
        self.aWeg.strecken[self.aWeg.index].dist = self.Karte[von][nach].dist
        self.aWeg.distanz = self.aWeg.distanz + self.Karte[von][nach].dist
        self.erfolgreich = nach == self.cZielort
        if (self.erfolgreich and self.AlleBesucht()):
            if self.aWeg.distanz < self.kWeg.distanz:
                self.kWeg.distanz = self.aWeg.distanz
                self.kWeg.strecken = [StreckeWeg(von=self.aWeg.strecken[i].von, nach=self.aWeg.strecken[i].nach, dist=self.aWeg.strecken[i].dist) for i in range(self.aWeg.index + 1)]
                self.kWeg.index = self.aWeg.index