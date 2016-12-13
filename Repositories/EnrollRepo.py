'''
Created on Dec 6, 2016

@author: Bendic
'''



from Domain.StudentEnrolment import enroll
from Domain.ClassException import classException


class enrollRepository:
    '''
    Class that contains all the enrolments
    properties:
        _enrollment - list of enrolled students 
    '''
    
    def __init__(self):
        self._enrolment = [enroll(1,1)]
        
    
    def __repr__(self):
        '''
        Function to represent enrollment
        '''
        return str(self._enrolment)[1:-1]
    
    def getEnroll(self):
        '''
        getter for enrolment
        '''
        return self._enrolment
    
    def getEnrollSize(self):
        '''
        getter for enrolment size
        '''
        return len(self._enrolment)
    
    def setEnroll(self,newRepo):
        '''
        setter for enrolmnet
        '''
        self._enrolment = newRepo
    
    def updateStudentID(self,studentID,newID):
        '''
        Function to update a student ID
        :param: studentID - id to be replaced
        :param: newID - new id 
        '''
        while True:
            try:
                self.searchStudent(studentID)
                for enrollment in self._enrolment:
                    if enrollment.get_student_id() == studentID:
                        enrollment.set_student_id(newID)
            except classException:
                break
    

    def updateDisciplineID(self,disciplineID,newID):
        '''
        Function to update a student ID
        :param: disciplineID - id to be replaced
        :param: newID - new id 
        '''
        while True:
            try:
                self.searchDiscipline(disciplineID)
                for enrollment in self._enrolment:
                    if enrollment.get_discipline_id() == disciplineID:
                        enrollment.set_discipline_id(newID)
            except classException:
                break
    
    def searchStudent(self,studentID):
        '''
        Funtion to find a student ID in the list
        :param: studentID - id to searh for
        '''
        for enrollment in self._enrolment:
            if enrollment.get_student_id() == studentID:
                return enrollment
        raise classException('Student not found')
    
    def searchDiscipline(self,disciplineID):
        '''
        Funtion to find a discipline ID in the list
        :param: disciplineID - id to searh for
        '''
        for enrollment in self._enrolment:
            if enrollment.get_discipline_id() == disciplineID:
                return enrollment 
        raise classException('Discipline not found')
    
    def searchEnrolment(self,enroll):
        '''
        Function to find enrollment in enrolment list
        :param: enroll - enrolment to search for
        '''
        for enrollment in self._enrolment:
            if enrollment.get_student_id() == enroll.get_student_id() and enrollment.get_discipline_id() == enroll.get_discipline_id():
                return enroll
        raise classException('Student not enrolled')
        
    def addEnrolment(self,enroll):
        '''
        Funciton to add enrolmnet to the discipline list
        :param: enroll - new enrolment
        '''
        try:
            self.searchEnrolment(enroll)
            raise ValueError('Student not enrolled')
        except classException:
            self._enrolment.append(enroll)
             
            
    def removeEnrolment(self,enroll):
        '''
        Function to remove a student Enrolment
        :param: enroll - enroll to be removed
        '''
        try:
            self.searchEnrolment(enroll)
            for index in range(len(self._enrolment)-1):
                if self._enrolment[index].get_student_id() == enroll.get_student_id() and self._enrolment[index].get_discipline_id() == enroll.get_discipline_id():
                    del self._enrolment[index]
        except classException:
            raise ValueError('Enrolment not found!')
        
      
    def removeEnrollStudent(self,studentID):
        '''
        Funciton to remove a student from the enrollment list
        :param: studentID - student to be removed
        '''
        index = 0
        while index <= len(self._enrolment) - 1:
            enroll = self._enrolment[index]
            if enroll.get_student_id() == studentID:
                del self._enrolment[index]
                index = 0
            index += 1
        raise classException('ID not found')
    
    def removeEnrollDiscipline(self,disciplineID):
        '''
        Funciton to remove a discipline from the enroll list
        :param: disciplineID - discipline to be removed
        '''
        index = 0
        while index <= len(self._enrolment) - 1:
            enroll = self._enrolment[index]
            if enroll.get_discipline_id() == disciplineID:
                del self._enrolment[index]
                index = 0
            index += 1
        raise classException('ID not found')
    