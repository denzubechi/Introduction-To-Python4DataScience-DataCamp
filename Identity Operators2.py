# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 22:17:08 2020

@author: Sah Meey
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content



# to demonstrate the difference betweeen "is not" and "<>": this comparison returns False because x is equal to y
