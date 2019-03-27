'''
Created on Mar 12, 2019

@author: Dr.aarij
'''
from tkinter import Tk
from com.ai.csp.gui.menuBoard import MenuBoard
from com.ai.csp.gui.bottomRowBoard import BottomRowBoard
import threading
import time
from com.ai.csp.inference.simpleInference import SimpleInference
from com.ai.csp.inference.forwardCheckingInference import ForwardCheckingInference
from com.ai.csp.strategy.backtrackingSearch import BactrackingSearch
from com.ai.csp.gui.nQueenGameBoard import NQueenGameBoard
from com.ai.csp.inference.arcConsistencyInference import ArcConsistencyInference
from com.ai.csp.gui.cspGameBoard import CSPGameBoard

class GuiHandler(object):
    '''
    classdocs
    '''


    def __init__(self):
            self.root = Tk()

    
    def initializeCSPGUI(self,board):
            self.board = board
            self.board.grid(row=0,column=0)
    #         player1 = PhotoImage(data=imagedata)
    #         self.board.addpiece("player1", player1, 0,0)
            
            self.frm = MenuBoard(self.root)
            self.frm.grid(row=0,column=1)
            
            self.frm2 = BottomRowBoard(self.root)
            self.frm2.grid(row=1,column=0,columnspan=2,sticky="w",padx=15,pady=10)
            
            self.frm2.nextButton.bind('<Button-1>',self.nextHandler)
            self.frm2.playButton.bind('<Button-1>',self.playHandler)
            self.frm2.pauseButton.bind('<Button-1>',self.pauseHandler)
            
    
            self.nextFlag = False
            self.play = False
            self.pause = False
            
            self.condition = threading.Condition()
            
            self.started = False
            
            def on_closing():            
    #             self.c1.shutdown_flag.set()
                self.root.destroy()
            
            self.root.protocol("WM_DELETE_WINDOW", on_closing)
            self.root.mainloop()
            
    def fireChange(self,csp,assignment):
        with self.condition:
            if self.nextFlag or self.pause:
                self.condition.wait()
            elif self.play:
                time.sleep(float(self.frm.speedEntry.get()))
            print(assignment)
            self.board.handleFireChange(csp,assignment)
            
    def startIt(self):
        self.started = True
        variableOrdering = False
        valueOrdering = False
        
        
        if self.frm.ordering.get() == 2:
            variableOrdering = True
        elif self.frm.ordering.get() == 3:
            variableOrdering = True
            valueOrdering = True
            
        if self.frm.filtering.get() == 1:
            self.inPro = SimpleInference()
        elif self.frm.filtering.get() == 2:
            self.inPro = ForwardCheckingInference()
        elif self.frm.filtering.get() == 3:
            self.inPro = ArcConsistencyInference()
        
        self.csp = self.board.createCSP()
        self.bts = BactrackingSearch(self.inPro,[self],variableOrdering,valueOrdering)
        
        self.c1 = threading.Thread(name='c1', target=self.bts.solve, args=(self.csp,))
        self.c1.start()
    
    def nextHandler(self,_):
        self.nextFlag = True
        if not self.started:            
            self.startIt()
        if self.pause:
            self.pause = False            
        with self.condition:
            self.condition.notifyAll()
            
    def playHandler(self,_):
        with self.condition:
            self.play = True
            
            if not self.started:            
                self.startIt()
            if self.pause:
                self.pause = False
                self.condition.notifyAll() 
            if self.nextFlag:
                self.nextFlag = False
                self.condition.notifyAll()            

    def pauseHandler(self,_):
        self.pause = True
        self.play = False
        self.nextFlag = False
        
if __name__ == "__main__":
    bd = GuiHandler()
    csp = NQueenGameBoard(bd.root)
    csp = CSPGameBoard(bd.root)
    bd.initializeCSPGUI(csp)
    