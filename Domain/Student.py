'''
Created on Nov 8, 2016

@author: Bendic 
'''

class student:
    '''
    Represents an entit student:
        -studentID - unique ID
        -name - name of the student
    '''
    def __init__(self,studentID,name):
        self._studentID = studentID
        self._name = name
        
    def __repr__(self):
        '''
        This function represtents the student
        '''
        return ' StudentID: %s | Name: %r \n' %(self._studentID,self._name)
    
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)
        
    def __gt__(self, other):
        '''
        Function to compare two instances
        :param: other - other instance
        '''
        return self._studentID > other._studentID

    def getId(self):
        '''
        Getter for the id of the student
        :return: an integer representing the id of the student
        '''
        return self._studentID
    
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
        self._studentID = newID
        
    def setName(self,newName):
        '''
        Setter for the student name
        :parameter: the new name
        '''
        self._name = newName

