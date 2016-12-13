'''
Created on Nov 15, 2016

@author: Bendic
'''

import Tkinter as tk
from Tkinter import Frame, Tk, Menubutton, Menu, Label, Listbox, END, TclError, ANCHOR
#import traceback


from copy import deepcopy
from operator import itemgetter, index

from Domain.Student import student
from Domain.Discipline import discipline
from Domain.StudentEnrolment import enroll
from Domain.Grade import grade

from GUI_Classes.window2 import Window2
from GUI_Classes.windowRemove import WindowRemove
from Domain.ClassException import classException

from Validator.Validate import Valid
from Validator.Validate import idError

import tkMessageBox
import pickle


class Application(Frame):
    
    def compress(self,sCTRL,dCTRL,eCTRL,gCTRL):
        
        allCTRL = {'Student': sCTRL,'Discipline': dCTRL, 'Enroll': eCTRL, 'Grade': gCTRL}
        pickle.dump( allCTRL, open( "save.p", "wb" ) )
    
    def compare(self):
        if self.oCont >= self.Max:
            self.Max = self.oCont
            return 
        
        
    def reader(self,Input,InputNumber):
        try:
            Input.getvar((str(InputNumber)))
        except TclError as tcl:
            s = str(tcl)
            return s.split("\"")[1]

    def clearText(self):
        self.textFrame.delete('1.0',END)
    
    def Srefresh(self):
        controller = self._studentControl.getCurentRepo().getStudents() 
        curList = self.sList
        curList.delete(0,END)
        controller.sort()
        for index in controller:
            curList.insert(END,index)
        
    def Drefresh(self):
        controller = self._disciplineControl.getCurentRepo().getDisciplines() 
        curList = self.dList
        curList.delete(0,END)
        controller.sort()
        for index in controller:
            curList.insert(END,index)
    
    def Erefresh(self):
        controller = self._enrolControl.getCurentRepo().getEnroll() 
        curList = self.eList
        curList.delete(0,END)
        controller.sort()
        for index in controller:
            curList.insert(END,index)
    
    def Grefresh(self):
        controller = self._gradeControl.getCurentRepo().getGrades()
        curList = self.gList
        curList.delete(0,END)
        controller.sort()
        for index in controller:
            curList.insert(END,index)
    
    def refreshALL(self):
        self.Srefresh()
        self.Drefresh()
        self.Erefresh()
        self.Grefresh()
    
    def SreadID(self,string):
        return string[11:string.index('|')-1]

    def DreadID(self,string):
        return string[15:string.index('|')-1]
    
    def EreadID(self,string):
        return [string[12:string.index('|')-1],string[string.index('|') + 15:-2]]
    
    def sPopup(self, event):
        self.sMenu.post(event.x_root, event.y_root)
        
    def dPopup(self, event):
        self.dMenu.post(event.x_root, event.y_root)
        
    def ePopup(self, event):
        self.eMenu.post(event.x_root, event.y_root)
    
    def gPopup(self, event):
        self.gMenu.post(event.x_root, event.y_root)
        
    def displayError(self,msg):
        tkMessageBox.showerror('Error', msg)
        
    def NewFile(self):
        self._studentControl.setRepo(deepcopy(student(1,'')))  
        self._disciplineControl.setRepo(deepcopy(discipline(1,'')))  
        self._enrolControl.setRepo(deepcopy(enroll(1,1)))  
        self._gradeControl.setRepo(deepcopy(grade(1,1)))
        self.refreshALL()
        
    '''
    #============================================#
    :STUDENT:
    #============================================#
    '''    
    def add_Student(self):
        try:
            top = tk.Toplevel()
            top.title('Input')
            Input = Window2('Enter student ID: ','Enter student Name: ',top)
            Input.mainloop()
            top.destroy()
           

            if not Input.getvar(str(Input.Input1)) == None and not Input.getvar(str(Input.Input2)) == None:
                
                studentID = Input.getvar(str(Input.Input1))
                name = Input.getvar(str(Input.Input2))
                
                print studentID
                print name 
                
                Valid().ID(studentID)
                Valid().name(name)
                
                self._studentControl.getCurentRepo().addStudent(student(int(studentID),name))
                self._studentControl.create(int(studentID),name)
               
                self.refreshALL()
            
        except ValueError:
            self.displayError('Invalid Input')
        
        except NameError:
            self.displayError('Invalid Name')
            
        except idError:
            self.displayError('Invalid ID')
        
    def remove_Student(self):
        try:
            index = self.sList.curselection()
            studentID = self.SreadID(self.sList.get(index))
            studentID = int(studentID)
           
            name = ''
            eList = []
            gList = []
            
            for Student in self._studentControl.getCurentRepo().getStudents():
                if int(Student.getId()) == studentID:
                    name = Student.getName()
                    
            for enroll in self._enrolControl.getCurentRepo().getEnroll():
                if enroll.get_student_id() == studentID:
                    eList.append(enroll)
            
            for grade in self._gradeControl.getCurentRepo().getGrades():
                if int(grade.getStudentID()) == studentID:
                    gList.append(grade)
            
            try:
                self._studentControl.removeStudent(studentID)
            except classException:
                pass
            try:
                self._enrolControl.removeEnrollStudent(studentID)
            except classException:
                pass
            try:
                self._gradeControl.removeGradeStudent(studentID)
            except classException:
                pass
               
            self._studentControl.delete(studentID, eList, gList, name)
         
            self.refreshALL()
            
        except ValueError:
            self.displayError('Invalid Input')
        
        except NameError:
            self.displayError('Invalid Name')
           
        except TclError:
            self.displayError('No item selected')
    
    def update_StudentID(self):
        try:
            top = tk.Toplevel()
            top.title('Input')
            Input = WindowRemove('New ID',top)
            Input.mainloop()
            top.destroy()
            
            index = self.sList.curselection()
            studentID = self.SreadID(self.sList.get(index))
            studentID = int(studentID)
                    
            if not Input.getvar(str(Input.Input1)) == None:    
                newID = Input.getvar(str(Input.Input1))
                newID = int(newID)
                self._studentControl.getCurentRepo().updateStudentID(studentID,newID)
                self._enrolControl.getCurentRepo().updateStudentID(studentID,newID)
                self._gradeControl.getCurentRepo().updateGradeStudentID(int(studentID),newID)
                
                self._studentControl.updateID(studentID, newID)
              
            self.refreshALL()
        

        except ValueError:
            self.displayError('Invalid Input')
        
        except NameError:
            self.displayError('Invalid Name')
            
        except TclError:
            self.displayError('No item selected')
        
        
            
    def update_StudentName(self):
        try:
            top = tk.Toplevel()
            top.title('Input')
            Input = WindowRemove('New name',top)
            Input.mainloop()
            top.destroy()
            
            index = self.sList.curselection()
            studentID = self.SreadID(self.sList.get(index))
            studentID = int(studentID)
            
            oldName =  self.sList.get(index)[self.sList.get(index).index('|') + 9 : - 2]
                
            if not Input.getvar(str(Input.Input1)) == None:    
                newName = Input.getvar(str(Input.Input1))
                Valid().name(newName)
                self._studentControl.getCurentRepo().updateStudentName(studentID,newName)
                
                self._studentControl.updateName(studentID, oldName, newName)
              
                self.refreshALL()
        
        except ValueError:
            self.displayError('Invalid Input')
        
        except NameError:
            self.displayError('Invalid Name')
                
        except TclError:
            self.displayError('No item selected')
        
            
    '''
    #=============================================#
    :DISCIPLINE:
    #=============================================#
    '''
    def add_Discipline(self):
        try:
            top = tk.Toplevel()
            top.title('Input')
            Input = Window2('Enter discipline ID: ','Enter discipline Name: ',top)
            Input.mainloop()
            top.destroy()
            
            if not Input.getvar(str(Input.Input1)) == None or not Input.getvar(str(Input.Input2)) == None:
                disciplineID = Input.getvar(str(Input.Input1))
                name = Input.getvar(str(Input.Input2))
                Valid().name(name)
                Valid().ID(disciplineID)
                self._disciplineControl.getCurentRepo().addDiscipline(discipline(int(disciplineID),name))
               
                self._disciplineControl.create(int(disciplineID),name)
                
                self.refreshALL()
   
        except ValueError:
            self.displayError('Invalid Input')
        
        except NameError:
            self.displayError('Invalid Name')
            
        except TclError:
            self.displayError('No item selected')
            
        except idError:
            self.displayError('Invalid ID')
        
        
    def remove_Discipline(self):
        try:
            index = self.dList.curselection()
            disciplineID = self.DreadID(self.dList.get(index))
            disciplineID = int(disciplineID)
            
            name = ''
            eList = []
            gList = []
            
            for Discipline in self._disciplineControl.getCurentRepo().getDisciplines():
                if int(Discipline.getId()) == disciplineID:
                    name = Discipline.getName()
                    
            for enroll in self._enrolControl.getCurentRepo().getEnroll():
                if enroll.get_discipline_id() == disciplineID:
                    eList.append(enroll)
            
            for grade in self._gradeControl.getCurentRepo().getGrades():
                if grade.getDisciplineID() == disciplineID:
                    gList.append(grade)
                    
            
            try:
                self._disciplineControl.removeDiscipline(disciplineID)
            except classException:
                pass
            try:
                self._gradeControl.removeGradeDiscipline(disciplineID)
            except classException:
                pass
            
            try:
                self._enrolControl.removeEnrollDiscipline(disciplineID)
            except classException:
                pass
          
            try:
                self._disciplineControl.delete(disciplineID, eList, gList, name)
            except classException:
                pass
            
            self.refreshALL()
        
        except ValueError:
            self.displayError('Invalid Input')
        
        except NameError:
            self.displayError('Invalid Name')
                
        except TclError:
            self.displayError('No item selected')
    
    def update_DisciplineID(self):
        try:
            top = tk.Toplevel()
            top.title('Input')
            Input = WindowRemove('New ID',top)
            Input.mainloop()
            top.destroy()
            
            index = self.dList.curselection()
            disciplineID = self.DreadID(self.dList.get(index))
            disciplineID = int(disciplineID)
            
                    
            if not Input.getvar(str(Input.Input1)) == None:    
                newID = Input.getvar(str(Input.Input1))
                newID = int(newID)
                self._disciplineControl.getCurentRepo().updateDisciplineID(disciplineID,newID)
                self._enrolControl.getCurentRepo().updateDisciplineID(disciplineID,newID)
                self._gradeControl.getCurentRepo().updateGradeDisciplineID(disciplineID,newID)
                
                self._disciplineControl.updateID(disciplineID, newID)
                
                self.refreshALL()
        
        except ValueError:
            self.displayError('Invalid Input')
        
        except NameError:
            self.displayError('Invalid Name')
                
        except TclError:
            self.displayError('No item selected')
            
            
    def update_DisciplineName(self):
        try:
            top = tk.Toplevel()
            top.title('Input')
            Input = WindowRemove('New name',top)
            Input.mainloop()
            top.destroy()
            
            index = self.dList.curselection()
            disciplineID = self.DreadID(self.dList.get(index))
            disciplineID = int(disciplineID)
            
            oldName =  self.dList.get(index)[self.dList.get(index).index('|') + 8 : - 2]
    
            if not Input.getvar(str(Input.Input1)) == None:    
                newName = Input.getvar(str(Input.Input1))
                Valid().name(newName)
                self._disciplineControl.getCurentRepo().updateDisciplineName(disciplineID,newName)
                
                self._disciplineControl.updateName(disciplineID, oldName, newName)
                
                self.refreshALL()
        
        
        except ValueError:
            self.displayError('Invalid Input')
        
        except NameError:
            self.displayError('Invalid Name')
                
        except TclError:
            self.displayError('No item selected')
    
    '''
    #===================================================#
    :ENROLL:
    #===================================================#
    '''
    
    def remove_Enroll(self):
        try:
            index = self.eList.curselection()
            IDs = self.EreadID(self.eList.get(index))
            studentID = int(IDs[0])
            disicplineID = int(IDs[1])
            
            self.eList.delete(ANCHOR)
            self._gradeControl.removeGrade(enroll(studentID,disicplineID))
            self._enrolControl.removeEnroll(enroll(studentID,disicplineID))
            self.Erefresh()
            self.Grefresh()
            
            self.refreshALL()
        
        except ValueError:
            self.displayError('Invalid Input')
        
        except NameError:
            self.displayError('Invalid Name')
                
        except TclError:
            self.displayError('No item selected')
        
    def add_Enroll(self):
        try:
            index = self.sList.curselection()
            studentID = self.SreadID(self.sList.get(index))
            studentID = int(studentID)
            
            index = self.dList.curselection()
            disciplineID = self.DreadID(self.dList.get(index))
            disciplineID = int(disciplineID)
            
            #try:
            self._enrolControl.addEnroll(enroll(studentID,disciplineID))
            #except ValueError:
                #self.displayError('Enrollment allready exists')
            
            
            self._enrolControl.create(enroll(studentID, disciplineID))
            
            self.refreshALL()
        
        except ValueError:
            self.displayError('Invalid Input')
        
        except NameError:
            self.displayError('Invalid Name')
                
        except TclError:
            self.displayError('No item selected')
        
    def add_EnrollGrade(self):
        try:
            top = tk.Toplevel()
            top.title('Input')
            Input = WindowRemove('Grade: ',top)
            Input.mainloop()
            top.destroy()
            
            
            index = self.eList.curselection()
            IDs = self.EreadID(self.eList.get(index))
            studentID = int(IDs[0])
            disciplineID = int(IDs[1])
            
            if not Input.getvar(str(Input.Input1)) == None:    
                gradeValue = Input.getvar(str(Input.Input1))
                gradeValue = float(gradeValue)
                
                Valid().grade(gradeValue)
                
                self._gradeControl.addGrade(grade(disciplineID,studentID),gradeValue)
                self.Grefresh()
            
                self.refreshALL()
                
        except ValueError:
            self.displayError('Invalid Input')
        
        except NameError:
            self.displayError('Invalid Name')
                
        except TclError:
            self.displayError('No item selected')
    
    '''
    #=======================================================#
    :GRADE:
    #=======================================================#
    '''
    
    def add_Grade(self):
        try:
            top = tk.Toplevel()
            top.title('Input')
            Input = WindowRemove('Grade: ',top)
            Input.mainloop()
            top.destroy()
            
            
            index = self.gList.curselection()
            IDs = self.EreadID(self.eList.get(index))
            studentID = int(IDs[0])
            disciplineID = int(IDs[1])
                    
            if not Input.getvar(str(Input.Input1)) == None:    
                gradeValue = Input.getvar(str(Input.Input1))
                gradeValue = float(gradeValue)
                
                Valid().grade(gradeValue)
                
                self._gradeControl.addGrade(grade(disciplineID,studentID),gradeValue)
                
                self._gradeControl.create(grade(disciplineID,studentID), gradeValue)
            
                self.refreshALL()
                
        except ValueError:
            self.displayError('Invalid Input')
        
        except NameError:
            self.displayError('Invalid Name')
    
        except TclError:
            self.displayError('No item selected')
            
    '''
    #================================================#  
    :SEARCH:
    #================================================#
    '''         
    def SearchALL(self):
        
      
        top = tk.Toplevel()
        top.title('Input')
        Input = WindowRemove('Search: ',top)
        Input.mainloop()    
        top.destroy()
        
        searchString = Input.getvar(str(Input.Input1))
        
        top = tk.Toplevel()
        top.title('Serch Results')
        top.text = Listbox(top)
        top.text.grid(row = 0, column = 0)
        top.text.config(width = 50)
        
        top.text.insert(END,'Disciplines:')
        for discipline in self._disciplineControl.getCurentRepo().getDisciplines():
            if searchString.lower() in str(discipline.getId()).lower() or str(discipline.getId()).lower() in searchString.lower() or searchString.lower() in discipline.getName().lower() or discipline.getName().lower() in searchString.lower():
                top.text.insert(END, discipline) 
        
        top.text.insert(END,'Students:')
        for student in self._studentControl.getCurentRepo().getStudents():
            if searchString.lower() in str(student.getId()).lower() or str(student.getId()).lower() in searchString.lower() or searchString.lower() in student.getName().lower() or student.getName().lower() in searchString.lower():
                top.text.insert(END, student)
            
    '''
    #===============================================#
    :STATISCTICS:
    #===============================================#
    '''
    def StudentEnrollA(self):
        
        try:
            
            top = tk.Toplevel()
            top.title('Enrollment List')
            top.text = Listbox(top)
            top.text.grid(row = 0, column = 0)
            
            index = self.dList.curselection()
            disciplineID = self.DreadID(self.dList.get(index))
            disciplineID = int(disciplineID)
    
            SList = self._enrolControl.studentEnrollA(disciplineID)
         
            for index in SList:
                top.text.insert(END,index)
    
            del SList[:]
            
        except TclError:
            top.destroy()
            self.displayError('No disicpline Selected')
    
    def StudentEnrollB(self):
        
        try:
            top = tk.Toplevel()
            top.title('Enrollment List')
            top.text = Listbox(top)
            top.text.grid(row = 0, column = 0)
                
            index = self.dList.curselection()
            disciplineID = self.DreadID(self.dList.get(index))
            disciplineID = int(disciplineID)
        
            SList = [[' ',-1]]
            for grade in self._gradeControl.getCurentRepo().getGrades():
                if grade.getDisciplineID() == disciplineID:
                    for student in self._studentControl.getCurentRepo().getStudents():
                        if student.getId() == grade.getStudentID():
                            if grade.getGrade() != []:
                                gradeAvg = self.listAvg(grade.getGrade(),grade.getGradeSize())
                                SList.append([student.getName(),gradeAvg])
            
            SList.sort(key=itemgetter(1),reverse = True)
            del SList[-1]                     
            for index in SList:
                top.text.insert(END,index)
            del SList[:]
          
        except TclError:
            top.destroy()
            self.displayError('No disicpline Selected')
    
        
    def FailingStudents(self):
        
        top = tk.Toplevel()
        top.title('Enrollment List')
        top.text = Listbox(top)
        top.text.grid(row = 0, column = 0)
        top.text.config(width = 50)
        
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
        
        
        for index in sList:
            top.text.insert(END,'\n'+index[0]+' - '+index[1])
        del sList[:]
    
    
    def BestStudents(self):
        
        top = tk.Toplevel()
        top.title('Enrollment List')
        top.text = Listbox(top)
        top.text.grid(row = 0, column = 0)
        top.text.config(width = 50)
        
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
        for index in range(1,len(sList)):
            top.text.insert(END,str(sList[index][0] + ' - ' + str(sList[index][1])))
        del sList[:]
        
    def DisciplineH(self):
        
        top = tk.Toplevel()
        top.title('Enrollment List')
        top.text = Listbox(top)
        top.text.grid(row = 0, column = 0)
        top.text.config(width = 50)
        
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

        for index in range(1,len(sList)):
            top.text.insert(END,'\n'+str(sList[index][0])+' - '+str(sList[index][1]))
        del sList[:]
    
    '''
    #======================================#
    :EDIT:
    #======================================#
    '''        
    def undo(self, event):
        
        self._undoControl.undo()
        self.refreshALL()
      
        
    def redo(self, event):
        
        self._undoControl.redo()
        self.refreshALL()
      
        
    '''
    #===========================================================================================#
    :Widgets:
    #===========================================================================================#
    '''
    
    def createWidgets(self):
        
      
        '''
        #==================================================#
        :TOPBAR:
        #==================================================#
        '''
        self.fileButton = Menubutton(self, text = 'File', relief = 'flat')
        self.fileButton.grid(row = 0, column = 0)
        
        self.fileButton.menu = Menu (self.fileButton, tearoff = 0)
        self.fileButton["menu"] = self.fileButton.menu
        
        self.fileButton.menu.add_command( label = "New", command = self.NewFile)
        self.fileButton.menu.add_command( label = "Exit", command = self.quit)
        
        self.eButton =  Menubutton(self, text="Enrollment", relief= 'flat' )
        self.eButton.grid(row = 0, column = 1)
        
        self.eButton.menu  =  Menu ( self.eButton, tearoff = 0 )
        self.eButton["menu"]  =  self.eButton.menu
    
        self.eButton.menu.add_command( label="Add Enrollment", command = self.add_Enroll)
        
        
        self.statButton = Menubutton(self, text="Statistics", relief= 'flat' )
        self.statButton.grid(row = 0, column = 2)
        
        self.statButton.menu  =  Menu ( self.statButton, tearoff = 0 )
        self.statButton["menu"]  =  self.statButton.menu
        
        self.discMenu = Menu(tearoff=0)
        self.discMenu.add_command(label="Sort by name", command = self.StudentEnrollA)
        self.discMenu.add_command(label="Sort by grade", command = self.StudentEnrollB)
        
        self.statButton.menu.add_cascade( label="Students Enrolled at disicpline", menu = self.discMenu)
        self.statButton.menu.add_command( label="Failing Students", command = self.FailingStudents)
        self.statButton.menu.add_command( label="Best Students", command = self.BestStudents)
        self.statButton.menu.add_command( label="Discipline Averages", command = self.DisciplineH)
        
        self.searchButton = Menubutton(self, text="Search", relief= 'flat' )
        self.searchButton.grid(row = 0, column = 3)
        
        self.searchButton.menu  =  Menu ( self.searchButton, tearoff = 0 )
        self.searchButton["menu"]  =  self.searchButton.menu
    
        self.searchButton.menu.add_command( label="Search", command = self.SearchALL)
        
        
        self.editButton = Menubutton(self, text="Edit", relief= 'flat' )
        self.editButton.grid(row = 0, column = 4)
        
        self.editButton.menu  =  Menu ( self.editButton, tearoff = 0 )
        self.editButton["menu"]  =  self.editButton.menu
    
        self.editButton.menu.add_command( label="Undo", command = self.undo)
        self.editButton.menu.add_command( label="Redo", command = self.redo)
        
        self.root.bind('<Control-z>',self.undo)
        self.root.bind('<Control-y>',self.redo)
        
        '''
        #===================================================#
        :Student:
        #===================================================#
        '''
        
        self.sbar = Label(self,text = 'Student list', fg = 'white', bg ='#3B9C9C', width =49)
        self.sbar.grid(row = 1, column =0, columnspan = 16)
        
        
        self.sList = Listbox(self,exportselection=0)
        for index in self._studentControl.getCurentRepo().getStudents():
            self.sList.insert(END,index)
        self.sList.grid(row = 2, column = 0, columnspan = 16)
        self.sList.config(width = 57, height = 40)
        
        
        self.sMenu = Menu(self, tearoff=0)
        self.sMenu.add_command(label="Add Student", command=self.add_Student)
        self.sMenu.add_command(label="Remove Student", command=self.remove_Student)
        self.sMenu.add_command(label='Update Student ID', command=self.update_StudentID)
        self.sMenu.add_command(label='Update Student name', command=self.update_StudentName)
        self.sMenu.add_command(label='Refresh', command=self.Srefresh)
        self.sList.bind("<Button-3>", self.sPopup)
                  
        
        '''
        #===================================================#
        :Discipline:
        #===================================================#
        '''
        self.dbar = Label(self,text = 'Discipline list', fg = 'white', bg ='#3B9C9C', width =49)
        self.dbar.grid(row = 1, column = 16, columnspan = 16)
        
        self.dList = Listbox(self,exportselection=0)
        for index in self._disciplineControl.getCurentRepo().getDisciplines():
            self.dList.insert(END,index)
        self.dList.grid(row = 2, column = 16, columnspan = 16)
        self.dList.config(width = 57, height = 40)
        
        
        self.dMenu = Menu(self, tearoff=0)
        self.dMenu.add_command(label="Add Discipline", command=self.add_Discipline)
        self.dMenu.add_command(label="Remove Discipline", command=self.remove_Discipline)
        self.dMenu.add_command(label='Update Discipline ID', command=self.update_DisciplineID)
        self.dMenu.add_command(label='Update Discipline name', command=self.update_DisciplineName)
        self.dMenu.add_command(label='Refresh', command=self.Drefresh)
        self.dList.bind("<Button-3>", self.dPopup)
        
        '''
        #===================================================#
        :Enroll:
        #===================================================#
        '''
        
        self.ebar = Label(self,text ='Enroll list', fg = 'white', bg ='#3B9C9C', width =49)
        self.ebar.grid(row = 1, column =32, columnspan = 16)
        
        self.eList = Listbox(self,exportselection=0)
        for index in self._enrolControl.getCurentRepo().getEnroll():
            self.eList.insert(END,'\n'+str(index))
        self.eList.grid(row = 2, column = 32, columnspan = 16)
        self.eList.config(width = 57, height = 40)
        
        self.eMenu = Menu(self, tearoff=0)
        self.eMenu.add_command(label="Remove Enrollment", command=self.remove_Enroll)
        self.eMenu.add_command(label="Grade Student", command=self.add_EnrollGrade)
        self.eMenu.add_command(label='Refresh', command=self.Erefresh)
        self.eList.bind("<Button-3>", self.ePopup)
        '''
        #===================================================#
        :Grade:
        #===================================================#
        '''
        self.gbar = Label(self,text = 'Grade list', fg = 'white', bg ='#3B9C9C', width =49)
        self.gbar.grid(row = 1, column = 48, columnspan = 16)
        
        self.gList = Listbox(self,exportselection=0)
        for index in self._gradeControl.getCurentRepo().getGrades():
            self.gList.insert(END,'\n'+str(index))
        self.gList.grid(row = 2, column = 48, columnspan = 16)
        self.gList.config(width = 57, height = 40)
        
        self.gMenu = Menu(self, tearoff=0)
        self.gMenu.add_command(label="Grade Student", command=self.add_Grade)
        self.gMenu.add_command(label='Refresh', command=self.Grefresh)
        self.gList.bind("<Button-3>", self.gPopup)
      
        
    def __init__(self,studentControl,disciplineControl,gradeControl,enrolControl, U1,  master=None):
        Frame.__init__(self, master)
        self.pack()
        self.grid()
        self.Max = 0
        self.oCont = 0
        self.root = master
        
        self._studentControl = studentControl
        self._disciplineControl = disciplineControl
        self._gradeControl = gradeControl
        self._enrolControl = enrolControl
        self._undoControl = U1
        
        
        self.createWidgets()
        
    @staticmethod
    def listAvg(myList,size):
        s = 0.0
        for index in range(size):
            s += myList[index]
        s /= size
        return s

class startGUI:
    
    def createWindow(self, C1, C2, C3, C4, U1):
            
        root = Tk()
        root.wm_title("Faculty")
        root.iconbitmap(default='C:\Users\user\Desktop\Uni\FP\Eclipse\Lab 5-7 Propper\sourceImages\ICON.ico')
        
        app = Application(C1, C2, C3, C4, U1, master = root)
        app.mainloop()
        root.destroy()

    
    def __init__(self, C1, C2, C3, C4, U1):
        self.createWindow(C1, C2, C3, C4, U1)
