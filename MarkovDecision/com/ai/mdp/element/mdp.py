import sys
import random
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
    
    def policyEvaluation(self,policy,start_v,threshold):
        while True:
            delta = 0.0
            for s in range(len(self._states)):
                v = start_v[s]
                actionValue = 0
                possibleOutcomes = self._transition(s,policy[s])
                if len(possibleOutcomes) == 0:
                    actionValue = self._reward(s,policy[s],None)
                for sp, prob in possibleOutcomes:
                    actionValue += prob * (self._reward(s,policy[s],sp) + self._discount * start_v[sp])
                start_v[s] = actionValue
                delta = max(delta, abs(v - start_v[s]))
            if delta < threshold:
                break
    
    def policyIteration(self,threshold = 0.000000001):
        '''intialize the policy and values'''
        start_v = [random.random() * 100 for _ in self._states]
        start_policy = [random.randint(0,len(self._actions)-1) for _ in self._states] 
        
        
        while True:
            policy_stable = True
            self.policyEvaluation(start_policy, start_v, threshold)
            
            for s in range(len(self._states)):
                old_action = start_policy[s]
                maxValue = -sys.maxsize - 1                                
                for a in range(len(self._actions)):
                    actionValue = 0
                    possibleOutcomes = self._transition(s,a)                                            
                    for sp, prob in possibleOutcomes:
                        actionValue += prob * (self._reward(s,a,sp) + self._discount * start_v[sp])
                    if maxValue < actionValue:
                        maxValue = actionValue
                        start_policy[s] = a
                if old_action != start_policy[s]:
                    policy_stable = False
            if policy_stable:
                break
        
        return start_policy, start_v
           
        
            
        