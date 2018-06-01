# -*- coding: utf-8 -*-

import sys, os
import pickle
        
class Datei:
    def __init__( self, filename ):
        self.getFilename = filename
        try:
            self = pickle.load(open(filename, "rb"))
        except IOError:
            print "Dateifehler"

    def close( self ):
        pickle.dump(self, open(self.getFilename, "w+"))

    def copy( self, filename ):
        pickle.dump(self, open(filename, "w+"))
