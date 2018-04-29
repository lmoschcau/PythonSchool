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
    def __init__( self, *args ):
        self.dist = None
        self.geschw = None
        self.von = None
        self.nach = None
        if len(args) >= 2:
            self.von = args[0]
            self.nach = args[1]

class Weg:
    def __init__(self):
        self.strecken = [StreckeWeg() for i in range(12)]
        self.distanz = None
            
# BackTrackSimple

class BackTrackSimple:
    def __init__(self):
        self.cMaxIndex = 5
        self.cStartort = 0
        self.cZielort = 3
        self.aWeg = [StreckeWeg() for i in range(12)]
        self.kWeg = [StreckeWeg() for i in range(12)]
        self.aIndex = -1
        self.kIndex = 0
        self.aKm = 0
        self.kKm = 100000
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
            
    def InitialisiereAuswahl(self):
        nach = -1

    def NaechsterKandidat(self, nach):
        return (nach + 1)

    def Annehmbar(self, von, nach):
        def Gefahren(von, nach):
            if (self.aIndex == -1):
                return False
            else:
                i = 0
                while not (((self.aWeg[i].von == von) and (self.aWeg[i].nach == nach)) or (i == self.aIndex)):
                    i  = i + 1
                return (self.aWeg[i].von == von) and ( self.aWeg[i].nach == nach)
        return (self.Karte[von][nach] != None ) and ( not Gefahren(von, nach))
  
    def ZeichneSchrittAuf(self, von, nach):
        self.aIndex = self.aIndex + 1
        self.aWeg[self.aIndex].von = von
        self.aWeg[self.aIndex].nach = nach
        self.aKm = self.aKm + self.Karte[von][nach].dist
        self.erfolgreich = nach == self.cZielort

    def LoescheSchritt(self, von, nach):
       self.aIndex = self.aIndex - 1
       self.aKm = self.aKm - self.Karte[von][nach].dist

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
        self.kKm = self.aKm
        self.kWeg = [StreckeWeg(self.aWeg[i].von, self.aWeg[i].nach) for i in range(self.aIndex + 1)]
        self.kIndex = self.aIndex

# BackTrackBester

class BackTrackBester(BackTrackSimple):
  
    def ZeichneSchrittAuf(self, von, nach):
        self.aIndex = self.aIndex + 1
        self.aWeg[self.aIndex].von = von
        self.aWeg[self.aIndex].nach = nach
        self.aKm = self.aKm + self.Karte[von][nach].dist
        self.erfolgreich = nach == self.cZielort
        if (self.erfolgreich):
            if self.aKm < self.kKm:
                self.kKm = self.aKm
                self.kWeg = [StreckeWeg(self.aWeg[i].von, self.aWeg[i].nach) for i in range(self.aIndex + 1)]
                self.kIndex = self.aIndex

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
            
    def AlleBesucht(self):
           Orte  = set(self.zuBesuchendeOrte)
           Orte.add(-1)
           for ZaehlerStr in range(self.aIndex + 1):
                Orte.discard(self.aWeg[ZaehlerStr].von)
                Orte.discard(self.aWeg[ZaehlerStr].nach)
           if (Orte == {-1}):
               return True
           else:
               return False
  
    def ZeichneSchrittAuf(self, von, nach):
        self.aIndex = self.aIndex + 1
        self.aWeg[self.aIndex].von = von
        self.aWeg[self.aIndex].nach = nach
        self.aKm = self.aKm + self.Karte[von][nach].dist
        self.erfolgreich = nach == self.cZielort
        if (self.erfolgreich and self.AlleBesucht()):
            if self.aKm < self.kKm:
                self.kKm = self.aKm
                self.kWeg = [StreckeWeg(self.aWeg[i].von, self.aWeg[i].nach) for i in range(self.aIndex + 1)]
                self.kIndex = self.aIndex

BackTrack = BackTrackBesucht()
BackTrack.FuegeStreckenHinzu([
    (0, 1, 50),
    (1, 0, 50),
    (5, 0, 60),
    (0, 5, 60),
    (5, 2, 20),
    (2, 5, 20),
    (5, 3, 30),
    (3, 5, 30),
    (5, 4, 40),
    (2, 3, 15),
    (3, 4, 10),
    (4, 3, 10)])

print('Matrix:')
for i in TOrt:     
    for j in TOrt:
        tempString = str(BackTrack.Karte[i][j]) + '      '
        print(tempString[:6], end="")
    print("")

print('Strecken:')
input("GO?")
BackTrack.Track(0, 0) # , zuBesuchendeOrte=set([2,3])

for Index in range(BackTrack.kIndex + 1):
    print(str(BackTrack.kWeg[Index].von) + ' -> ' + str(BackTrack.kWeg[Index].nach) + ' (' +  'km)')
     
print("")
print('Gesamtweg-Laenge: ', BackTrack.kKm)
input("exit?")

############################## ToDo ########################
# 
# class Weg
#   def __init__(self):
#       self.Strecken = ...
#       self.Distanz
#       .
#       .
#       .