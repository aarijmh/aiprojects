'''
Created on Mar 26, 2019

@author: Dr.aarij
'''
from tkinter.ttk import Frame
from tkinter import Canvas, Tk, Button, Label, Radiobutton, IntVar
from com.ai.adversarial.sample.tictactoe.tictactoeGame import TicTacToeGame
import sys
import threading
import time
from tkinter.constants import LEFT
from com.ai.adversarial.search.simpleMinimax import SimpleMinimax

class TictactoeGUI(Frame):
    '''
    classdocs
    '''


    def __init__(self, parent,screenHeight=300, screenWidth=300):
        '''
        Constructor
        '''
        Frame.__init__(self, parent)
        self.screenHeight = screenHeight
        self.screenWidth = screenWidth
        
        self.canvas = Canvas(self, borderwidth=0, highlightthickness=0,
                                width=self.screenWidth, height=self.screenHeight, background="bisque")
        self.canvas.grid(row=0,column=0)
        self.refresh()
        
    def refresh(self):
        self.canvas.delete("pieces")
        self.canvas.delete("boxes")
                
        self.boxwidth = int(self.screenWidth / 3)
        self.boxheight = int(self.screenHeight / 3)
            
        for row in range(3):
            for col in range(3):
                x1 = (col * self.boxwidth)
                y1 = (row * self.boxheight)
                x2 = x1 + self.boxwidth
                y2 = y1 + self.boxheight
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white", tags="boxes")
        
        self.canvas.tag_raise("pieces")
        self.canvas.tag_lower("boxes")
        
    def drawState(self,state):
        self.canvas.delete("pieces")
        for row in range(3):
            for col in range(3):
                x1 = (col * self.boxwidth)
                y1 = (row * self.boxheight)
                x2 = x1 + self.boxwidth
                y2 = y1 + self.boxheight
                if state._board[row][col] == "X":
                    self.canvas.create_line(x1,y1,x2,y2, fill="red", tags="pieces")
                    self.canvas.create_line(x2,y1,x1,y2, fill="red", tags="pieces")
                elif state._board[row][col] == "O":
                    self.canvas.create_oval(x1, y1, x2, y2, outline="red", tags="pieces")
                    
class GuiHandler(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.root = Tk()
        self.game = TicTacToeGame()
        sys.setrecursionlimit(10000) 
        self.minimax = SimpleMinimax(self.game)
        self.started = False
        self.initializeGui()
        
    def initializeGui(self):
        self.board = TictactoeGUI(self.root)
        self.state = self.game.getInitialState()
        self.board.drawState(self.state)
        self.board.grid(row=0,column = 0,rowspan=5)
        self.btn = Button(self.root, text="Play game")
        self.btn.grid(row=0,column = 1)
    
        self.btn.bind('<Button-1>',self.nextHandler)
        
        self.rb = IntVar()
        Label(self.root, text="Select move ordering: ", justify = LEFT,padx = 20).grid(row=1,column = 1)
        Radiobutton(self.root,text="Move first",padx = 20,variable=self.rb,value=1, justify = LEFT).grid(row=2,column = 1)
        Radiobutton(self.root,text="Move Second",padx = 20,variable=self.rb,value=2, justify = LEFT).grid(row=3,column = 1)
        Radiobutton(self.root,text="Autoplay",padx = 20,variable=self.rb,value=3, justify = LEFT).grid(row=4,column = 1)
        
        self.board.canvas.bind("<Button-1>", self.movePlayer)
        
        
    
        self.lb = Label(self.root,text="Algorithms", font=("Helvetica", 16))
        self.lb.grid(row=6, column=0,sticky="w")
    
        self.root.mainloop()
        
    def movePlayer(self,event):
        if self.started:
            row = int(event.y / 100)
            col = int(event.x / 100)
            self.state._board[row][col] = "O"
            self.board.drawState(self.state)
            self.state._move = 0
            self.minimax.minimax_decision(self.state)
            
#             self.state = st            
            if self.state == None:
                self.lb['text'] = 'Game drawn'
                return                 
            elif self.state._move == -1:
                if self.state._utility == -1:
                    self.lb['text'] = 'Player Won'
                elif  self.state._utility == 1:
                    self.lb['text'] = 'Computer Won'
            else:
                self.state._board[self.state._action[0]][self.state._action[1]] = 'X'
                self.state._move = 1
            self.board.drawState(self.state)
            self.state._utility = 0
        
    def nextHandler(self,_):
        if self.rb.get() != 0:
            self.started = True
        if self.rb.get() == 3:
            threading.Thread(name='c1', target=self.runAlgos, ).start()
        
    def runAlgos(self):
        while self.state._move != -1:
            fun = None
            lmb = None
            retValue = 0
            if self.state._move == 0:
                fun = self.minimax.minvalue
                lmb = lambda a,b: a >= b
                retValue = -1000000000000
            else:
                fun = self.minimax.maxvalue
                lmb = lambda a,b: a <= b
                retValue = 1000000000000
            self.minimax.minimax_decision(self.state)
#             print(action, valu, st)
#             self.state = st
            self.state._utility = 0
            self.board.drawState(self.state)
            self.lb['text'] = str(self.state._utility)
            time.sleep(.1)
            
if __name__ == "__main__":
    GuiHandler()        