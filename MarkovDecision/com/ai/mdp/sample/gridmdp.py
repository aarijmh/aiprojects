'''
Created on Apr 18, 2019

@author: dr.aarij
'''
from _io import open
from com.ai.mdp.element.mdp import MDP

class GridMDP(object):
    '''
    classdocs
    '''


    def __init__(self, file, noise=0.2,livingReward = 0.0):
        self._livingReward = livingReward
        self._noise = noise
        self._states = []
        self._actions = [(-1,0),(1,0),(0,-1),(0,1)]
        self.readFile(file)
    
    
    def readFile(self,file):
        f = open(file,"+r")
        lines = f.readlines()
        
        self._rows = int(lines[0])
        self._columns = int(lines[1])
        
        for i in range(2, len(lines)):
            self._states += [int(x) for x in lines[i].split(" ")]
        
#         print(self._states)
    
    def transition(self,state,action):
        returnStates = []
        
        if self._states[state] == 2:
            return returnStates
        
        if self._states[state] == 3 or self._states[state] == 4:
            return returnStates
        
        stateRow = int (state / self._columns)
        stateColumn = state % self._columns
        
        possibleActions = [ (self._actions[action][0],self._actions[action][1],1-self._noise),
                           ((self._actions[action][0]**2 + 1)%2,(self._actions[action][1]**2 + 1)%2,self._noise/2.0),
                           ( ((self._actions[action][0]**2 + 1)%2)*-1, ((self._actions[action][1]**2 + 1)%2)*-1,self._noise/2.0)]
        
        for pa in possibleActions:            
            if stateRow + pa[0] >= 0 and\
                stateRow + pa[0] < self._rows and\
                stateColumn + pa[1] >= 0 and\
                stateColumn + pa[1] < self._columns and\
                self._states[int((stateRow + pa[0]) * self._columns + (stateColumn + pa[1]))] != 2:
                
                returnStates.append(((stateRow + pa[0]) * self._columns + (stateColumn + pa[1]),pa[2]))
            else:
                returnStates.append((state,pa[2]))                        
        
        return returnStates
    
    def reward(self,s,a,sp):
        if self._states[s] == 3:
            return 1.0
        if self._states[s] == 4:
            return -1.0        
        return self._livingReward
        

if __name__ == "__main__":
    grid = GridMDP("grid.txt",livingReward=-2.0)
    mdp = MDP(grid._states, grid._actions, grid.transition, grid.reward, .9)
    v = mdp.policyIteration() 
    print(v[0])
    print(v[1])

        