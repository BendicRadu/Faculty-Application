'''
Created on Dec 10, 2016

@author: Bendic
'''

from Domain.ClassException import classException


class UndoController:
    def __init__(self):
        self._operations = []
        self._index = -1    
        self._recorded = True
    
    def __str__(self):
        return str(self._operations)
    
    def getOperations(self):
        return self._operations
    
    def recordOperation(self, operation):
        if self.isRecorded() == True:
            self._operations[-1].append(operation)

    def newOperation(self):
        if self.isRecorded() == False:
            return

        self._operations = self._operations[0:self._index + 1]
        self._operations.append([])
        self._index += 1

    def isRecorded(self):
        return self._recorded

    def undo(self):
        if self._index < 0:
            return False
        
        self._recorded = False
        
        try:
            for oper in self._operations[self._index]:
                oper.undo()
        except classException:
            print classException() 
        
        except ValueError:
            pass 
    
        self._recorded = True
    
        self._index -= 1
        return True
    
    def redo(self):
        if self._index >= len(self._operations) - 1:
            return False
        
        self._recorded = False
        
        self._index += 1
        
        try:
            for oper in self._operations[self._index]:
                oper.redo()
        except classException:
            pass 
        
        except ValueError:
            pass 
    
        self._recorded = True
    

class FunctionCall:
    def __init__(self, functionRef, *parameters):
        self._functionRef = functionRef
        self._parameters = parameters
        
    def __repr__(self):
        return str(self._functionRef) + str(self._parameters)

    def call(self):
        self._functionRef(*self._parameters)

class Operation:
    def __init__(self, functionDo, functionUndo):
        self._functionDo = functionDo
        self._functionUndo = functionUndo

    def __repr__(self):
        return str(self._functionDo) + str(self._functionUndo)

    def undo(self):
        self._functionUndo.call()

    def redo(self):
        self._functionDo.call()
