'''
Created on Mar 12, 2019

@author: Dr.aarij
'''
from tkinter import Frame, Label, StringVar, OptionMenu, IntVar, Radiobutton,\
    Entry

class MenuBoard(Frame):
    def __init__(self, parent):
        '''size is the size of a square, in pixels'''

        Frame.__init__(self, parent)
        self.setUpMenu();

    def setUpMenu(self):
        lbl = Label(self, text="Algorithms", font=("Helvetica", 16))
        lbl.grid(row=0,column=0,columnspan=2,sticky="w")
        
        Label(self, text="   ").grid(row=1,column=0)
        self.algorithm = StringVar(self)
        self.algorithm.set("Backtracking") # default value
        

        w = OptionMenu(self, self.algorithm, "DFS", "Backtracking")
        w.grid(row=1,column=1)
        
        Label(self, text=" ", font=("Helvetica", 16)).grid(row=2,column=0,columnspan=2)
        Label(self, text="Ordering", font=("Helvetica", 16)).grid(row=3,column=0,columnspan=2,sticky="w")

        self.ordering = IntVar(self)
        self.ordering.set(1)  # initializing the choice, i.e. Python

        orderOptions = [
            ("None",1),
            ("MRV",2),
            ("MRV with LCV",3),
        ]
        
        def ShowChoice():
            print(self.ordering.get())
            
        row = 5
        
        for nm,val in orderOptions:
            Radiobutton(self,text=nm,  variable=self.ordering, command=ShowChoice, value=val).grid(row=row,column=1,sticky="w")
            row = row + 1
        
        Label(self, text=" ", font=("Helvetica", 16)).grid(row=row,column=0,columnspan=2)
        row = row + 1
        Label(self, text="Filtering", font=("Helvetica", 16)).grid(row=row,column=0,columnspan=2,sticky="w")
        row = row + 1
        
        self.filtering = IntVar(self)
        self.filtering.set(1)
        
        filterOptions = [
            ("None",1),
            ("Forward Checking",2),
            ("Arc Consistency",3),
        ]
        
        def ShowChoiceFiltering():
            print(self.filtering.get())
            
        
        for nm,val in filterOptions:
            Radiobutton(self,text=nm,  variable=self.filtering, command=ShowChoiceFiltering, value=val).grid(row=row,column=1,sticky="w")
            row = row + 1
            
        Label(self, text=" ", font=("Helvetica", 16)).grid(row=row,column=0,columnspan=2)
        row = row + 1
        Label(self, text="Board Options", font=("Helvetica", 16)).grid(row=row,column=0,columnspan=2,sticky="w")
        row = row + 1
        
        self.boardType = IntVar(self)
        self.boardType.set(1)
        
        boardOptions = [
            ("Show Board",1),
            ("Show Domain",2)
        ]
        
        def ShowChoiceBoard():
            print(self.boardType.get())
            
        
        for nm,val in boardOptions:
            Radiobutton(self,text=nm,  variable=self.boardType, command=ShowChoiceBoard, value=val).grid(row=row,column=1,sticky="w")
            row = row + 1
        
        Label(self, text="Speed (in seconds)", font=("Helvetica", 12)).grid(row=row,column=0,columnspan=2,sticky="w")
        row = row + 1
        self.speedEntry = Entry(self,text="0.005",width=10)
        self.speedEntry.insert(0, ".005")
        self.speedEntry.grid(row=row,column=1)      