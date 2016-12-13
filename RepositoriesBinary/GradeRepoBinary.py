'''
Created on Dec 6, 2016

@author: Bendic
'''


from Repositories.GradeRepo import gradeRepository

import pickle

class gradeRepositoryBinary(gradeRepository):
    '''
    This class contains all the grades
    This class usses the 'gradeRepository' class as it's parent
    Properties:
        _grades - grade List 
    '''
    def __init__(self,path):
        self._path = path 
        gradeRepository.__init__(self)
        self.readRepo()
        
            
    def readRepo(self):
    
        with open(self._path,'r') as gFile:
            self._grades = pickle.load(gFile)
                
                
