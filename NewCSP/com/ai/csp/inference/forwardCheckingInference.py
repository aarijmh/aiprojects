'''
Created on Mar 6, 2019

@author: dr.aarij
'''
from com.ai.csp.assignment.assignment import Assignment

class ForwardCheckingInference(object):
    '''
    classdocs
    '''


    def __init__(self):pass
    
    def doInference(self,inferenceInfo,csp,variable,value):
        assignment = Assignment()
        assignment.addVariableToAssignment(variable, value)        
        for con in csp.getConstraints(variable):
            otherVariables = csp.getNeighbour(variable,con)
            for ov in otherVariables:
                someValues = []
                changed = False
                domVals = inferenceInfo.getDomainsOfAffectedVariables(ov)
                if domVals is None:
                    domVals = csp.getDomainValues(ov)
                    
                for domVal in domVals:
                    assignment.addVariableToAssignment(ov, domVal)
                    if not con.isConsistentWith(assignment):
                        changed = True
                    else:
                        someValues.append(domVal)
                
                if changed:
                    inferenceInfo.addToAffectedVariables(ov,someValues)
                    
                assignment.removeVariableFromAssignment(ov)
        return []        