'''
Created on Dec 12, 2016

@author: Bendi
'''


from undoControllers.undoController import Operation,FunctionCall
from Controllers.enrollController import enrollController

class enrollControllerWithUndo(enrollController):
    
    def __init__(self, eRepo, undoController):
        enrollController.__init__(self, eRepo)
        self._undoController = undoController
        
    
    def create(self, enroll):
        
        redo = FunctionCall(self.addEnroll, enroll)
        undo = FunctionCall(self.removeEnroll, enroll)
       
        operation = Operation(redo, undo)
        self._undoController.newOperation()
        self._undoController.recordOperation(operation)