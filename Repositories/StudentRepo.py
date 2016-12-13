'''
Created on Dec 6, 2016

@author: Bendic
'''


from Domain.Student import student
from Domain.ClassException import classException

class studentRepository:
    '''
    This class contains all the students
    Properties:
        _students - student List 
    '''
    def __init__(self):
        self._students = [student(1,'Stefania Matei')]
        
    def __repr__(self):
        '''
        This function represtents the student
        '''
        return str(self._students)[1:-1]
    
    def getStudents(self):
        '''
        getter for the student list
        '''
        return self._students
    
    def getStudentSize(self):
        '''
        getter for the size of student list
        '''
        return len(self._students)
    
    def setStudents(self,newList):
        '''
        setter for the student list
        '''
        self._students = newList
    
    def searchStudent(self,studentID):
        '''
        Function to find a student in the list
        :param: studentID - student to be found
        '''
        for student in self.getStudents():
            if student.getId() == studentID:
                return student
        raise classException('Student not found!') 
       
    def searchAll(self,searchString):
        '''
        Function to find all instances of the search string
        :param: searchString - string to search for
        '''
        for index in range(self.getStudentSize()):
            for student in self.getStudents():
                if searchString in self.getStudents()[index].getName() or searchString in str(self.getStudents()[index].getId()):
                    print self.getStudents()[index] 
                    if index == self.getStudentSize() - 1:
                        break 
                    else:
                        index += 1
                    
    def addStudent(self,student):
        '''
        Function to add a student to the student list
        :param: student - student to be added
        '''
        try:
            self.searchStudent(student.getId())
            raise ValueError('Student ID already taken')
        except classException:
            return self._students.append(student)
    
            
    def updateStudentID(self,studentID,newID):
        '''
        Function to update a student ID
        :param: studentID - the student ID to be updated
        :param: newID - the new ID
        '''
        try:
            self.searchStudent(newID)
            raise ValueError('Student ID already taken')
        except classException:
            for student in self.getStudents():
                if student.getId() == studentID:
                    student.setId(newID)
                    return
            raise classException('ID not found!')
    
    def updateStudentName(self,studentID,newName):
        '''
        Function to update a student name
        :param: studentID - the student ID to be updated
        :param: newName - the new name
        '''
        for student in self.getStudents():
            if student.getId() == studentID:
                student.setName(newName)
                return
        raise classException('ID not found!')
    
    
    def removeStudent(self,studentID):
        '''
        Function to remove a student from the list
        :param: studentID - student to be removed
        '''        
        for index in range (len(self._students)):
            student = self._students[index]
            if student.getId() == studentID:
                del self._students[index]
                return
        raise classException('ID not found!')


    def search(self,searchString):
        '''
        Function to search in the student list
        :param: searchString - string to be searched for
        '''
        for student in self._students:
            if searchString.lower() in str(student.getId()).lower() or str(student.getId()).lower() in searchString.lower() or searchString.lower() in student.getName().lower() or student.getName().lower() in searchString.lower():
                print student
