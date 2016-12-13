'''
Created on Nov 8, 2016

@author: Bendic
'''

class discipline:
    '''
    Represents an entity discipline:
        -disciplineID - unique ID
        -name - name of the student
    '''
    def __init__(self,disciplineID,name):
        self._disciplineID = disciplineID 
        self._name = name
        
    def __repr__(self):
        '''
        This function represtents the student
        '''
        return 'Discipline ID: %d | Name: %s \n'  %(self._disciplineID,self._name)
    
    def __eq__(self, other):
        '''
        Function to compare two instances
        :param: other - other instance
        '''
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)
    
    def __gt__(self, other):
        '''
        Function to compare two instances
        :param: other - other instance
        '''
        return self._disciplineID > other._disciplineID
    
    def getId(self):
        '''
        Getter for the id of the student
        :return: an integer representing the id of the student
        '''
        return self._disciplineID
    
    def getName(self):
        '''
        Getter for the Name of the student
        :return: a string: the name of the student
        '''
        return self._name 
    
    def setId(self,newID):
        '''
        Setter for the student Id
        :parameter: the new Id 
        '''
        self._disciplineID = newID
        
    def setName(self,newName):
        '''
        Setter for the student name
        :parameter: the new name
        '''
        self._name = newName
