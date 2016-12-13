'''
Created on Nov 12, 2016

@author: Bendic
'''

class idError(Exception):
    pass


class Valid:
    '''
    Class that contains validators
    '''
    def grade(self,gradeValue):
        '''
        function to validate a grade
        :param: gradeValue - grade to be validated
        '''
        
        gradeValue = float(gradeValue)
        
        if gradeValue > 10 or gradeValue < 1:
            raise ValueError
        
    def name(self,name):
        '''
        function to validate a name
        :param: name - name to be validated
        '''
        if name == '':
            raise NameError
        
        for index in name:
            try:
                int(index)
                raise NameError
            except ValueError:
                pass
            
    def ID(self,ID):
        '''
        function to validate an ID
        :param: ID - id to be validated 
        '''
        try:
            int(ID)
        except ValueError:
            raise idError