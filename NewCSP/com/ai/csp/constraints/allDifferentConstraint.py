'''
Created on Mar 12, 2019

@author: Dr.aarij
'''

class AllDifferentConstraint(object):
    '''
    classdocs
    '''


    def __init__(self, variables = []):
        '''
        Constructor
        '''
        self._scope = variables
    
    def getScope(self):
        return self._scope
    
    def isConsistentWith(self,assignment):
        for i in range(0,len(self._scope) - 1):
            v = self._scope[i]
            if assignment.hasAssignmentFor(v):
                for j in range(i+1, len(self._scope)):
                    v2 = self._scope[j]
                    if assignment.hasAssignmentFor(v2):
                        if assignment.getAssignmentOfVariable(v) == assignment.getAssignmentOfVariable(v2):
                            return False
        return True