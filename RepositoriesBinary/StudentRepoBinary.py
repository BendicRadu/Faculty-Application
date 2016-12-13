'''
Created on Nov 8, 2016

@author: Bendic
'''

from Repositories.StudentRepo import studentRepository

import pickle

class studentRepositoryBinary(studentRepository):
    '''
    This class contains all the students
    This class usses the 'studentRepository' class as it's parent
    Properties:
        _students - student List 
    '''
    def __init__(self, path):
        self._path = path 
        studentRepository.__init__(self)
        self.readRepo()
            
    def readRepo(self):
    
        with open(self._path,'r') as sFile:
            self._students = pickle.load(sFile)
                
                
