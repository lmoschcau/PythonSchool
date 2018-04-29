# types
TOrt = set([-1, 0, 1, 2, 3, 4, 5])

class Strecke:
    def __init__( self ):
        self.von = None
        self.nach = None

class MatrixStrecke:
    def __init__( self, distanz, geschwindigkeit=30 ):
        """Stellt die Strecke in eine Richtung in der Adjazemsmatrix dar.
        
        distanz:            int(in km)
        geschwindigkeit     int(in km/h; standard=30)"""
        self.dist = distanz
        self.geschw = geschwindigkeit

    def getMinZeit(self):
        return self.dist / self.geschw

# BackTrackSimple

class BackTrackSimple:
    def __init__(self):
        self.cMaxIndex = 5
        self.cStartort = 0
        self.cZielort = 0
        self.aWeg = [Strecke() for i in range(12)]
        self.kWeg = [Strecke() for i in range(12)]
        self.aIndex = 0
        self.kIndex = 0
        self.aKm = 0
        self.kKm = 100000
        self.Karte = None
        #self.nach = 0
    def Succ(original):
        return original + 1

    def InitialisiereAuswahl(self):
        nach = -1

    def NaechsterKandidat(self, nach):
        return (nach + 1)

    def Annehmbar(self, von, nach):
        print("            Anfrage: " + str(von) + "->" + str(nach))
        def Gefahren(von, nach):
            if (self.aIndex == 0):
                return False
            else:
                i = 0
                while not (((self.aWeg[i].von == von) and (self.aWeg[i].nach == nach)) or (i == self.aIndex)):
                    print("                Bedingung [von:  " + str(self.aWeg[i].von == von) + " a: " + str(von) + " weg: " + str(self.aWeg[i].von) + "] [nach: " + str(self.aWeg[i].nach == nach) + " a: " + str(nach) + " weg: " + str(self.aWeg[i].nach) + "]")
                    i  = i + 1
                print("                i: " + str(i))
                return (self.aWeg[i].von == von) and ( self.aWeg[i].nach == nach)
        tmp = ( self.Karte[von][nach] != -1 ) and ( not Gefahren(von, nach))
        print("            Annehmbar: " + str(tmp))
        return tmp
    
    def AlleBesucht(self):
           Orte  = set(TOrt)
           for ZaehlerStr in range(self.aIndex):
                Orte.discard(self.aWeg[ZaehlerStr].von)
                Orte.discard(self.aWeg[ZaehlerStr].nach)
           if (Orte == {-1}):
                return True
           else:
                return False

    def ZeichneSchrittAuf(self, von, nach):
       self.aIndex = self.aIndex + 1
       print("            Aufgezeichnet: " + str(von) + "->" + str(nach))
       self.aWeg[self.aIndex].von = von
       self.aWeg[self.aIndex].nach = nach
       self.aKm = self.aKm + self.Karte[von][nach]
       Ausgabe = ""
       for i in range(12):
           Ausgabe += "(" + str(self.aWeg[i].von) + "->" + str(self.aWeg[i].nach) + ") "
       print("WEG: " + Ausgabe)
       erfolgreich = nach == self.cZielort
       if (erfolgreich and self.AlleBesucht):
        if self.aKm < self.kKm:
          self.kKm = self.aKm
          self.kWeg = self.aWeg
          self.kIndex = self.aIndex
      
    def LoescheSchritt(self, von, nach):
       self.aIndex = self.aIndex - 1
       self.aKm = self.aKm - self.Karte[von][nach]
  

    def KeinKandidatMehr(self, nach):
       return nach == self.cMaxIndex

    def Reise(self, von):
        nach = -1
        self.InitialisiereAuswahl()
        while True:
            nach = self.NaechsterKandidat(nach)
            if self.Annehmbar(von, nach):
                print("        aIndex:  " + str(self.aIndex))
                self.ZeichneSchrittAuf(von, nach)
                self.Reise(nach)
                self.LoescheSchritt(von, nach)
            if self.KeinKandidatMehr(nach): break
 


Karte = [[(-1) for i in TOrt] for j in TOrt]
   
Karte[0][1] = 50
Karte[1][0] = 50
Karte[5][0] = 60
Karte[0][5] = 60
Karte[5][2] = 20
Karte[2][5] = 20
Karte[5][3] = 30
Karte[3][5] = 30
Karte[5][4] = 40
Karte[2][3] = 15
Karte[3][4] = 10
Karte[4][3] = 10
print('Matrix:')

for i in TOrt:     
    for j in TOrt:
        tempString = str(Karte[i][j]) + '    '
        print(tempString, end="")
    print("")


print
print('Strecken:')
BackTrack = BackTrackSimple()
BackTrack.Karte = Karte
input("GO?")
BackTrack.Reise(0)

for Index in range(BackTrack.kIndex):
     
    print(str(BackTrack.kWeg[Index].von) + ' -> ' + str(BackTrack.kWeg[Index].nach) + ' (' +  'km)')
     
print("")
print('Gesamtweg-Laenge: ', BackTrack.kKm)
input("exit?")

