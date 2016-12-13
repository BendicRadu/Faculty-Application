'''
Created on Dec 6, 2016

@author: Bendic
'''


from Domain.Grade import grade
from Domain.ClassException import classException

class gradeRepository:
    '''
    Class that contains the list of grades
    properties:
        _grades - list of grades
    '''
    def __init__(self):
        self._grades = []
     
        
    def __repr__(self):
        '''
        Function to represent grades
        '''
        return str(self._grades)[1:-1]
    
    def getGrades(self):
        '''
        Getter for the grade list
        '''
        return self._grades
    
    def getGradesSize(self):
        '''
        Getter for the grade list size
        '''
        return len(self.getGrades())
    
    def setGrade(self,newRepo):
        '''
        Setter for the grade list
        '''
        self._grades = newRepo
    
    def updateGradeDisciplineID(self,disciplineID,newID):
        '''
        Funtion to update a discipline ID in the grade list
        :param: disciplineID - the discipline ID to be updated
        :param: newName - the new name
        '''
        while True:
            try:
                self.searchDiscipline(disciplineID)
                for grade in self._grades:
                    if grade.getDisciplineID() == disciplineID:
                        grade.setDisciplieID(newID)
            except classException:
                break
        
    def updateGradeStudentID(self,studentID,newID):
        '''
        Function to update a student ID in the grade list
        :param: studentID - the student ID to be updated
        :param: newID - the new ID
        '''
        index = 0 
        while True:
            try:
                if index > self.getGradesSize():
                    break
                index += 1
                self.searchStudent(studentID)
                for grade in self._grades:
                    if grade.getStudentID() == studentID:
                        print 'ok'
                        grade.setStudentID(newID)
            except classException:
                break
    
    def searchStudent(self,studentID):
        '''
        Funtion to find a student ID in the list
        :param: studentID - id to searh for
        '''
        for grade in self._grades:
            if grade.getStudentID() == studentID:
                return grade
        raise classException('Student not found')
    
    def searchDiscipline(self,disciplineID):
        '''
        Funtion to find a discipline ID in the list
        :param: disciplineID - id to searh for
        '''
        for grade in self._grades:
            if grade.getDisciplineID() == disciplineID:
                return grade 
        raise classException('Discipline not found')
    
    def searchGrade(self, grade):
        '''
        Function to find a grade in the list
        :param: grade - grade to search for
        '''
        
        for grades in self._grades:
            if grades.getDisciplineID() == grade.getDisciplineID() and grades.getStudentID() == grade.getStudentID():
                return grade
        raise classException('Grade not found')
    
    def removeGradeStudent(self,studentID):
        '''
        Funciton to remove a student from the grade list
        :param: studentID - student to be removed
        '''
        index = 0
        while index <= len(self._grades) - 1:
            grade = self._grades[index]
            if int(grade.getStudentID()) == int(studentID):
                del self._grades[index]
                index = 0
            index += 1
        raise classException('ID not found')
    
    def removeGradeDiscipline(self,disciplineID):
        '''
        Funciton to remove a discipline from the grade list
        :param: disciplineID - discipline to be removed
        '''
        index = 0
        while index <= len(self._grades) - 1:
            enroll = self._grades[index]
            if enroll.getDisciplineID() == disciplineID:
                del self._grades[index]
                index = 0
            index += 1
        raise classException('ID not found')
    
    def removeGrade(self, grade):
        '''
        Function to remove a grade based on enrollment
        :param: enroll - enrollment to be removed
        '''
        for index in range(len(self._grades) - 1):
            gradeObj = self._grades[index]
            if gradeObj == grade:
                del self._grades[index]
                return 
        raise classException('ID not found')
    
    def addGrade(self,grade,gradeValue):
        '''
        Function to add a new grade
        :param: grade - grade to be added
        :param: gradeValue - grade value to be added
        '''
        try:
            for grades in self._grades:
                if grades.getDisciplineID() == grade.getDisciplineID() and grades.getStudentID() == grade.getStudentID():
                    grades.addGrade(gradeValue)
                    return 
            self._grades.append(grade)
            self.addGrade(grade, gradeValue)
        except classException:
            raise ValueError("Student was not graded")
        
    
    def addEnrollGrade(self,enroll,gradeValue):
        '''
        Function to add a new grade based on enrollment
        :param: enroll - grade to be added
        :param: gradeValue - grade value to be added
        '''
        try:
            for grades in self._grades:
                if grades.getDisciplineID() == enroll.get_discipline_id() and grades.getStudentID() == enroll.get_student_id():
                    grades.addGrade(gradeValue)
                    return 
            self._grades.append(grade)
            self.addGrade(grade, gradeValue)
        except classException:
            raise ValueError("Student was not graded")
    
    
    def addGradeList(self, grade):
        '''
        Funtcion to add a list of grades
        :param: grade - grade instance
        '''
        
        try:
            self.searchGrade(grade)
        except classException:
            self._grades.append(grade)
    
    
    def removeGradeList(self, grade):
        '''
        Function to remove a list of grades
        :param: grade - grade to be removed
        '''
        
        print grade
        
        self._grades.remove(grade)
    
    
    def removeLastGrade(self, grade):
        '''
        Funtcion to remove he last grade from a lis tof grades
        :param: grade - grade instance
        '''
        try:
            for grades in self._grades:
                if grades.getDisciplineID() == grade.getDisciplineID() and grades.getStudentID() == grade.getStudentID():
                    grades.getGrade().pop()
                    return
        except classException:
            raise ValueError("Student was not graded")
        