'''
Created on Nov 8, 2016

@author: Bendic
'''

class enroll:
    '''
    represents a entity of enrolment
        properties:
            _studentID - the id of the student
            _disciplineID - the id of
    '''
    def __init__(self,studentID,disciplineID):
        self._studentID = studentID
        self._disciplineID = disciplineID

        
    def __repr__(self):
        return ' StudentID: %s | DisciplineID: %d \n' %(self._studentID,self._disciplineID)
        
    def __gt__(self, other):
        '''
        Function to compare two instances
        :param: other - other instance
        '''
        return self._studentID > other._studentID
    
    
    def get_student_id(self):
        '''
        getter for student id 
        '''
        return self._studentID


    def get_discipline_id(self):
        '''
        getter for discipline id
        '''
        return self._disciplineID


    def set_student_id(self, value):
        '''
        setter for student id
        '''
        self._studentID = value


    def set_discipline_id(self, value):
        '''
        setter for discipline id
        '''
        self._disciplineID = value
        
    