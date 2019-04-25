'''
Created on Apr 25, 2019

@author: dr.aarij
'''
from copy import deepcopy

class BrickGameState(object):
    '''
    classdocs
    '''


    def __init__(self, board,move,playerbox=0,opponentbox=0):
        self._board = board
        self._move = move
        self._playerbox = playerbox
        self._opponentbox = opponentbox
        self._utility = playerbox - opponentbox
        self._action = None
        
    def copy(self):
        return BrickGameState(deepcopy(self._board),self._move,self._playerbox,self._opponentbox)
    
    def __str__(self):
        return str(self._board)+"_"+str(self._move)
    
    def isMax(self):
        return self._move == 0
    
    def isNextAgentMax(self):
        return (self._move + 1) % 2 == 0
    
    def getAction(self):
        return self._action
    
    def updateUtility(self):
        self._utility = self._playerbox - self._opponentbox
    
