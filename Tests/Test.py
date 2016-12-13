'''
Created on Nov 14, 2016

@author: Bendic
'''

import unittest

from Domain.Student import student
from Domain.Discipline import discipline
from Domain.Grade import grade
from Domain.StudentEnrolment import enroll

from RepositoriesFile.DisciplineRepoFile import disciplineRepository
from RepositoriesFile.StudentRepoFile import studentRepository
from RepositoriesFile.EnrollRepoFile import enrollRepository
from RepositoriesFile.GradeRepoFile import gradeRepository


class unitTest(unittest.TestCase):
    '''
    Class for all the test functions
    '''
    def testClasses(self):
        '''
        Function for the class tests
        '''
        
        '''
        :Student: :Section:
        '''
        sTest = student(-1,'Test')
        assert sTest.getId() == -1 
        assert sTest.getName() == 'Test'
        sTest.setId(int(-2))
        assert sTest.getId() == -2
        sTest.setName('Test2')
        assert sTest.getName() == 'Test2'
        
        '''
        :Discipline: :Section:
        '''
        dTest = discipline(-1,'Test')
        assert dTest.getId() == -1 
        assert dTest.getName() == 'Test'
        dTest.setId(int(-2))
        assert dTest.getId() == -2
        dTest.setName('Test2')
        assert dTest.getName() == 'Test2'
        
        '''
        :Enroll: :Section:
        '''
        eTest = enroll(1,1)
        assert eTest.get_discipline_id() == 1
        assert eTest.get_student_id() == 1
        eTest.set_discipline_id(2)
        assert eTest.get_discipline_id() == 2
        eTest.set_student_id(2)
        assert eTest.get_student_id() == 2
        
        '''
        :Grade: :Section:
        '''
        gTest = grade(1,1)
        assert gTest.getDisciplineID() == 1
        assert gTest.getStudentID() == 1 
        gTest.addGrade(10)
        assert gTest.getGrade() == [10]
        assert gTest.getGradeSize() == 1
        gTest.setDisciplieID(2)
        assert gTest.getDisciplineID() == 2
        gTest.setStudentID(int(-2))
        
        
    def testRepos(self):
        '''
        Function for the repository test
        '''
        
        '''
        :Student: :Section:
        '''
        sTest = studentRepository()
        sTest.setStudents([])
        assert sTest.getStudents() == []
        assert sTest.getStudentSize() == 0
        sTest.addStudent(student(1,'Test'))
        assert sTest.getStudents() == [student(1,'Test')]
        assert sTest.searchStudent(1) == student(1,'Test')
        sTest.updateStudentID(1,2)
        assert sTest.getStudents()[0].getId() == 2
        sTest.updateStudentName(2,'Test2')
        assert sTest.getStudents()[0].getName() == 'Test2'
        sTest.removeStudent(2)
        assert sTest.getStudents() == []
        
        '''
        :Discipline: :Section:
        '''
        
        dTest = disciplineRepository()
        dTest.setDisciplines([])
        assert dTest.getDisciplines() == []
        assert dTest.getDisciplinesSize() == 0
        dTest.addDiscipline(discipline(1,'Test'))
        assert dTest.getDisciplines() == [discipline(1,'Test')]
        assert dTest.searchDiscipline(1) == discipline(1,'Test')
        dTest.updateDisciplineID(1,2)
        assert dTest.getDisciplines()[0].getId() == 2
        dTest.updateDisciplineName(2,'Test2')
        assert dTest.getDisciplines()[0].getName() == 'Test2'
        dTest.removeDiscipline(2)
        assert dTest.getDisciplines() == []
        
        '''
        :Enroll: :Section:
        '''
        eTest = enrollRepository()
        eTest.setEnroll([])
        assert eTest.getEnroll() == []
        assert eTest.getEnrollSize() == 0
        en = enroll(1,1)
        eTest.addEnrolment(en)
        assert eTest.getEnrollSize() == 1
        assert eTest.getEnroll() == [en]
        assert eTest.searchEnrolment(en) == en
        eTest.addEnrolment(enroll(1,2))
        eTest.addEnrolment(enroll(2,3))
        eTest.removeEnrollDiscipline(2)
        eTest.removeEnrollStudent(2)
        assert eTest.getEnrollSize() == 1
        
        '''
        :Grade: :Section:
        '''
        gTest = gradeRepository()
        gTest.setGrade([])
        assert gTest.getGradesSize() == 0
        assert gTest.getGrades() == []
        gr = grade(1,1)
        gTest.addGrade(gr,10)
        assert gTest.getGrades() == [gr]
        assert gTest.getGrades()[0].getGrade() == [10.0]
        gTest.updateGradeDisciplineID(1, 2)
        assert gTest.getGrades()[0].getDisciplineID() == 2
        gTest.updateGradeStudentID(1,10)
        assert gTest.getGrades()[0].getStudentID() == 10
        gTest.removeGradeDiscipline(2)
        assert gTest.getGradesSize() == 0
        gr = grade(1,1)
        gTest.addGrade(gr,10)
        gr1 = grade(10,1)
        gTest.addGrade(gr1,10)
        assert gTest.getGradesSize() == 2
        assert gTest.getGrades() == [gr,gr1]
        gr2 = grade(1,10)
        gTest.addGrade(gr2,10)
        assert gTest.getGrades() == [gr,gr1,gr2] 
        gTest.removeGradeDiscipline(10)
        assert gTest.getGrades() == [gr,gr2]
        gTest.removeGradeStudent(10)
        assert gTest.getGrades() == [gr] 
        