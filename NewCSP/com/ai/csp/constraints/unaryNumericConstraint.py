'''
Created on Mar 12, 2019

@author: Dr.aarij
'''

class UnaryNumericConstraint(object):
    '''
    classdocs
    '''


    def __init__(self, var1, equality, value):
        '''
        Constructor
        '''
        self._scope = [var1]
        self.equality = equality
        self.value = int(value)
    
    def getScope(self):
        return self._scope
    
    def isConsistentWith(self,assignment):
        val1 = int(assignment.getAssignmentOfVariable(self._scope[0]))
        if self.equality.lower() == "eq":
            return val1 == self.value
        if self.equality.lower() == "lt":
            return val1 > self.value
        if self.equality.lower() == "lte":
            return val1 >= self.value
        if self.equality.lower() == "gt":
            return val1 < self.value
        if self.equality.lower() == "gte":
            return val1 <= self.value
        return False