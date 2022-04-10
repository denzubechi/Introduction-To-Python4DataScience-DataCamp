# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:19:18 2020

@author: Sah Meey
"""
#We use "try except" blocks to handle errors in python
#An exception is a kind of error that crashes a program

try:
    age = int(input("Enter Age: "))
    income = 20000
    rist = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print("invalid value")

