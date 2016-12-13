'''
Created on Dec 6, 2016

@author: Bendic 
'''

from Domain.Grade import grade

import pickle

class gPickle:
    
    def __init__(self):
        self._list = []
        pickle.HIGHEST_PROTOCOL
        self.readRepo()
        self.dumpPickle()
            
    def readRepo(self):
        with open('C:\Users\user\Desktop\Uni\FP\Eclipse\Lab 5-7 Propper\Initializers\grades','r') as gFile:
            for line in gFile:
                g = grade(int(line.split()[1]),(int(line.split()[0])))
                g.addGrade(float(line.split()[2]))
                g.addGrade(float(line.split()[3]))
                self._list.append(g)
                
    def dumpPickle(self):
        with open('C:\Users\user\Desktop\Uni\FP\Eclipse\Lab 5-7 Propper\InitializersPickle\gPickleFile','w') as gFile:
            for index in self._list:
                pickle.dump(index,gFile)
        
        
