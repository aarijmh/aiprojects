'''
Created on Apr 25, 2019

@author: dr.aarij
'''

class BrickPlayer(object):
    '''
    classdocs
    '''


    def __init__(self, name, color):
        self._name = name
        self._color = color
        self._moves = [] 
        
    def __str__(self):
        return str(self._name)+"_"+str(self._color)