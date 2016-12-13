'''
Created on Nov 10, 2016

@author: Bendic 
'''

from copy import deepcopy

class studentControl(object):
    '''
    Class that contains all the instances of studentRepository
    proprieties:
        _repo - list of repositories
    '''
    
    def __init__(self, repo):
        self._repo = [repo]
        
    def __repr__(self):
        return str(self._repo)
   
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
    
    def getCurentRepo(self):
        '''
        getter for the curent repository
        '''
        return self._repo[-1]
    
    def getOCountRepo(self,oCount):
        '''
        getter for a specific repository
        '''
        return self._repo[oCount]
    
    def setRepo(self,newRepo):
        '''
        setter for the repository list
        '''
        self._repo = deepcopy(newRepo)
        
    def addRepo(self,repo):
        '''
        Function to add a new repository to the list
        :param: repo - repo to be added
        '''
        self._repo.append(repo)
        
    def searchStudent(self,studentID):
        '''
        Function to search for a student in studentRepository
        '''
        self.getCurentRepo().searchStudent(studentID)
        
    def addStudent(self,student):
        '''
        Function to add student in repository
        :param: student - student to be added
        '''
        
        self.getCurentRepo().addStudent(student)
        
    def removeStudent(self,studentID):
        '''
        Function to remove a student
        :param: studentID - student to be removed
        '''
        self.getCurentRepo().removeStudent(studentID)
        
    def setStudentID(self,studentID,newID):
        '''
        Function to update a student ID
        :param: studentID - old ID
        :param: newID - new ID
        '''
        self.getCurentRepo().updateStudentID(studentID,newID)
    
    def setStudentName(self,studentID,newName):
        '''
        Funciton to update a student Name
        :param: studentID - the id of the student
        :param: newName - the new name
        '''
        self.getCurentRepo().updateStudentName(studentID,newName)
        
    def search(self,searchString):
        '''
        Function to search for an item in the student Repo
        :param: searchString - item to be searched for
        '''
        self.getCurentRepo().search(searchString)

    def searchAll(self,searchString):
        '''
        Function to search for all the instances of an item
        :param: serachString - string to search for
        '''
        self.getCurentRepo().search(searchString)

    