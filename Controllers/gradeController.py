'''
Created on Nov 10, 2016

@author: Bendic
'''

class gradeController(object):
    '''
    Class that contains all the instances of gradeRepository
    proprieties:
        _repo - list of repositories
    '''
    
    def __init__(self, repo):
        self._repo = [repo]
        
    def __repr__(self):
        return str(self.getCurentRepo())[1:-1]
   
    def getRepo(self):
        '''
        getter for the repository list
        '''
        return self._repo
    
    def getRepoSize(self):
        '''
        getter fot the repostitory size
        '''
        return len(self._repo)
    
    
    def getOCountRepo(self,oCount):
        '''
        getter for a specific repository
        '''
        return self._repo[oCount]
    
    def getCurentRepo(self):
        '''
        getter for the curent repository
        '''
        return self._repo[-1]
    
    def setRepo(self,newRepo):
        '''
        setter for the repository list
        '''
        self._repo = newRepo
        
    def addRepo(self,gradeRepository):
        '''
        Function to add a new repository to the list
        :param: gradeRepository
        '''
        self._repo.append(gradeRepository)
        
    def searchGrade(self):
        '''
        Function to search for a grade in gradeRepository
        '''
        self.getCurentRepo().searchGrade()
        
    def addGrade(self,grade,gradeValue):
        '''
        Function to add grade in repository
        :param: grade - grade to be added
        :param: gradeValue - grade value to be added
        '''
        self.getCurentRepo().addGrade(grade,gradeValue)
        
    def removeGradeStudent(self,studentID):
        '''
        Function to remove a student 
        :param: studentID - student ID to be removed
        '''
        self.getCurentRepo().removeGradeStudent(studentID)
        
    def removeGradeDiscipline(self,disciplineID):
        '''
        Function to remove a discipline
        :param: disciplineID - discipline ID to be removed
        '''
        self.getCurentRepo().removeGradeDiscipline(disciplineID)
    
    def removeGrade(self,enroll):
        '''
        Function to remove a grade based on enrollment
        :param: enroll - enrollment to be removed
        '''
        self.getCurentRepo().removeGrade(enroll)
    
    def setStudentID(self,studentID,newID):
        '''
        Function to update a grade student ID
        :param: studentID - old ID
        :param: newID - new ID
        '''
        self.getCurentRepo().updateGradeStudentID(studentID,newID)
    
    def setDisciplineID(self,disciplineID,newID):
        '''
        Funciton to update a grade discipline ID
        :param: gradeID - the id of the grade
        :param: newID - the new ID
        '''
        self.getCurentRepo().updateGradeDisciplineID(disciplineID,newID)
    
    def addGradeList(self, grade):
        '''
        Function to add a grade list
        :param: grade - grade instance to be added
        '''
        
        print 'ADD GRADE LIST OK'
        
        self.getCurentRepo().addGradeList(grade)
        
    def removeLastGrade(self, grade):
        '''
        Function to remove the last grade from a list of grades
        :pararm: grade - grade instace 
        '''
        self.getCurentRepo().removeLastGrade(grade)
        
    def removeGradeList(self, grade):
        
        print 'REMOVE GRADE LIST CONTROLLER OK'
        
        self.getCurentRepo().removeGradeList(grade)