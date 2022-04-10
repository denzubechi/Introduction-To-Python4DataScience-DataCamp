# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:21:41 2020

@author: Sah Meey
"""

class Mammal:
    def walk(self):
        print("Walk")
         
        
class Dog(Mammal):
    def Bark(self):
        print("Bark")
    

class Cat(Mammal):
    def can_be_annoying(self):
        print("Can be annoying")
    
    
dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.can_be_annoying()
