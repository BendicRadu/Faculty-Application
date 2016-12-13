'''
Created on Nov 10, 2016

@author: Bendic
'''

from Domain.StudentEnrolment import enroll
from Repositories.EnrollRepo import enrollRepository


class enrollRepositoryFile(enrollRepository):
    '''
    Class that contains all the enrolments
    properties:
        _enrollment - list of enrolled students 
    '''
    
    def __init__(self, path):
        self._path = path
        enrollRepository.__init__(self)
        self.readRepo()
        
    def readRepo(self):
        with open(self._path,'r') as eFile:
            for line in eFile:
                self._enrolment.append(enroll(int(line.split(' ',1)[0]),int(line.split(' ',1)[1])))
    