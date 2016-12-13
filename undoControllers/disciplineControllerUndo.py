'''
Created on Dec 11, 2016

@author: Bendi
'''


from Domain.Discipline import discipline
from undoController import FunctionCall, Operation 

from Controllers.disciplineController import disciplineControl


class disciplineControlWithUndo(disciplineControl):
    def __init__(self, sRepo, eCTRL, gCTRL, undoController):
        disciplineControl.__init__(self, sRepo)
        self._undoController = undoController
        self._eCTRL = eCTRL
        self._gCTRL = gCTRL      
    
    def create(self, disciplineID, name):
        
        redo = FunctionCall(self.addDiscipline, discipline(disciplineID, name))
        undo = FunctionCall(self.removeDiscipline, disciplineID)
        operation = Operation(redo, undo)
        self._undoController.newOperation()
        self._undoController.recordOperation(operation)   
      
        
    def delete(self, disciplineID, eList, gList, name):
       
        disciplineID = int(disciplineID)
       
        redo = FunctionCall(self.removeDiscipline, disciplineID) 
        undo = FunctionCall(self.addDiscipline, discipline(disciplineID, name))
        
        operation = Operation(redo, undo)
        self._undoController.newOperation()
        self._undoController.recordOperation(operation)
        
        
        for Grade in gList:
            redo = FunctionCall(self._gCTRL.removeGradeList, Grade)
            undo = FunctionCall(self._gCTRL.addGradeList, Grade)
            operation = Operation(redo, undo)
            self._undoController.recordOperation(operation)
        
        
        for Enroll in eList:
            redo = FunctionCall(self._eCTRL.removeEnrollDiscipline, Enroll.get_discipline_id())
            undo = FunctionCall(self._eCTRL.addEnroll, Enroll)
            operation = Operation(redo, undo)
            self._undoController.recordOperation(operation)
  
     
            
        
    def updateID(self, oldID, newID):
        
        oldID = int(oldID)
        newID = int(newID)
        
        redo = FunctionCall(self.setDisciplineID, oldID, newID)
        undo = FunctionCall(self.setDisciplineID, newID, oldID)
        
        operation = Operation(redo, undo)
        self._undoController.newOperation()
        self._undoController.recordOperation(operation)
        
        redo = FunctionCall(self._eCTRL.updateDisciplineID, oldID, newID)
        undo = FunctionCall(self._eCTRL.updateDisciplineID, newID, oldID)
        
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)
        
        redo = FunctionCall(self._gCTRL.setDisciplineID, oldID, newID)
        undo = FunctionCall(self._gCTRL.setDisciplineID, newID, oldID)
        
        operation = Operation(redo, undo)
        self._undoController.recordOperation(operation)
        
    
    def updateName(self, disciplineID, oldName, newName):
        
        disciplineID = int(disciplineID)
        
        redo = FunctionCall(self.setDisciplineName, disciplineID, newName)
        undo = FunctionCall(self.setDisciplineName, disciplineID, oldName)
        
        operation = Operation(redo, undo)
        self._undoController.newOperation()
        self._undoController.recordOperation(operation)
        