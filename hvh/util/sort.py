# coding=utf-8
def vertausche( Feld, i, j ):
    Feld[i], Feld[j] = Feld[j], Feld[i]
    return Feld

def AuswahlSort( Feld ):
    for grenze in range(len(Feld)):
        kleinstes = grenze
        for i in range(grenze, len(Feld)):
            if Feld[i] < Feld[kleinstes]:
                kleinstes = i
        Feld = vertausche(Feld, grenze, kleinstes)
    return Feld

def EinSort( Feld ):
    def FuegeEin( Feld, i ):
        Inhalt = Feld[i]
        while ( ( i > 0 ) & ( Feld[i - 1] > Inhalt ) ):
            Feld[i] = Feld[i - 1]
            i -= 1
        Feld[i] = Inhalt
        return Feld
    for grenze in range(1, len(Feld)):
        Feld = FuegeEin(Feld, grenze)
    return Feld

def BubbleSort( Feld ):
    for grenze in range(len(Feld) - 1):
        for i in range(len(Feld) - 1, grenze, -1):
            if ( Feld[i - 1] > Feld[i] ):
                vertausche(Feld, i, i - 1)
    return Feld

def BubbleSortOpt( Feld ):
    grenze = 0
    while ( grenze < len(Feld) ):
        merke = len(Feld)
        for i in range(len(Feld) - 1, grenze, -1):
            if ( Feld[i - 1] > Feld[i] ):
                vertausche(Feld, i, i - 1)
                merke = i
        grenze = merke
    return Feld

def QuickSort( Feld):
    return QuickSortFunktion(Feld, 0, len(Feld) - 1)
def QuickSortFunktion( Feld, erstes, letztes ):
    if ( erstes < letztes ):
        mitte = ( erstes + letztes ) // 2
        vergleichselement = Feld[mitte]
        vonlinks = erstes
        vonrechts = letztes
        while ( vonlinks <= vonrechts ):
            while ( Feld[vonlinks] < vergleichselement ):
                vonlinks += 1
            while ( Feld[vonrechts] > vergleichselement ):
                vonrechts -= 1
            if ( vonlinks <= vonrechts ):
                vertausche(Feld, vonlinks, vonrechts)
                vonlinks += 1
                vonrechts -= 1
        Feld = QuickSortFunktion(Feld, erstes, vonrechts)
        Feld = QuickSortFunktion(Feld, vonlinks, letztes)
    return Feld