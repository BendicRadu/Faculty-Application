'''
Created on Dec 6, 2016

@author: Bendic 
'''

from Domain.StudentEnrolment import enroll

import pickle

class ePickle:
    
    def __init__(self):
        self._list = []
        pickle.HIGHEST_PROTOCOL
        self.readRepo()
        self.dumpPickle()
            
    def readRepo(self):
        with open('C:\Users\user\Desktop\Uni\FP\Eclipse\Lab 5-7 Propper\Initializers\enrollments','r') as eFile:
            for line in eFile:
                self._list.append(enroll(int(line.split(' ',1)[0]),int(line.split(' ',1)[1])))
    
    def dumpPickle(self):
        with open('C:\Users\user\Desktop\Uni\FP\Eclipse\Lab 5-7 Propper\InitializersPickle\ePickleFile','w') as eFile:
            for index in self._list:
                pickle.dump(index,eFile)
        
        
obj = ePickle()
