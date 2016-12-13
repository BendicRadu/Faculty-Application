'''
Created on Nov 10, 2016

@author: Bendic
'''

from Domain.Grade import grade
from Repositories.GradeRepo import gradeRepository


class gradeRepositoryFile(gradeRepository):
    '''
    Class that contains the list of grades
    properties:
        _grades - list of grades
    '''
    def __init__(self, path):
        self._path = path
        gradeRepository.__init__(self)
        self.readRepo()
        
        
    def readRepo(self):  
        with open(self._path,'r') as gFile:
            for line in gFile:
                g = grade(int(line.split()[1]),(int(line.split()[0])))
                g.addGrade(float(line.split()[2]))
                g.addGrade(float(line.split()[3]))
                self._grades.append(g)