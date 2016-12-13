'''
Created on Dec 6, 2016

@author: Bendic
'''

__author__ = 'Bendic'

from Domain.Student import student
from Domain.Discipline import discipline
from Domain.StudentEnrolment import enroll
from Domain.Grade import grade

from Repositories.StudentRepo import studentRepository
from Repositories.DiscplineRepo import disciplineRepository
from Repositories.EnrollRepo import enrollRepository
from Repositories.GradeRepo import gradeRepository

from RepositoriesFile.StudentRepoFile import studentRepositoryFile
from RepositoriesFile.DisciplineRepoFile import disciplineRepositoryFile
from RepositoriesFile.EnrollRepoFile import enrollRepositoryFile
from RepositoriesFile.GradeRepoFile import gradeRepositoryFile

from RepositoriesBinary.StudentRepoBinary import studentRepositoryBinary
from RepositoriesBinary.DisciplineRepoBinary import disciplineRepositoryBinary
from RepositoriesBinary.EnrollRepoBinary import enrollRepositoryBinary
from RepositoriesBinary.GradeRepoBinary import gradeRepositoryBinary

from Tkconstants import GROOVE

from undoControllers.disciplineControllerUndo import disciplineControlWithUndo
from undoControllers.gradeControllerUndo import gradeControllerWithUndo
from undoControllers.studentControllerUndo import studentControlWithUndo
from undoControllers.enrollControllerUndo import enrollControllerWithUndo 


from undoControllers.undoController import UndoController

from UI.GUI import startGUI
from UI.Menu_UI import startCBM
import tkMessageBox

from Tkinter import Frame, Tk, StringVar, OptionMenu, Entry, Label, Button


