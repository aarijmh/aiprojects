'''
Created on Mar 25, 2019

@author: Aarij Mahmood
'''

class TictactoePlayer(object):
    '''
    classdocs
    '''


    def __init__(self, name, symbol):
        self._name = name
        self._symbol = symbol
        self._moves = [] 
        
    def __str__(self, *args, **kwargs):
        return str(self._name)+"_"+str(self._sybmbol)