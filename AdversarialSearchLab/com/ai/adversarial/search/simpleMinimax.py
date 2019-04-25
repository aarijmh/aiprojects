'''
Created on Mar 16, 2019

@author: dr.aarij
'''




class SimpleMinimax(object):
    '''
    classdocs
    '''


    def __init__(self, game, listeners = []):
        '''
        Constructor
        '''
        self._game = game
        self.listeners = listeners
        self._expandedNodes = 0
        self._duplicateStates = {}
    
    def minimax_decision(self,state):
        self._duplicateStates[str(state)] = state
        
        if self._game.terminalTest(state):
            return state._utility
        
        if state.isMax():
            return self.maxvalue(state)
        else:
            return self.minvalue(state)
    
    def minvalue(self,state):
        ss = str(state)
        if ss in self._duplicateStates and self._duplicateStates[ss]._utility > state._utility:
            return state._utility
        else:
            self._duplicateStates[str(state)] = state
            
        self._expandedNodes += 1
        
        retValue = 1000000000000
        
#         player = self._game.getPlayer(state)
        actions = self._game.getActions(state)
        
        for action in actions:
            tempValue = self.minimax_decision(self._game.getResult(state,action))
            if tempValue < retValue:
                retValue = tempValue    
                state._utility = retValue
                state._action = action
                   
        return retValue
            
    def maxvalue(self,state):
        
        ss = str(state)
        if ss in self._duplicateStates and self._duplicateStates[ss]._utility > state._utility:
            return state._utility
        else:
            self._duplicateStates[str(state)] = state
            
        self._expandedNodes += 1
        
        retValue = -1000000000000
        
#         player = self._game.getPlayer(state)
        actions = self._game.getActions(state)
        
        for action in actions:
            tempValue = self.minimax_decision(self._game.getResult(state,action))
            if tempValue > retValue:
                retValue = tempValue    
                state._utility = retValue
                state._action = action
        
        return retValue
    
