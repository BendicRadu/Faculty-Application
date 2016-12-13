'''
Created on Nov 8, 2016

@author: Bendic
'''


from Repositories.DiscplineRepo import disciplineRepository

import pickle

class disciplineRepositoryBinary(disciplineRepository):
    '''
    This class contains all the disciplines
    This class usses the 'disciplineRepository' class as it's parent
    Properties:
        _disciplines - discipline List 
    '''
    def __init__(self,path):
        self._path = path 
        disciplineRepository.__init__(self)
        self.readRepo()
        
            
    def readRepo(self):
    
        with open(self._path,'r') as dFile:
            self._disciplines = pickle.load(dFile)
                
