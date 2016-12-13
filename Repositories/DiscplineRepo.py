'''
Created on Dec 6, 2016

@author: Bendic
'''


from Domain.Discipline import discipline
from Domain.ClassException import classException
        
class disciplineRepository:
    '''
    This class contains all 
    Properties:
        _disciplines - list of disciplines
    '''
    
    def __init__(self):
        self._disciplines = [discipline(1,'Fundamental of Programing')]
                
    def __repr__(self):
        return str(self._disciplines)[0:-1]
    
    def getDisciplines(self):
        '''
        Getter for the discipline list
        '''
        return self._disciplines
    
    def getDisciplinesSize(self):
        '''
        Getter for the discipline list size
        '''
        return len(self.getDisciplines())
    
    def setDisciplines(self,newList):
        '''
        Setter for the discipline list
        '''
        self._disciplines = newList 
    
    def searchDiscipline(self,disciplineID):
        '''
        Function to find a discipline in the list
        :param: disciplindeID - dicipline to be found 
        '''
        for discipline in self.getDisciplines():
            if discipline.getId() == disciplineID:
                return discipline
        raise classException('Discipline not found')
    
    def searchAll(self,searchString):
        '''
        Function to find all instances of the search string
        :param: searchString - string to search for
        '''
        for index in range(self.getDisciplinesSize()):
            for discipline in self.getDisciplines():
                if searchString in self.getDisciplines()[index].getName() or searchString in str(self.getDisciplines()[index].getId()):
                    print self.getDisciplines()[index] 
    
    def addDiscipline(self,discipline):
        '''
        Funciton to add discipline to the discipline list
        :param: discipline - discipline to be added
        '''
        try:
            self.searchDiscipline(discipline.getId())
            raise ValueError('Discipline ID already taken')
        except classException:
            self._disciplines.append(discipline)
    
     
    def updateDisciplineID(self,disciplineID,newID):
        '''
        Function to update the ID of a discipline
        :param: disciplineID - the discipline ID to be updated
        :param: newID - the new ID
        '''
        try:
            self.searchDiscipline(newID)
            raise ValueError('Discipline ID already taken')
        except classException:
            for discipline in self.getDisciplines():
                if discipline.getId() == disciplineID:
                    discipline.setId(newID)
                    return
            raise classException('ID not found!')
    
    
    def updateDisciplineName(self,disciplineID,newName):
        '''
        Function to update a discipline name
        :param: disciplineID - the discipline ID to be updated
        :param: newName - the new name
        '''
        for discipline in self.getDisciplines():
            if discipline.getId() == disciplineID:
                discipline.setName(newName)
                return
        raise classException('ID not found!')
        
           
    def removeDiscipline(self,disciplineID):
        '''
        Function to remove a discipline from the discipline list
        :param: disciplineID - discipline to be removed
        '''
        for index in range(len(self._disciplines)):
            discipline = self._disciplines[index]
            if discipline.getId() == disciplineID:
                del self._disciplines[index]
                return
        raise classException('ID not found')
    
    def search(self,searchString):
        '''
        Function to search in the discipline list
        :param: searchString - string to be searched for
        '''
        for discipline in self._disciplines:
            if searchString.lower() in str(discipline.getId()).lower() or str(discipline.getId()).lower() in searchString.lower() or searchString.lower() in discipline.getName().lower() or discipline.getName().lower() in searchString.lower():
                print discipline
            
