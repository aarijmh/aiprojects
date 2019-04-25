'''
Created on Apr 25, 2019

@author: dr.aarij
'''
from com.ai.adversarial.elements.game import Game
from com.ai.adversarial.sample.brickgame.brickplayer import BrickPlayer
from com.ai.adversarial.sample.brickgame.brickline import BrickLine
from com.ai.adversarial.sample.brickgame.brickgamestate import BrickGameState
from com.ai.adversarial.search.simpleMinimax import SimpleMinimax

class BrickGame(Game):
    '''
    classdocs
    '''


    def __init__(self, row=3,col=3,move=0):
        self._row = row
        self._col = col
        self._move = move
        self._agents =[ BrickPlayer("Player","blue"),
                       BrickPlayer("Opponent","red")]
        self._board = {}
        self._lines = 0
        
        for i in range(self._row):
            for j in range(self._col - 1):
                self._board["%d-%d-%d-%d"%(i,j,i,j+1)] = BrickLine(i, j, i, j+1,True)
                if i + 1 < self._row:
                    self._board["%d-%d-%d-%d"%(i, j, i+1, j)] = BrickLine(i, j, i+1, j,False)
            if i + 1 < self._row:
                self._board["%d-%d-%d-%d"%(i, self._col - 1, i+1, self._col - 1)] = BrickLine(i, self._col - 1, i+1, self._col - 1,False)
        
    def getInitialState(self):
        return BrickGameState(self._board,self._move)
    
    def getPlayer(self,state):
        return self._agents[state._move]
    
    def getActions(self,state):      
        return [br for br in state._board.values() if br._player == None]
    
    def _checkHorizontalBox(self,state,bl):
        count = 0
        if bl._startX - 1 >= 0 and bl._endX - 1 >= 0 :
            if state._board["%d-%d-%d-%d"%(bl._startX-1,bl._startY,bl._startX,bl._startY)]._player != None and\
            state._board["%d-%d-%d-%d"%(bl._endX-1,bl._endY,bl._endX,bl._endY)]._player != None and\
            state._board["%d-%d-%d-%d"%(bl._startX-1,bl._startY,bl._endX-1,bl._endY)]._player != None:
                count += 1
        
        if bl._startX + 1 < self._row and bl._endX + 1 < self._row:
            if state._board["%d-%d-%d-%d"%(bl._startX,bl._startY,bl._startX+1,bl._startY)]._player != None and\
            state._board["%d-%d-%d-%d"%(bl._endX,bl._endY,bl._endX+1,bl._endY)]._player != None and\
            state._board["%d-%d-%d-%d"%(bl._startX+1,bl._startY,bl._endX+1,bl._endY)]._player != None:
                count += 1
        
        return count
    
    def _checkVerticalBox(self,state,bl):
        count = 0
        if bl._startY - 1 >= 0 and bl._endY - 1 >= 0 :
            if state._board["%d-%d-%d-%d"%(bl._startX,bl._startY-1,bl._endX,bl._endY - 1)]._player != None and\
            state._board["%d-%d-%d-%d"%(bl._startX,bl._startY-1,bl._startX,bl._startY)]._player != None and\
            state._board["%d-%d-%d-%d"%(bl._endX,bl._endY-1,bl._endX,bl._endY)]._player != None:
                count += 1
        
        if bl._startY + 1 < self._col and bl._endY + 1 < self._col:
            if state._board["%d-%d-%d-%d"%(bl._startX,bl._startY+1,bl._endX,bl._endY + 1)]._player != None and\
            state._board["%d-%d-%d-%d"%(bl._startX,bl._startY,bl._startX,bl._startY + 1)]._player != None and\
            state._board["%d-%d-%d-%d"%(bl._endX,bl._endY,bl._endX,bl._endY + 1)]._player != None:
                count += 1
        
        return count
    
    def getResult(self, state, action):
        newState = state.copy()
        player = self.getPlayer(state)
        bl = newState._board['%d-%d-%d-%d'%(action._startX,action._startY,action._endX,action._endY)]
        
        bl._player = player
        
        increaseBox = 0
        
        if bl._horizontal:
            increaseBox += self._checkHorizontalBox(newState, bl)
        else:
            increaseBox += self._checkVerticalBox(newState, bl)
        
        if increaseBox > 0:
            for tempbl in newState._board.values():
                if tempbl._player == None:                    
                    if tempbl._horizontal:
                        tempbl._player = player
                        count = self._checkHorizontalBox(newState, tempbl)
                        if count == 0:
                            tempbl._player = None
                        else:
                            increaseBox += count
                    else:
                        tempbl._player = player
                        count = self._checkVerticalBox(newState, tempbl)
                        if count == 0:
                            tempbl._player = None
                        else:
                            increaseBox += count     
        
        if newState._move == 0:
            newState._playerbox += increaseBox
        else:
            newState._opponentbox += increaseBox
            
        newState._move = (newState._move + 1) % 2
        
        newState.updateUtility()
        return newState                
    
    def terminalTest(self,state):
        for bl in state._board.values():
            if bl._player == None: return False
        return True
    
    def utility(self,state,player): 
        return state._utility
    
    def getAgentCount(self):
        return 2


if __name__ == "__main__":
    game = BrickGame(row=3,col=3)
    minimax = SimpleMinimax(game)
    initialState = game.getInitialState()
    minimax.minimax_decision(initialState)
    
    print(initialState)                          