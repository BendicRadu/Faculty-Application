'''
Created on Dec 6, 2016

@author: Bendic 
'''

from Domain.Student import student

import pickle

class sPickle:
    
    def __init__(self):
        self._list = []
        pickle.HIGHEST_PROTOCOL
        self.readRepo()
        self.dumpPickle()
            
    def readRepo(self):
        with open('C:\Users\user\Desktop\Uni\FP\Eclipse\Lab 5-7 Propper\Initializers\students','r') as sFile:
            for line in sFile:
                self._list.append(student(int(line.split(' ',1)[0]),line.split(' ',1)[1][:-1]))
            
    def dumpPickle(self):
        with open('C:\Users\user\Desktop\Uni\FP\Eclipse\Lab 5-7 Propper\InitializersPickle\sPickleFile','w') as sFile:
            for index in self._list:
                pickle.dump(index,sFile)
        
        
obj = sPickle()
