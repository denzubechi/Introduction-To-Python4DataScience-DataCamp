# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 22:19:29 2020

@author: Sah Meey
"""
Guess_Count = 0
Guess_limit = 3
while Guess_Count < Guess_limit:
    password = input("Enter password? ")
    Guess_Count +=1
    if "banana" in password.lower():
        print("Welcome")
        break
    elif "apple" in password.lower():
        print("Welcome")
        break
    else:
        print("Password wrong")
else:
    print("Try again Later")
    



# returns True because a sequence with the value "banana" is in the list
