'''
Created on Mar 25, 2019

@author: dr.aarij
'''
from com.ai.adversarial.sample.tictactoe.tictactoeState import TictactoeState
from com.ai.adversarial.sample.tictactoe.tictactoePlayer import TictactoePlayer
from com.ai.adversarial.elements.game import Game
from com.ai.adversarial.search.simpleMinimax import SimpleMinimax

class TicTacToeGame(Game):
    '''
    classdocs
    '''


    def __init__(self, move = 0):
        self._board = [[0,0,0],[0,0,0],[0,0,0]]
        self._move = move
        self._agents =[ TictactoePlayer("Player","X"),
                       TictactoePlayer("Opponent","O")]
        
        self._winningPositions = [[(0,0),(0,1),(0,2)],
                                  [(1,0),(1,1),(1,2)],
                                  [(2,0),(2,1),(2,2)],
                                  [(0,0),(1,0),(2,0)],
                                  [(0,1),(1,1),(2,1)],
                                  [(0,2),(1,2),(2,2)],
                                  [(0,0),(1,1),(2,2)],
                                  [(2,0),(1,1),(0,2)]]
        
    def getInitialState(self):
        return TictactoeState(self._board,self._move)
    
    def getPlayer(self,state):
        return self._agents[state._move]
    
    def getActions(self,state):
        actions = []
        
        for i in range(3):
            for j in range(3):
                if state._board[i][j] == 0:
                    actions.append((i,j))
                
        
        return actions
    
    def getResult(self, state, action):
        newState = state.copy()
        player = self.getPlayer(state)
        
        newState._board[action[0]][action[1]] = player._symbol
        newState._move = (newState._move + 1) % 2 
        
        winposfound = True
        for pos in self._winningPositions:
            winposfound = True
            for indpos in pos:
                if newState._board[indpos[0]][indpos[1]] != player._symbol:
                    winposfound = False
                    break
            if winposfound:
                break 
        
        if winposfound:
            newState._move = -1
            if player._symbol == "X":
                newState._utility = 1
            else:
                newState._utility = -1
        else:
            zeroFound = False
            for i in range(3):
                for j in range(3):
                    if newState._board[i][j] == 0:
                        zeroFound = True
                        break
                if zeroFound:
                    break
            if not zeroFound:
                newState._move = -1
                newState._utility = 0     
        return newState
    
    def terminalTest(self,state):
        return state._move == -1

    def utility(self,state,player): 
        return state._utility
    
    def getAgentCount(self):
        return 2
    
if __name__ == "__main__":
    game = TicTacToeGame()
    minimax = SimpleMinimax(game)
    initialState = game.getInitialState()
    minimax.minimax_decision(initialState)
    
    print(initialState)    