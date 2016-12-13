'''
Created on Nov 10, 2016

@author: Bendic
'''

class enrollController(object):
    '''
    Class that contains all the instances of enrollRepository
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
    
    def addRepo(self,repo):
        '''
        Funtion to add a new repo to the list
        :param: repo - new repository
        '''
        self._repo.append(repo)
    
    def removeEnrollStudent(self,studentID):
        '''
        Function to remove a student 
        :param: studentID - student ID to be removed
        '''
        self.getCurentRepo().removeEnrollStudent(studentID)
    
    def updateStudentID(self,studentID,newID):
        '''
        Function to update a student ID
        :param: studentID - id to be replaced
        :param: newID - the new id
        '''
        self.getCurentRepo().updateStudentID(studentID,newID)
        
    def updateDisciplineID(self,disciplineID,newID):
        '''
        Function to update a discipline ID
        :param: disciplineID - id to be replaced
        :param: newID - the new id
        '''
        self.getCurentRepo().updateDisciplineID(disciplineID,newID)
    
    def removeEnrollDiscipline(self,disciplineID):
        '''
        Function to remove a discipline
        :param: disciplineID - discipline ID to be removed
        '''
        self.getCurentRepo().removeEnrollDiscipline(disciplineID)  
         
    def searchEnroll(self,enroll):
        '''
        Function to search for a enroll in enrollRepository
        :param: studentID - student ID
        :param: disciplineID - discipline ID
        '''
        self.getCurentRepo().searchEnrolment(enroll)
        
    def addEnroll(self,enroll):
        '''
        Function to add grade in repository
        :param: grade - grade to be added
        '''
        self.getCurentRepo().addEnrolment(enroll)
        
    def removeEnroll(self,enroll):
        '''
        Function to remove an enrollment from the list
        :param: enroll - enrollment to be removed
        '''
        self.getCurentRepo().removeEnrolment(enroll)
        
        