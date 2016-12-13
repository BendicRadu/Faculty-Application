'''
Created on Dec 10, 2016

@author: Bendi
'''

from Domain.Student import student
from undoController import FunctionCall, Operation

from Controllers.studentController import studentControl


class studentControlWithUndo(studentControl):
    def __init__(self, sRepo, eCTRL, gCTRL, undoController):
        studentControl.__init__(self, sRepo)
        self._undoController = undoController
        self._eCTRL = eCTRL
        self._gCTRL = gCTRL      
    
    def create(self, studentID, name):
        
        redo = FunctionCall(self.addStudent, student(studentID, name))
        undo = FunctionCall(self.removeStudent, studentID)
        operation = Operation(redo, undo)
        self._undoController.newOperation()
        self._undoController.recordOperation(operation)   
      
        
    def delete(self, studentID, eList, gList, name):
       
        studentID = int(studentID)
       
        redo = FunctionCall(self.removeStudent, studentID) 
        undo = FunctionCall(self.addStudent, student(studentID, name))
        
        operation = Operation(redo, undo)
        self._undoController.newOperation()
        self._undoController.recordOperation(operation)
        
        
        
        for Grade in gList:
            
            redo = FunctionCall(self._gCTRL.removeGradeList, Grade)
            undo = FunctionCall(self._gCTRL.addGradeList, Grade)
            
            operation = Operation(redo, undo)
            self._undoController.recordOperation(operation)
        
        
        for Enroll in eList:
            
            redo = FunctionCall(self._eCTRL.removeEnrollStudent, studentID)
            undo = FunctionCall(self._eCTRL.addEnroll, Enroll)
            
            operation = Operation(redo, undo)
            self._undoController.recordOperation(operation)

    
        
        
        
    def updateID(self, oldID, newID):
        
        oldID = int(oldID)
        newID = int(newID)
        
        redo = FunctionCall(self.setStudentID, oldID, newID)
        undo = FunctionCall(self.setStudentID, newID, oldID)
        
        operation = Operation(redo, undo)
        self._undoController.newOperation()
        self._undoController.recordOperation(operation)
        
        redo = FunctionCall(self._eCTRL.updateStudentID, oldID, newID)
        undo = FunctionCall(self._eCTRL.updateStudentID, newID, oldID)
        
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)
        
        redo = FunctionCall(self._gCTRL.setStudentID, oldID, newID)
        undo = FunctionCall(self._gCTRL.setStudentID, newID, oldID)
        
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)
        
        
    def updateName(self, studentID, oldName, newName):
        
        studentID = int(studentID)
        
        redo = FunctionCall(self.setStudentName, studentID, newName)
        undo = FunctionCall(self.setStudentName, studentID, oldName)
        
        operation = Operation(redo, undo)
        self._undoController.newOperation()
        self._undoController.recordOperation(operation)
        