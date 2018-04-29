# coding=utf-8
import util.io as io
import util.backtrack as backtrack
import colorama
from time import sleep as sleep

colorama.init()

input("GO?")
BackTrack = backtrack.BackTrackBesucht()
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
print(list({""} | (backtrack.TOrt - {-1})))
table = io.Table(list({""} | (backtrack.TOrt - {-1})))
for i in backtrack.TOrt - {-1}:
    Zeile = [i]
    for j in backtrack.TOrt - {-1}:
        Zeile.append(BackTrack.Karte[i][j])
    table.ZeileHinzufügen(Zeile)

#table.RandStielHorizontal = {0:"S", 1:"D", 2:"N"}
table.GibTabelleAus(4, flush=True)

print('Strecken:')
input("GO?")
TrackErgebniss = BackTrack.Track(0, 0) # , zuBesuchendeOrte=set([2,3])

for Index in range(TrackErgebniss.index + 1):
    print(str(TrackErgebniss.strecken[Index].von) + ' -> ' + str(TrackErgebniss.strecken[Index].nach) + ' (' + str(TrackErgebniss.strecken[Index].dist) + 'km)')
     
print("")
print('Gesamtweg-Laenge: ', TrackErgebniss.distanz)
input("exit?")