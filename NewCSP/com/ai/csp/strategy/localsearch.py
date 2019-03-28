'''
Created on Mar 6, 2019

@author: dr.aarij
'''
from com.ai.csp.strategy.searchStrategy import SearchStrategy
from com.ai.csp.assignment.assignment import Assignment
from com.ai.csp.inference.inferenceInfo import InferenceInfo
import math
import random


class LocalSearch(SearchStrategy):
    '''
    classdocs
    '''


    def __init__(self, inferenceProcdeure,listeners = [],variableOrdering=False,valueOrdering=False,maxSteps = 100000):
        '''
        Constructor
        '''
        SearchStrategy.__init__(self, listeners)
        self._inferenceProcedure = inferenceProcdeure
        self._variableOrdering = variableOrdering
        self._valueOrdering = valueOrdering
        self._maxSteps = maxSteps
        
    def intiliazeRandomly(self,csp):
        self._assignment = Assignment()
        domainLength = len(csp.getListOfDomains())
        for va in csp.getVariables():
            self._assignment.addVariableToAssignment(va, csp.getListOfDomains()[random.randint(0,domainLength-1)])
    
    def solve(self,csp):
        self.intiliazeRandomly(csp)
        
        for _ in range(self._maxSteps):
            if self._assignment.isSolution(csp):
                return self._assignment
            cands = self.getConflictedVariable(csp)
            var = cands[random.randint(0,len(cands)-1)]
            val = self.getMinConflictValueFor(var,csp)
#             print(str(var)+"_"+str(val)+"__"+str(len(cands)))
            self.fireListeners(csp, self._assignment)
            self._assignment.addVariableToAssignment(var,val)
            
        return False
    
    def getConflictedVariable(self,csp):
        resultVariables = []
        
        for con in csp.getListOfConstraints():
            if not self._assignment.isConsistent([con]):
                for var in con.getScope():
                    if var not in resultVariables:
                        resultVariables.append(var)
        
        return resultVariables
    
    def getMinConflictValueFor(self,var,csp):
        
        constraints = csp.getConstraints(var)
        assignment = self._assignment.returnCopy()
        minConflict = 100000000000
        candidates = []
        
        for val in csp.getDomainValues(var):
            assignment.addVariableToAssignment(var,val)
            count = 0
            for con in constraints:
                if assignment.isConsistent([con]):
                    count+=1
            if count <= minConflict:
                if count < minConflict:
                    candidates = []
                    count = minConflict
                candidates.append(val)
                
        return candidates[random.randint(0,len(candidates)-1)]
    
    def fireListeners(self,csp,assignment):
        for listener in self._listeners:
            listener.fireChange(csp,assignment)