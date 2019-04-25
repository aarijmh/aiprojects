'''
Created on Mar 16, 2019

@author: dr.aarij
'''
from abc import abstractmethod

class Game(object):
    '''
    classdocs
    '''

    @abstractmethod
    def __init__(self, params): pass
    
    @abstractmethod
    def getInitialState(self):pass
    
    @abstractmethod
    def getPlayer(self,state):pass
    
    @abstractmethod
    def getActions(self,state): pass
    
    @abstractmethod
    def getResult(self, state, action): pass
    
    @abstractmethod
    def terminalTest(self,state): pass
    
    @abstractmethod
    def utility(self,state,player): pass
    
    @abstractmethod
    def getAgentCount(self): pass