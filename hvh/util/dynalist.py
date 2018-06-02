class Dynalist:
    class element:
        def __init__(self):
            self.inhalt = None
            self.naechster = None

        def __init__(self, inhalt):
            self.inhalt = inhalt
            self.naechster = None

    def __init__(self, laenge):
        self.list = [None] * laenge
    def __getitem__(self, key):
        return self.list[key]
    def addElement(self, inhalt, pos):
        self.list[pos] = self.element(inhalt)

dyn1 = Dynalist(8)
dyn1.addElement("Hallo", 1)
print(dyn1[1].inhalt)