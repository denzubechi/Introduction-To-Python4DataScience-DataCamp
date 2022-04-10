# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 12:01:20 2020

@author: Sah Meey
"""

name = input("Enter username: ")
types = int

if len(name) < 3:
    print("Name must be at least three characters long")
elif len(name) > 50:
    print("name can be maximum of fifty Characters")
else:
    print("name looks Good")