class appStart(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.grid()
        
        self.sInput = StringVar()
        self.dInput = StringVar()
        self.eInput = StringVar()
        self.gInput = StringVar()
        
        self.createWidgets()
       
        
    def createWidgets(self):
        
        '''
        :SELECT1:
        '''
        self.selectLabel = Label(self, text = 'Select repo setting')
        self.selectLabel.grid(row = 0, column = 0)
        
        self.RepoList = ['Memory','File','Binary','Curent Setting']
        self.var1 = StringVar()
        self.drop = OptionMenu(self, self.var1, *self.RepoList)
        self.drop.grid(row = 0, column = 1)
        self.drop.config(width = 13)
        '''
        :Student:
        '''
        self.sLabel = Label(self, text = 'Student repo path')
        self.sLabel.grid(row = 2, column = 0)
        
        self.sPath = Entry(self, textvariable = self.sInput)
        self.sPath.grid(row = 2, column = 1)
        '''
        :Discipline:
        '''     
        self.sLabel = Label(self, text = 'Discipline repo path')
        self.sLabel.grid(row = 3, column = 0)
        
        self.sPath = Entry(self, textvariable = self.dInput)
        self.sPath.grid(row = 3, column = 1)
        '''
        :Enroll:
        '''
        self.sLabel = Label(self, text = 'Enroll repo path')
        self.sLabel.grid(row = 4, column = 0)
        
        self.sPath = Entry(self, textvariable = self.eInput)
        self.sPath.grid(row = 4, column = 1)
        '''
        :Grade:
        '''
        self.sLabel = Label(self, text = 'Grade repo path')
        self.sLabel.grid(row = 5, column = 0)
        
        self.sPath = Entry(self, textvariable = self.gInput)
        self.sPath.grid(row = 5, column = 1)
           
        '''
        :SELECT2:
        '''
        self.selectLabel = Label(self, text = 'Select UI type')
        self.selectLabel.grid(row = 1, column = 0)
        
        self.RepoList = ['CBM','GUI']
        self.var2 = StringVar()
        self.drop = OptionMenu(self, self.var2, *self.RepoList)
        self.drop.grid(row = 1, column = 1)
        self.drop.config(width = 13)
        
        '''
        :Submit:
        '''
        self.exit = Button(self, text = 'Exit', relief = GROOVE)
        self.exit.grid(row = 6, column = 0)
        self.exit.config(width = 17)
        self.exit['command'] = self.quit 
        
        self.submit = Button(self, text = 'Submit', relief = GROOVE)
        self.submit.grid(row = 6, column = 1)
        self.submit['command'] = self.quit 
        self.submit.config(width = 17)
        
        
class start:
    
    def displayError(self,msg):
        tkMessageBox.showerror('Error', msg)
        
    
    def reader(self):
        with open('C:\Users\user\Desktop\Uni\FP\Eclipse\Lab 5-7 Propper\MAIN\CONFIG','r') as eFile:
            line = eFile.readline()
            repoType = line[line.index('=') + 2:-1]
            
            line = eFile.readline()
            sPath = line[line.index('=') + 2:-1]
            
            line = eFile.readline()
            dPath = line[line.index('=') + 2:-1]
             
            line = eFile.readline()
            ePath = line[line.index('=') + 2:-1]
            
            line = eFile.readline()
            gPath = line[line.index('=') + 2:-1]
            
            line = eFile.readline()
            uiType = line[line.index('=') + 2:-1]
            
            return [repoType,sPath,dPath,ePath,gPath,uiType]
            
    
    
    def createMemoryControllers(self):
        
        sRepo = studentRepository()
        sRepo.addStudent(student(2,'Ion Pascu'))
        sRepo.addStudent(student(3,'Anrei Istoc'))
        sRepo.addStudent(student(4,'Maria Jiu'))
        sRepo.addStudent(student(5,'Camelia Danu'))
        sRepo.addStudent(student(6,'Ionut Frunza'))
        sRepo.addStudent(student(7,'Eleanor Popescu'))
        sRepo.addStudent(student(8,'Ana-Maria Biju'))
        sRepo.addStudent(student(9,'Dan Lautar'))
        sRepo.addStudent(student(10,'Maria Babos'))
        sRepo.addStudent(student(11,'Irina Mase'))
        sRepo.addStudent(student(12,'Estera Chelariu'))
        sRepo.addStudent(student(13,'Florin Andreescu'))
        sRepo.addStudent(student(14,'Bobes Bogdan'))
        sRepo.addStudent(student(15,'Victor Paul'))
        
        
        dRepo = disciplineRepository()
        dRepo.addDiscipline(discipline(2,'Analiza Lexicografica'))
        dRepo.addDiscipline(discipline(3,'Sport'))
        
        eRepo = enrollRepository()
        eRepo.addEnrolment(enroll(2,1))
        eRepo.addEnrolment(enroll(3,1))
        eRepo.addEnrolment(enroll(4,1))
        eRepo.addEnrolment(enroll(5,1))
        
        eRepo.addEnrolment(enroll(6,2))
        eRepo.addEnrolment(enroll(7,2))
        eRepo.addEnrolment(enroll(8,2))
        eRepo.addEnrolment(enroll(9,2))
        eRepo.addEnrolment(enroll(10,2))
        
        eRepo.addEnrolment(enroll(11,3))
        eRepo.addEnrolment(enroll(12,3))
        eRepo.addEnrolment(enroll(13,3))
        eRepo.addEnrolment(enroll(14,3))
        eRepo.addEnrolment(enroll(15,3))
        
        gRepo = gradeRepository()
        gRepo.addGrade(grade(1,1),10)
        gRepo.addGrade(grade(1,2),6.5)
        gRepo.addGrade(grade(1,3),4.3)
        gRepo.addGrade(grade(1,4),2.3)
        gRepo.addGrade(grade(1,5),6)
        
        gRepo.addGrade(grade(2,6),7)
        gRepo.addGrade(grade(2,7),7)
        gRepo.addGrade(grade(2,8),7)
        gRepo.addGrade(grade(2,9),7)
        gRepo.addGrade(grade(2,10),7)
        
        gRepo.addGrade(grade(3,11),7)
        gRepo.addGrade(grade(3,12),7)
        gRepo.addGrade(grade(3,13),7)
        gRepo.addGrade(grade(3,14),7)
        gRepo.addGrade(grade(3,15),7)
        
        
        E = enrollControllerWithUndo(eRepo, self._undoController)
        G = gradeControllerWithUndo(gRepo, self._undoController)
        S = studentControlWithUndo(sRepo, E, G, self._undoController)
        D = disciplineControlWithUndo(dRepo, E, G, self._undoController)
        
        return [S,D,E,G]
    
    def createWindow(self):
        
        root = Tk() 
        root.wm_title("Config")
        root.iconbitmap(default='C:\Users\user\Desktop\Uni\FP\Eclipse\Lab 5-7 Propper\sourceImages\ICON.ico')
        self.app = appStart(master = root)
        self.app.mainloop()
        root.destroy()
    
    def generateControllers(self):
        
        try:
            repoType = self.app.getvar(str(self.app.var1))
            uiType = self.app.getvar(str(self.app.var2))
            
            sPath = self.app.getvar(str(self.app.sInput))
            dPath = self.app.getvar(str(self.app.dInput))
            ePath = self.app.getvar(str(self.app.eInput))
            gPath = self.app.getvar(str(self.app.gInput))
            
            
            if repoType == '':
                raise ValueError
            
            if repoType == 'Curent Setting':
                cnfList = self.reader()
                
                repoType = cnfList[0]
                sPath = cnfList[1]
                dPath = cnfList[2]
                ePath = cnfList[3]
                gPath = cnfList[4]
                uiType = cnfList[5] 
            
            if repoType == 'Memory':
                cList = self.createMemoryControllers()
                S = cList[0]
                D = cList[1]
                E = cList[2]
                G = cList[3]
            
            elif repoType == 'File':
            
                E = enrollControllerWithUndo(enrollRepositoryFile(ePath), self._undoController)
                G = gradeControllerWithUndo(gradeRepositoryFile(gPath), self._undoController)  
                S = studentControlWithUndo(studentRepositoryFile(sPath), E, G, self._undoController)
                D = disciplineControlWithUndo(disciplineRepositoryFile(dPath), E, G, self._undoController)
                
            elif repoType == 'Binary':
             
                E = enrollControllerWithUndo(enrollRepositoryBinary(ePath), self._undoController)
                G = gradeControllerWithUndo(gradeRepositoryBinary(gPath), self._undoController)
                S = studentControlWithUndo(studentRepositoryBinary(sPath), E, G, self._undoController)
                D = disciplineControlWithUndo(disciplineRepositoryBinary(dPath), E, G, self._undoController)
                
            if uiType == 'GUI':
                startGUI(S, D, G, E,self._undoController)
                
            if uiType == 'CBM':
                startCBM(S, D, G, E, self._undoController)
                
                    
        except IOError:
            self.displayError('One ore more paths are invalid')
            self.createWindow()
            self.generateControllers()
        
        except ValueError:
            self.displayError('One ore more paths are invalid')
            self.createWindow()
            self.generateControllers()
        
        except UnboundLocalError:
            self.displayError('Config file error')
            self.createWindow()
            self.generateControllers()
         
    def __init__(self, UndoController):
        self._undoController = UndoController
        self.createWindow()
        self.generateControllers()
        
        
start(UndoController())
        