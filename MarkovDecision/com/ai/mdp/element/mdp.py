import sys
class MDP(object):
    
    def __init__(self,states,actions,transition,reward,discount=0.5):
        self._states = states
        self._actions = actions
        self._transition = transition
        self._reward = reward
        self._discount = discount
        self._initial_v = [ 0 for _ in states]
        self._initial_q = [[0 for _ in actions] for _ in states]
        
    def valueIteration(self,iterations = 0,threshold = 0.000000001):
        previousMatrix = self._initial_v
        returnQMatrix = [[0 for _ in self._actions] for _ in self._states]
        
        delta = 0.0
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
                    returnQMatrix[s][a] = actionValue
                    maxValue = max(maxValue,actionValue)
                returnMatrix[s] = maxValue
                delta = max(delta, abs(previousMatrix[s] - returnMatrix[s]))
            previousMatrix = returnMatrix
            if delta < threshold:
                break
                        
        return previousMatrix, returnQMatrix