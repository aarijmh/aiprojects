'''
Created on Mar 9, 2019

@author: dr.aarij
'''


from tkinter import Canvas, Frame



from com.ai.csp.csp import CSP
from com.ai.csp.elements.variable import Variable
from com.ai.csp.constraints.unaryNumericConstraint import UnaryNumericConstraint
from com.ai.csp.constraints.allDifferentConstraint import AllDifferentConstraint


class CSPGameBoard(Frame):
    def __init__(self, parent, size=64, color1="white", color2="white"):
        '''size is the size of a square, in pixels'''

        self.rows = 9
        self.columns = 9
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}
        self.adjustedPieces = {}

        canvas_width = self.columns * size
        canvas_height = self.rows * size

        Frame.__init__(self, parent)
        self.canvas = Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
#         self.canvas.bind("<Configure>", self.refresh)



    def refresh(self):
        '''Redraw the board, possibly in response to window being resized'''
#         xsize = int((event.width-1) / self.columns)
#         ysize = int((event.height-1) / self.rows)
#         self.size = min(xsize, ysize)
        self.canvas.delete("square")
        self.canvas.delete("piece")
        self.canvas.delete("text")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
                val = self.assignment.getAssignmentOfVariable(self.csp.getVariables()[row * 9 + col])
                
                if val == None:
                    val = self.csp.getDomainValues(self.csp.getVariables()[row * 9 + col])                
                self.canvas.create_text(x1+30, y1+20,fill="darkblue", tags="text",width=50,font="Times 8 italic bold",text=val)
                
        self.canvas.tag_raise("text")
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")
    
              
    def createCSP(self):
        
        variables = []
        domains = [1,2,3,4,5,6,7,8,9]
        constraints = []
        rowName ='ABCDEFGHI'
        colName ='123456789'
        
        V = [
        0, 0, 0, 2, 6, 0, 7, 0, 1,
        6, 8, 0, 0, 7, 0, 0, 9, 0,
        1, 9, 0, 0, 0, 4, 5, 0, 0,
        8, 2, 0, 1, 0, 0, 0, 4, 0,
        0, 0, 4, 6, 0, 2, 9, 0, 0,
        0, 5, 0, 0, 0, 3, 0, 2, 8,
        0, 0, 9, 3, 0, 0, 0, 7, 4,
        0, 4, 0, 0, 5, 0, 0, 3, 6,
        7, 0, 3, 0, 1, 8, 0, 0, 0
        ]
        unaryMap = {}
        for i in range(0,9):
            for j in range(0,9):
                varname = rowName[i]+colName[j]
                var1 = Variable(varname)
                variables.append(var1)
                if V[i * 9 + j] != 0:
                    unaryMap[var1] = V[i * 9 + j]
                
        for i in range(0,9):
            rowVars = []
            colVars = []
            for j in range(0,9):
                rowVars.append(variables[i*9 + j])
                colVars.append(variables[i + j*9])
            constraints.append(AllDifferentConstraint(rowVars))
            constraints.append(AllDifferentConstraint(colVars))
            
        for i in range(0,9):
            rowRange = int(i/3) * 3
            colRange = (i*3)%9
            varbs = []
            for row in range(rowRange, rowRange+3):
                for col in range(colRange,colRange+3):
                    varbs.append(variables[row*9 + col])
            constraints.append(AllDifferentConstraint(varbs))


        self.csp = CSP(variables,domains,constraints)
        
        for var,value in unaryMap.items():
            self.csp.addVariableDomain(var,[value])
        
        return self.csp

    def handleFireChange(self,csp,assignment):
        self.csp = csp
        self.assignment = assignment
        self.refresh()


