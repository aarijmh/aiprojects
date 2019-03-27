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
        assignment = Assignment()
        assignment.addVariableToAssignment(variable, value)        
        for con in csp.getConstraints(variable):
            otherVariables = csp.getNeighbour(variable,con)
            for ov in otherVariables:
                someValues = []
                changed = False
                for domVal in csp.getDomainValues(ov):
                    assignment.addVariableToAssignment(ov, domVal)
                    if not con.isConsistentWith(assignment):
                        changed = True
                    else:
                        someValues.append(domVal)
                
                if changed:
                    inferenceInfo.getAffectedVariables().append((ov,someValues))
                assignment.removeVariableFromAssignment(ov)
        return [] 