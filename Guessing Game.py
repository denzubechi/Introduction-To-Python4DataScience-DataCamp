# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 23:08:28 2020

@author: Sah Meey
"""


Secret_number= 9
Guess_Count = 0
Guess_limit = 3
while Guess_Count < Guess_limit:
    value = int(input("Guess: "))
    Guess_Count +=1
    if value == Secret_number:
        print("You Won! ")
        break
else:
    print("You lose! ")
        
    