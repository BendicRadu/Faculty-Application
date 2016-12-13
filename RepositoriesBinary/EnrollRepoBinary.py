'''
Created on Dec 6, 2016

@author: Bendic
'''


from Repositories.EnrollRepo import enrollRepository

import pickle

class enrollRepositoryBinary(enrollRepository):
    '''
    This class contains all the enrolls
    This class usses the 'enrollRepository' class as it's parent
    Properties:
        _enrolls - enroll List 
    '''
    def __init__(self, path):
        self._path = path 
        enrollRepository.__init__(self)
        self.readRepo()
       
            
    def readRepo(self):
    
        with open(self._path,'r') as eFile:
            self._enrollment = pickle.load(eFile)
                
                

