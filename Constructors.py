# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:51:22 2020

@author: Sah Meey
"""
#init is short for initialize
# It is used to construct or create an object..
#Nb: int is not callable

class Point:
    def __init__(self, x, y): #The function gets called when a new Point object is created
        #Initializing objects..
        self.x = x
        self.y = y
        
    def move(self):
        print("Move")
        
    def draw(self):
        print("Draw")
        
point = Point(20, 30)
point.x = 11
print(point.x)
print(point.y)
point.draw()