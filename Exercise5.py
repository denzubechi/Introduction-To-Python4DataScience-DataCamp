# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:03:46 2020

@author: Sah Meey
"""

class Definition:
    def __init__(self, name):
        #Initializing objects....
        self.name = name
    
    def talk(self):
        print(f'{Samuel.name} says "I will be great!" ')


Samuel = Definition("Chukwuma Samuel")
Samuel.talk()

Samuel = Definition("Samuel Nzubechi")
Samuel.talk()