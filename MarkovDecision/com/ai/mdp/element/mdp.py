from copy import deepcopy
import sys
class MDP(object):
    
    def __init__(self,states,actions,transition,reward,discount=0.5):
        self._states = states
        self._actions = actions
        self._transition = transition
        self._reward = reward
        self._discount = discount
        self._intitial_v = [ 0 for _ in states]
        self._intitial_q = [[0 for _ in states] for _ in actions]
        
    def valueIteration(self,initial_v,iterations = 0):
        previousMatrix = deepcopy(initial_v)
                        
        for _ in range(iterations):
            returnMatrix = [ 0 for _ in self._states]
            for s in range(len(self._states)):
                maxValue = -sys.maxsize - 1
                for a in range(len(self._actions)):
                    actionValue = 0
                    possibleOutcomes = self._transition(s,a)
                    if len(possibleOutcomes) == 0:
                        maxValue = self._reward(s,a,None)
                        continue
                    for sp, prob in possibleOutcomes:
                        actionValue += prob * (self._reward(s,a,sp) + self._discount * previousMatrix[sp])
                    maxValue = max(maxValue,actionValue)
                returnMatrix[s] = maxValue
            previousMatrix = returnMatrix
                        
        return previousMatrix