'''
Created on Mar 6, 2019

@author: dr.aarij
'''
from com.ai.csp.elements.constraint import Constraint

class NotAttackingConstraint(Constraint):
    '''
    classdocs
    '''


    def __init__(self, var1, var2):
        '''
        Constructor
        '''
        self._scope = [var1,var2]
    
    def getScope(self):
        return self._scope
    
    def isConsistentWith(self,assignment):
        val1 = assignment.getAssignmentOfVariable(self._scope[0])
        val2 = assignment.getAssignmentOfVariable(self._scope[1])
        return val1 == None or val2 == None or self.checkAttack(val1,val2)
    
    def checkAttack(self,val1,val2):
        
        if val1 == val2:
            return False
        
        pos1 = int(self._scope[0]._name.split("_")[1])
        pos2 = int(self._scope[1]._name.split("_")[1])
        
        if abs(val2 - val1) == abs(pos2 - pos1):
            return False
         
        
        return True