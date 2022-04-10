# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 22:51:10 2020

@author: Sah Meey
"""

weight = int(input("Enter your weight: "))
unit = input(" (L)bs or (K)g : ")
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} kilos")
else:
    coverted = weight // 0.45
    print(f"you are {converted} pounds")
    