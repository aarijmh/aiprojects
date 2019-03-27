'''
Created on Mar 12, 2019

@author: Dr.aarij
'''
from tkinter import Frame, Button

class BottomRowBoard(Frame):
    def __init__(self, parent):
        '''size is the size of a square, in pixels'''

        Frame.__init__(self, parent)
        self.setUpMenu();

    def setUpMenu(self):
        self.resetButton = Button(self,text="Reset")
        self.resetButton.grid(row= 0, column=0,padx=15,pady=10)
        self.previousButton = Button(self,text="Prev")
        self.previousButton.grid(row= 0, column=1,padx=15,pady=10)
        self.pauseButton = Button(self,text="Pause")
        self.pauseButton.grid(row= 0, column=2,padx=15,pady=10)
        self.nextButton = Button(self,text="Next")
        self.nextButton.grid(row= 0, column=3,padx=15,pady=10)
        self.playButton = Button(self,text="Play")
        self.playButton.grid(row= 0, column=4,padx=15,pady=10)
        self.fastButton = Button(self,text="Fast")
        self.fastButton.grid(row= 0, column=5,padx=15,pady=10)