'''
Created on Nov 10, 2016

@author: Bendic
'''

from Domain.Discipline import discipline
from Repositories.DiscplineRepo import disciplineRepository
        
class disciplineRepositoryFile(disciplineRepository):
    '''
    This class contains all 
    Properties:
        _disciplines - list of disciplines
    '''
    
    def __init__(self, path):
        self._path = path
        disciplineRepository.__init__(self)
        self.readRepo()
        
    def readRepo(self):
        with open(self._path,'r') as dFile:
            for line in dFile:
                self._disciplines.append(discipline(int(line.split(' ',1)[0]),line.split(' ',1)[1][:-1]))
