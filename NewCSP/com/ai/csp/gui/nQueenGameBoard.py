'''
Created on Mar 9, 2019

@author: dr.aarij
'''


from tkinter import Canvas, Frame,  PhotoImage


from com.ai.csp.constraints.notAttackingConstraint import NotAttackingConstraint
from com.ai.csp.csp import CSP
from com.ai.csp.elements.variable import Variable


class NQueenGameBoard(Frame):
    def __init__(self, parent, rows=8, columns=8, size=64, color1="white", color2="blue", n=8):
        '''size is the size of a square, in pixels'''

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}
        self.adjustedPieces = {}
        self.n = n

        canvas_width = columns * size
        canvas_height = rows * size

        Frame.__init__(self, parent)
        self.canvas = Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
#         self.canvas.bind("<Configure>", self.refresh)

    def addpiece(self, name, image, row=0, column=0):
        '''Add a piece to the playing board'''
        self.adjustedPieces[str(row),"_",str(column)]=(row,column)
        self.canvas.create_image(0,0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
        '''Place a piece at the given row/column'''
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

    def refresh(self):
        '''Redraw the board, possibly in response to window being resized'''
#         xsize = int((event.width-1) / self.columns)
#         ysize = int((event.height-1) / self.rows)
#         self.size = min(xsize, ysize)
        self.canvas.delete("square")
        self.canvas.delete("piece")
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
        for name in self.pieces:
            x1 = (self.pieces[name][0] * self.size) + 5
            y1 = (self.pieces[name][1] * self.size) + 5
            x2 = x1 + self.size - 10
            y2 = y1 + self.size - 10
            self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="green", tags="square")
            self.otherConstraints(self.pieces[name][0],self.pieces[name][1])
            
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
            self.canvas.tag_raise(name)
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")
    
    def otherConstraints(self,row,column):
        for i in range(self.columns):
            s = str(row),"_",str(i)
            if s not in self.adjustedPieces:
                x1 = (row * self.size) + 5
                y1 = (i * self.size) + 5
                x2 = x1 + self.size - 10
                y2 = y1 + self.size - 10
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="indianred", tags="square")
                
        for i in range(self.columns):
            s = str(i),"_",str(column)
            if s not in self.adjustedPieces:
                x1 = (i * self.size) + 5
                y1 = (column * self.size) + 5
                x2 = x1 + self.size - 10
                y2 = y1 + self.size - 10
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="indianred", tags="square")
                
        i = row
        j = column        
        while i < self.columns:
            i += 1
            j += 1
            s = str(i),"_",str(j)
            if s not in self.adjustedPieces:
                x1 = (i * self.size) + 5
                y1 = (j * self.size) + 5
                x2 = x1 + self.size - 10
                y2 = y1 + self.size - 10
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="indianred", tags="square")
        
        i = row
        j = column        
        while i >= 0 and j >= 0:
            i -= 1
            j -= 1
            s = str(i),"_",str(j)
            if s not in self.adjustedPieces:
                x1 = (i * self.size) + 5
                y1 = (j * self.size) + 5
                x2 = x1 + self.size - 10
                y2 = y1 + self.size - 10
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="indianred", tags="square")
                
        i = row
        j = column        
        while i >= 0 and j < self.columns:
            i -= 1
            j += 1
            s = str(i),"_",str(j)
            if s not in self.adjustedPieces:
                x1 = (i * self.size) + 5
                y1 = (j * self.size) + 5
                x2 = x1 + self.size - 10
                y2 = y1 + self.size - 10
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="indianred", tags="square")
        i = row
        j = column        
        while i < self.columns and j >= 0:
            i += 1
            j -= 1
            s = str(i),"_",str(j)
            if s not in self.adjustedPieces:
                x1 = (i * self.size) + 5
                y1 = (j * self.size) + 5
                x2 = x1 + self.size - 10
                y2 = y1 + self.size - 10
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="indianred", tags="square")                 

          
    def createCSP(self):
        variables = []
        domains = []
        constraints = []
        for i in range(self.n):
            variables.append(Variable("Q_%d"%(i+1)))
        for i in range(1,self.n+1):
            domains.append(i)
        for i in range(self.n-1):
            for j in range(i+1,self.n):
                constraints.append(NotAttackingConstraint(variables[i] , variables[j]))
        return CSP(variables,domains,constraints)

    def handleFireChange(self,csp,assignment):
            self.pieces = {}
            self.adjustedPieces = {}
            for vari in assignment._variables:
                col = int(vari._name.split("_")[1])
                self.addpiece(vari._name, PhotoImage(data=imagedata),col-1, assignment.getAssignmentOfVariable(vari)-1 )            
            self.refresh()
# image comes from the silk icon set which is under a Creative Commons
# license. For more information see http://www.famfamfam.com/lab/icons/silk/
imagedata = '''
    R0lGODlhEAAQAOeSAKx7Fqx8F61/G62CILCJKriIHM+HALKNMNCIANKKANOMALuRK7WOVLWPV9eR
    ANiSANuXAN2ZAN6aAN+bAOCcAOKeANCjKOShANKnK+imAOyrAN6qSNaxPfCwAOKyJOKyJvKyANW0
    R/S1APW2APW3APa4APe5APm7APm8APq8AO28Ke29LO2/LO2/L+7BM+7BNO6+Re7CMu7BOe7DNPHA
    P+/FOO/FO+jGS+/FQO/GO/DHPOjBdfDIPPDJQPDISPDKQPDKRPDIUPHLQ/HLRerMV/HMR/LNSOvH
    fvLOS/rNP/LPTvLOVe/LdfPRUfPRU/PSU/LPaPPTVPPUVfTUVvLPe/LScPTWWfTXW/TXXPTXX/XY
    Xu/SkvXZYPfVdfXaY/TYcfXaZPXaZvbWfvTYe/XbbvHWl/bdaPbeavvadffea/bebvffbfbdfPvb
    e/fgb/Pam/fgcvfgePTbnfbcl/bfivfjdvfjePbemfjelPXeoPjkePbfmvffnvbfofjlgffjkvfh
    nvjio/nnhvfjovjmlvzlmvrmpvrrmfzpp/zqq/vqr/zssvvvp/vvqfvvuPvvuvvwvfzzwP//////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    ////////////////////////////////////////////////////////////////////////////
    /////////////////////////////////////////////////////yH+FUNyZWF0ZWQgd2l0aCBU
    aGUgR0lNUAAh+QQBCgD/ACwAAAAAEAAQAAAIzAD/CRxIsKDBfydMlBhxcGAKNIkgPTLUpcPBJIUa
    +VEThswfPDQKokB0yE4aMFiiOPnCJ8PAE20Y6VnTQMsUBkWAjKFyQaCJRYLcmOFipYmRHzV89Kkg
    kESkOme8XHmCREiOGC/2TBAowhGcAyGkKBnCwwKAFnciCAShKA4RAhyK9MAQwIMMOQ8EdhBDKMuN
    BQMEFPigAsoRBQM1BGLjRIiOGSxWBCmToCCMOXSW2HCBo8qWDQcvMMkzCNCbHQga/qMgAYIDBQZU
    yxYYEAA7
'''

