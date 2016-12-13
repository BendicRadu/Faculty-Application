'''
Created on Nov 8, 2016

@author: Bendic
'''

from Domain.Student import student
from Repositories.StudentRepo import studentRepository

class studentRepositoryFile(studentRepository):
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
            for line in sFile:
                self._students.append(student(int(line.split(' ',1)[0]),line.split(' ',1)[1][:-1]))


