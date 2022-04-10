# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:22:59 2020

@author: Sah Meey
"""

numbers = [2, 2, 4, 6, 3, 1, 6, 4]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)