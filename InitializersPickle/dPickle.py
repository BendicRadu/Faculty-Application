'''
Created on Dec 6, 2016

@author: Bendic 
'''

from Domain.Discipline import discipline

import pickle

class dPickle:
    
    def __init__(self):
        self._list = []
        pickle.HIGHEST_PROTOCOL
        self.readRepo()
        self.dumpPickle()
            
    def readRepo(self):
        with open('C:\Users\user\Desktop\Uni\FP\Eclipse\Lab 5-7 Propper\Initializers\disciplines','r') as dFile:
            for line in dFile:
                self._list.append(discipline(int(line.split(' ',1)[0]),line.split(' ',1)[1][:-1]))
            
    def dumpPickle(self):
        with open('C:\Users\user\Desktop\Uni\FP\Eclipse\Lab 5-7 Propper\InitializersPickle\dPickleFile','w') as dFile:
            for index in self._list:
                pickle.dump(index,dFile)
        
        
obj = dPickle()
