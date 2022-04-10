# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:41:26 2020

@author: Sah Meey
"""

name = input("Enter your name: ")
if len(name) < 5:
    print("Name must be at least 3 characters")
elif len(name) >10:
    print("Nmae must be at most 10 characters")
else:
    print("You are welcome "+ name)