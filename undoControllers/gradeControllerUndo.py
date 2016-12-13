'''
Created on Dec 11, 2016

@author: Bendi
'''

from undoControllers.undoController import Operation,FunctionCall
from Controllers.gradeController import gradeController

class gradeControllerWithUndo(gradeController):
    
    def __init__(self, gRepo, undoController):
        gradeController.__init__(self, gRepo)
        self._undoController = undoController
        
    
    def create(self, grade, gradeValue):
        
        redo = FunctionCall(self.addGrade, grade, gradeValue)
        undo = FunctionCall(self.removeLastGrade, grade)
       
        operation = Operation(redo, undo)
        self._undoController.newOperation()
        self._undoController.recordOperation(operation)