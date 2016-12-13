'''
Created on Nov 10, 2016

@author: Bendic
'''

from Validator.Validate import Valid
from Domain.Student import student
from Domain.Discipline import discipline
from Domain.StudentEnrolment import enroll
from Domain.Grade import grade
from Domain.ClassException import classException


from operator import itemgetter
from copy import deepcopy

class menuUI:
    
  
    
    '''
    The menu UI class
    properties:
        _studentControl - the student controller
        _disciplinenrolControl - the discipline controller
        _gradenrolControl - the grade controller
        _enrolControl - the enrol controller
    '''
    
    
    def compare(self):
        if self.oCont >= self.Max:
            self.Max = self.oCont
            return 
        

    def addRepo(self,sCTRL,dCTRL,eCTRL,gCTRL):    
        
        self._sMain.insert(self.oCont, deepcopy(sCTRL))
        self._dMain.insert(self.oCont, deepcopy(dCTRL))
        self._eMain.insert(self.oCont, deepcopy(eCTRL))
        self._gMain.insert(self.oCont, deepcopy(gCTRL))
        
    def getRepo(self):
        self._studentControl = deepcopy(self._sMain[self.oCont])
        self._disciplineControl = deepcopy(self._dMain[self.oCont])
        self._enrolControl = deepcopy(self._eMain[self.oCont])
        self._gradeControl = deepcopy(self._gMain[self.oCont])
        
  
    #==========================================================================================#
    '''
    :Student: :Section:
    '''
    #==========================================================================================#
    
      
    
    def add_Student(self):
        studentID = int(input('\nEnter student ID: '))
        name = str(raw_input('Enter student Name: '))
        Valid().name(name)
        Valid().ID(studentID)
   
        S = self._studentControl
        D = self._disciplineControl
        E = self._enrolControl
        G = self._gradeControl
        
        self.addRepo(S,D,E,G)
        
        self._studentControl.addStudent(student(studentID,name))
        print '\nStudent has been added'
        
        self.oCont += 1
        self.compare()
    
    def updateStudent(self):
        print '\n1). Update student ID'
        print '2). Update student name'
        option = input('Enter Option:')
        
        
        S = self._studentControl
        D = self._disciplineControl
        E = self._enrolControl
        G = self._gradeControl
        
        self.addRepo(S,D,E,G)
        
        
        if option != 1 and option != 2:
            print 'Option invalid'
            return
        
        elif option == 1:
            studentID = int(input('\nEnter student ID: '))
            newID = int(input('Enter new ID: '))
            self._studentControl.setStudentID(studentID,newID)
            self._enrolControl.updateStudentID(studentID,newID)
            self._gradeControl.setStudentID(studentID,newID)
            print '\nStudent ID has been updated'
            
            self.oCont += 1
            self.compare()
    
        
        elif option == 2:
            studentID = int(input('\nEnter student ID: '))
            newName = raw_input('Enter new name: ')
            self._studentControl.setStudentName(studentID,newName)
            print '\nStudent name has been updated'
            
            self.oCont += 1
            self.compare()
    
    def removeStudent(self):
        studentID = int(input('\nEnter student ID: '))
        
        S = self._studentControl
        D = self._disciplineControl
        E = self._enrolControl
        G = self._gradeControl
        
        self.addRepo(S,D,E,G)
        
        self._studentControl.removeStudent(studentID)
        self._gradeControl.removeGradeStudent(studentID)
        self._enrolControl.removeEnrollStudent(studentID)
        print '\nStudent has been removed'
        
        self.oCont += 1
        self.compare()
    
    
    #==============================================================================================#    
    '''
    :Discipline: :Section:
    '''
    #==============================================================================================#

    def addDiscipline(self):
        disciplineID = int(input('\nEnter discipline ID: '))
        name = str(raw_input('Enter discipline Name: '))
        
        Valid().name(name)
        Valid().ID(disciplineID)
        
        S = self._studentControl
        D = self._disciplineControl
        E = self._enrolControl
        G = self._gradeControl
        
        self.addRepo(S,D,E,G)
        
        self._disciplineControl.addDiscipline(discipline(disciplineID,name))
        print '\nDiscipline has been added'
        self.oCont += 1
        self.compare()
    
    def updateDiscipline(self):
        print '\n1). Update discipline ID'
        print '2). Update discipline name'
        option = input('Enter Option:')
        
        S = self._studentControl
        D = self._disciplineControl
        E = self._enrolControl
        G = self._gradeControl
        
        self.addRepo(S,D,E,G)
        
        
        if option != 1 and option != 2:
            print 'Option invalid'
            return
        
        
        elif option == 1:
            disciplineID = int(input('\nEnter discipline ID: '))
            newID = int(input('Enter new ID: '))
            self._disciplineControl.setDisciplineID(disciplineID, newID)
            self._enrolControl.updateDisciplineID(disciplineID,newID)
            self._gradeControl.setDisciplineID(disciplineID,newID)
            print '\nDiscipline ID has been updated'
            self.oCont += 1
            self.compare()
        
        
        elif option == 2:
            disciplineID = int(input('\nEnter discipline ID: '))
            newName = raw_input('Enter new name: ')
            self._disciplineControl.setDisciplineName(disciplineID,newName)
            print '\nDiscipline name has been updated'
            self.oCont += 1
            self.compare()
        
    
    def removeDiscipline(self):
        disciplineID = int(input('\nEnter discipline ID: '))
        
        S = self._studentControl
        D = self._disciplineControl
        E = self._enrolControl
        G = self._gradeControl
        
        self.addRepo(S,D,E,G)
        
        self._disciplineControl.removeDiscipline(disciplineID)
        self._gradeControl.removeGradeDiscipline(disciplineID)
        self._enrolControl.removeEnrollDiscipline(disciplineID)
        print '\nDiscipline has been removed'
        self.oCont += 1
        self.compare()
        
           
    
    #=====================================================================================#
    '''
    :Enrollment: :Section:
    '''
    #=====================================================================================#
    
    def addEnrollment(self):
        studentID = int(input('\nEnter student ID: '))
        disciplineID = int(input('Enter discipline ID: ')) 
        
        Valid().ID(studentID)
        Valid().ID(disciplineID)
        
        S = self._studentControl
        D = self._disciplineControl
        E = self._enrolControl
        G = self._gradeControl
        
        self.addRepo(S,D,E,G)
        
        self._disciplineControl.searchDiscipline(disciplineID)
        self._studentControl.searchStudent(studentID)
        self._enrolControl.addEnroll(enroll(studentID,disciplineID))
        print '\nEnrollment has been added'
        self.oCont += 1
        self.compare()
        
        
        
    def removeEnrollment(self):
        studentID = int(input('\nEnter student ID: '))
        disciplineID = int(input('Enter discipline ID: '))
        self._enrolControl.removeEnroll(enroll(studentID,disciplineID))
        print '\nErnollment had been removed'
        self.oCont += 1
        self.compare()
        
        
        
    
    #=====================================================================================#
    '''
    :Grade: :Section:
    '''
    #=====================================================================================#
    def gradeStudent(self):
        studentID = int(input('\nEnter student ID: '))
        disciplineID = int(input('Enter discipline ID: '))
        gradeValue = float(input('Enter grade: '))
        
        Valid().ID(studentID)
        Valid().ID(disciplineID)
        Valid().grade(gradeValue)
        
        S = self._studentControl
        D = self._disciplineControl
        E = self._enrolControl
        G = self._gradeControl
        
        self.addRepo(S,D,E,G)
        
        try:
            self._enrolControl.searchEnroll(enroll(studentID,disciplineID))
            self._gradeControl.addGrade(grade(disciplineID,studentID),gradeValue)
            self.oCont += 1
            self.compare()
        
        
        except ValueError:
            print '\nStudent has been graded'
    
    
    
    #=====================================================================================#
    '''
    :Search: :Section:
    '''
    #=====================================================================================#
    
    def searchAll(self):
        searchString = raw_input('Search for: ')
        print ' \nDisciplines: \n '
        print self._disciplineControl.searchAll(searchString)
        print ' \nStudents: \n'
        print self._studentControl.searchAll(searchString)
    
    #=====================================================================================#
    '''
    :Statistic: :Section:
    '''
    #=====================================================================================#
    
    def statEnroll(self):
        disciplineID =int(input('\nEnter discipline ID:'))
        print '\n1). Sort alphabetically'
        print '2). Sort by grade'
        option = input('Enter Option:')
        if option != 1 and option != 2:
            print 'Option invalid'
            return
        
        elif option == 1:
            sList = []
            for enroll in self._enrolControl.getCurentRepo().getEnroll():
                if enroll.get_discipline_id() == disciplineID:
                    sList.append(enroll.get_student_id())
            
            for index in range(len(sList)):
                for student in self._studentControl.getCurentRepo().getStudents():
                    if sList[index] == student.getId():
                        sList[index] = student.getName()
            
            sList.sort()
            print '\n' 
            for index in sList:
                print index
            del sList[:]
        
        elif option == 2:
            sList = [[' ',-1]]
            for grade in self._gradeControl.getCurentRepo().getGrades():
                if grade.getDisciplineID() == disciplineID:
                    for student in self._studentControl.getCurentRepo().getStudents():
                        if student.getId() == grade.getStudentID():
                            if grade.getGrade() != []:
                                gradeAvg = self.listAvg(grade.getGrade(),grade.getGradeSize())
                                sList.append([student.getName(),gradeAvg])
            
            sList.sort(key=itemgetter(1),reverse = True)
            print '\n'
            for index in range(len(sList)-1):
                print sList[index]
            del sList[:]
            
    
    def statFailing(self):
        sList = [['','']]
        for grade in self._gradeControl.getCurentRepo().getGrades():
            for student in self._studentControl.getCurentRepo().getStudents():
                for discipline in self._disciplineControl.getCurentRepo().getDisciplines():
                    if grade.getStudentID() == student.getId():
                        if grade.getDisciplineID() == discipline.getId():
                            if grade.getGrade() != []:
                                gradeAvg = self.listAvg(grade.getGrade(),grade.getGradeSize())
                                if gradeAvg < 5:
                                    sList.append([student.getName(),discipline.getName()])
        
        print '\n'
        for index in sList:
            print index[0],' - ',index[1]
        del sList[:]
    
    
    def statBest(self):
        sList =[['','']]
        gList =[]
        sName = ''
        for student in self._studentControl.getCurentRepo().getStudents():
            for grade in self._gradeControl.getCurentRepo().getGrades():
                if student.getId() == grade.getStudentID():
                    if(grade.getGrade() != []):
                        gAvg = self.listAvg(grade.getGrade(), grade.getGradeSize())
                        gList.append(gAvg)
                        sName = student.getName()
            if gList != []:
                sAvg = self.listAvg(gList, len(gList))
                sList.append([sName,round(sAvg,2)])
        
        sList.sort(key=itemgetter(1),reverse = True)
        print '\n'
        for index in range(1,len(sList)):
            print sList[index][0],' - ',sList[index][1]
        del sList[:]
    
    def statDiscipline(self):
        sList =[['','']]
        gList =[]
        dName = ''
        for discipline in self._disciplineControl.getCurentRepo().getDisciplines():
            for grade in self._gradeControl.getCurentRepo().getGrades():
                if discipline.getId() == grade.getDisciplineID():
                    if(grade.getGrade() != []):
                        gAvg = self.listAvg(grade.getGrade(), grade.getGradeSize())
                        gList.append(gAvg)
                        dName = discipline.getName()
            if gList != []:
                sAvg = self.listAvg(gList, len(gList))
                sList.append([dName,round(sAvg,2)])
            
        sList.sort(key=itemgetter(1),reverse = True)
        print '\n'
        for index in range(1,len(sList)):
            print sList[index][0],' - ',sList[index][1]
        del sList[:]
    
    def menu(self):
        '''
        UI function - displays menu
        '''
        while True:
            try:
                print 
                print
                print '       -Menu-        '
                print 
                print '-Students:' 
                print
                print '1).  Add student'
                print '2).  Update student'
                print '3).  Remove student'
                print '4).  Student list'
                print
                print '-Disciplines:'
                print
                print '5).  Add discipline'
                print '6).  Update discipline'
                print '7).  Remove discipline'
                print '8).  Discipline list'
                print 
                print '-Discipline Enrollment:'
                print
                print '9).  Add enrollment'
                print '10). Remove enrollment'
                print '11). Enrollment list'
                print 
                print '-Grades:'
                print  
                print '12). Grade a student'
                print '13). Grade list'
                print 
                print '-Search:'
                print
                print '14). Search'
                print 
                print '-Statistics:'
                print 
                print '15). Students enrolled at discipline '
                print '16). Failing students'
                print '17). Best students'
                print '18). All grades'
                print
                print '-Undo/Redo'
                print 
                print '19). Undo'
                print '20). Redo'
                print 
                print  
                option = int(input('Please enter your option: '))
                
                if option < 1 or option > 20:
                    print 'Invalid Input'
                    
                elif option == 1:
                    self.add_Student()
                
                elif option == 2:
                    self.updateStudent()    
                
                elif option == 3:
                    self.removeStudent()
                
                elif option == 4:
                    print self._studentControl.getCurentRepo()
                
                elif option == 5:
                    self.addDiscipline()    
                
                elif option == 6:
                    self.updateDiscipline()
                
                elif option == 7:
                    self.removeDiscipline()
                
                elif option == 8:
                    print self._disciplineControl.getCurentRepo()
                    
                elif option == 9:
                    self.addEnrollment()
                
                elif option == 10:
                    self.removeEnrollment()
                    
                elif option == 11:
                    print self._enrolControl.getCurentRepo()
                
                elif option == 12:
                    self.gradeStudent()
                
                elif option == 13:
                    print self._gradeControl
                
                elif option == 14:
                    self.searchAll()
                    
                elif option == 15:
                    self.statEnroll()
                    
                elif option == 16:
                    self.statFailing() 
                
                elif option == 17:
                    self.statBest()
                    
                elif option == 18:
                    self.statDiscipline()
                
                elif option == 19:
                    if self.oCont >= 1:
                        self.oCont -= 1
                        self.getRepo()
                
                elif option == 20:
                    if self.oCont < self.Max - 1:
                        self.oCont += 1
                        self.getRepo()   
                     
            except ValueError:
                print '\nInvalid input , Value Error'
            
            except NameError:
                print '\nInvalid input, Name Error'
                
            except SyntaxError:
                print '\nInvalid input, Syntax Error'
                
            except classException:
                print '\nInvalid input, class exception'
                
    
    
    def __init__(self,studentControl,disciplineControl,gradeControl,enrolControl):
        self._studentControl = deepcopy(studentControl)
        self._disciplineControl = deepcopy(disciplineControl)
        self._gradeControl = deepcopy(gradeControl)
        self._enrolControl = deepcopy(enrolControl)
        self.oCont = 0
        self.Max = 0
        
        self._studentControl = deepcopy(studentControl)
        self._disciplineControl = deepcopy(disciplineControl)
        self._gradeControl = deepcopy(gradeControl)
        self._enrolControl = deepcopy(enrolControl)
        
        self._sMain = [deepcopy(self._studentControl)]
        self._dMain = [deepcopy(self._disciplineControl)]
        self._eMain = [deepcopy(self._enrolControl)]
        self._gMain = [deepcopy(self._gradeControl)]
        
        self.menu()
    
    @staticmethod
    def listAvg(myList,size):
        s = 0.0
        for index in range(size):
            s += myList[index]
        s /= size
        return s
    



class startCBM:
    def __init__(self,C1,C2,C3,C4):
        menuUI(C1,C2,C3,C4)
