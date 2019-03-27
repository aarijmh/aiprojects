'''
Created on Mar 9, 2019

@author: dr.aarij
'''
import logging
import threading
import time
from tkinter import Tk, Frame, Label, Entry, Button

# def consumer(cond):
#     """wait for the condition and use the resource"""
#     logging.debug('Starting consumer thread')
#     with cond:
#         cond.wait()
#         logging.debug('Resource is available to consumer')
# 
# 
# def producer(cond):
#     """set up the resource to be used by the consumer"""
#     logging.debug('Starting producer thread')
#     with cond:
#         logging.debug('Making resource available')
#         cond.notifyAll()
# 
# 
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s (%(threadName)-2s) %(message)s',
# )
# 
# condition = threading.Condition()
# 
# c1 = threading.Thread(name='c1', target=consumer,
#                       args=(condition,))
# c2 = threading.Thread(name='c2', target=consumer,
#                       args=(condition,))
# p = threading.Thread(name='p', target=producer,
#                      args=(condition,))
# 
# c1.start()
# time.sleep(0.2)
# c2.start()
# time.sleep(0.2)
# p.start()


class TestGUI(object):
    def __init__(self): 
        self.initGUI()

        
    def initGUI(self):
        root = Tk()
        board = Frame(root,width=100,height=100)
        board.grid(row=0,column=0)
        
        
        self.lbl = Label(root,text="",width=30)
        self.lbl.grid(row=1,column=0) 
        self.lbl.config(text='change the value')
        
        root.mainloop()
    def changeNumber(self,n):
        self.lbl.config(text=str(n))

def generateNumber(lbl,cond):
    with cond:
        for i in range(20000):
            lbl.config(text=str(i))
            cond.wait()
 

if __name__=="__main__":
    
    cond = threading.Condition()
    
    root = Tk()
    board = Frame(root,width=100,height=100)
    board.grid(row=0,column=0)
        
    def callback(event): 
        with cond:
            print("OK")
            cond.notifyAll()
    
    def callback2(event): 
        with cond:
            print("OK")
            c1 = threading.Thread(name='c1', target=generateNumber,args=(lbl,cond,))
            c1.start()
            
    
    lbl = Label(root,text="",width=30)
    lbl.grid(row=1,column=0) 
    lbl.config(text='change the value')
    
    btn = Button(root,text="OK")
    btn.grid(row=2,column=0)
    btn.bind("<Button-1>", callback)
    
    btn2 = Button(root,text="Start")
    btn2.grid(row=3,column=0)
    btn2.bind("<Button-1>", callback2)
    
    root.mainloop()
        
#     generateNumber(t)