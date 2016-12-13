'''
Created on Nov 10, 2016

@author: Bendic
'''

class disciplineControl(object):
    '''
    Class to control the discipline repository
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
        self._repo = newRepo
        
    def addRepo(self,disciplineRepository):
        '''
        Function to add a new repository to the list
        :param: disciplineRepository
        '''
        self._repo.append(disciplineRepository)
        
    def searchDiscipline(self,disciplineID):
        '''
        Function to search for a discipline in disciplineRepository
        :param: disciplineID - discipline to search for
        '''
        self.getCurentRepo().searchDiscipline(disciplineID)
        
    def addDiscipline(self,discipline):
        '''
        Function to add discipline in repository
        :param: discipline - discipline to be added
        '''
        self.getCurentRepo().addDiscipline(discipline)
        
    def removeDiscipline(self,disciplineID):
        '''
        Function to remove a discipline
        :param: disciplineID - discipline to be removed
        '''
        self.getCurentRepo().removeDiscipline(disciplineID)
        
    def setDisciplineID(self,disciplineID,newID):
        '''
        Function to update a discipline ID
        :param: disciplineID - old ID
        :param: newID - new ID
        '''
        self.getCurentRepo().updateDisciplineID(disciplineID,newID)
    
    def setDisciplineName(self,disciplineID,newName):
        '''
        Funciton to update a discipline Name
        :param: disciplineID - the id of the discipline
        :param: newName - the new name
        '''
        self.getCurentRepo().updateDisciplineName(disciplineID,newName)
    
    def search(self,searchString):
        '''
        Function to search for an item in the discipline Repo
        :param: searchString - item to be searched for
        '''
        self.getCurentRepo().search(searchString)
        
    def searchAll(self,searchString):
        '''
        Function to search for all the instances of an item
        :param: serachString - string to search for
        '''
        self.getCurentRepo().search(searchString)