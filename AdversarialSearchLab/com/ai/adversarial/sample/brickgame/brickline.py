'''
Created on Apr 25, 2019

@author: dr.aarij
'''

class BrickLine(object):
    '''
    classdocs
    '''


    def __init__(self, row1,col1,row2,col2,horizontal,player=None):
        self._startX = row1
        self._startY = col1
        self._endX = row2
        self._endY = col2
        self._horizontal = horizontal
        self._player = player
    
    def __eq__(self, other):
        if isinstance(other, BrickLine):
            if self._startX == other._startX and\
            self._startY == other._startY and\
            self._endX == other._endX and\
            self._endY == other._endY:
                return True
        return False
    
    def __hash__(self, *args, **kwargs):
        return hash(str(self))
    
    def __str__(self):
        return "(%d,%d) -- (%d,%d) : %s"%(self._startX,self._startY,self._endX,self._endY,str(self._player)) 