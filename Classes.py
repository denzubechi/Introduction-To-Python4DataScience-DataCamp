# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:33:44 2020

@author: Sah Meey
"""

#We use classes to define new types to model real concepts e.g a shopping cart.
#We define a class by using the class keyword.
# We name starting with a capital letter(pascal naming convention)
#An object is an instance of a class
#A class simply defines the blueprint or template of creating objects

class Piont:
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")
        

#Creating an object
piont1 =  Piont()
piont1.x = 20
piont1.y = 50
print(piont1.x)
piont1.draw()   

point2 = Piont()
try:
    print(point2.x)
except AttributeError:
    print("'Piont' object has no attribute 'x'")
