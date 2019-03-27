'''
Created on Mar 12, 2019

@author: Dr.aarij
'''
from com.ai.csp.assignment.assignment import Assignment

class ArcConsistencyInference(object):
    '''
    classdocs
    '''


    def __init__(self):pass
    
    def doInference(self,inferenceInfo,csp,variable,value):
        self.assignment = Assignment()
        self.assignment.addVariableToAssignment(variable, value)
        
        self.varToC = variable
        self.valToC = value
        
        queue = csp.getConstraints(variable)
        pairs = []
        
        for q in queue:
            if len(q.getScope()) == 2:
                obj = [q.getScope()[1],q.getScope()[0],q]
                pairs.append(obj)
        
        while len(pairs) > 0:
            constraint = pairs[0][2]
            if self.revise(csp, pairs[0][0], pairs[0][1], constraint):
                if len(csp.getDomainValues(pairs[0][0])) == 0:
                    return None
                                    
                for con in csp.getNeighboursOfVariableExcept(pairs[0][0],pairs[0][1]):
                    if con.getScope()[0]._name == variable._name or con.getScope()[1]._name == variable._name:
                        continue
                    if con.getScope()[0]._name == pairs[0][0]._name:
                        pairs.append([con.getScope()[1],con.getScope()[0],con])
                    else:
                        pairs.append([con.getScope()[0],con.getScope()[1],con])
            del pairs[0]
        return []
    
    def revise(self,csp,var1,var2,constraint):
        revised = False
        dv2Values = [] 
        
        assignment = Assignment()
        assignment.addVariableToAssignment(self.varToC, self.valToC)
        
        if assignment.hasAssignmentFor(var2):
            dv2Values.append(self.assignment.getAssignmentOfVariable(var2))
        else:
            dv2Values = csp.getDomainValues(var2)

        for dv1 in csp.getDomainValues(var1):            
            for dv2 in dv2Values:
                if not assignment.hasAssignmentFor(var1):               
                    assignment.addVariableToAssignment(var1, dv1)
                assignment.addVariableToAssignment(var1, dv1)
                if not assignment.isConsistent([constraint]):
                    csp.removeValueFromDomain(var1,dv1)
                    revised = True                
        return revised
                