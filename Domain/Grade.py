'''
Created on Nov 8, 2016

@author: Bendic
'''
from copy import deepcopy

class grade:
    '''
    represents the entity of a grade
    propities:
        studentID - the id of the student
        disciplineID - the id of the Discipline
        grade - the value of the grade
    '''
    
    def __init__(self,disciplineID,studentID):
        self._disciplineID = int(disciplineID)
        self._studentID = int(studentID)
        self._grade = []
        
    def __repr__(self):
        '''
        This function represtents the grade ent
        '''
        return '\nStudentID: %s | DisciplineID: %d \nGrade: %s \n ' %(self._studentID,self._disciplineID,self._grade)
    
    def __gt__(self, other):
        '''
        Function to compare two instances
        :param: other - other instance
        '''
        return self._studentID > other._studentID
    
    def __eq__(self, other):
        '''
        Function to compare two instances
        :param: other - other instance
        '''
        return self._studentID == other._studentID and self._disciplineID == other._disciplineID
        
    def addGrade(self,gradeValue):
        '''
        Function to add a grade
        :param: gradeValue - grade to be added
        '''
        self._grade.append(gradeValue)
    
    def getDisciplineID(self):
        '''
        Getter for the id of the student
        :return: an integer representing the id of the student
        '''
        return self._disciplineID
    
    def getStudentID(self):
        '''
        Getter for the Name of the student
        :return: a string: the name of the student
        '''
        return self._studentID 
    
    def getGrade(self):
        '''
        Getter for the grade of the student
        :return: a float: value of the grade
        '''
        return self._grade 
    
    def getGradeSize(self):
        '''
        Getter for the size of the grade list
        '''
        return len(self.getGrade())
    
    def setDisciplieID(self,newID):
        '''
        Setter for the discipline Id
        :parameter: the new Id 
        '''
        self._disciplineID = newID
        
    def setStudentID(self,newID):
        '''
        Setter for the student Id
        :parameter: the new Id
        '''
        self._studentID = newID
        
    def setGrade(self,newGrade):
        '''
        Setter for the grade
        :parameter: the new grade 
        '''
        self._grade = deepcopy(newGrade)
        
