# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 20:59:16 2020

@author: Sah Meey
"""

Course = "Python, for Beginners"
Split = Course.split(",")
print(len(Course))
print(Course.upper())
print(Course.lower())
print(Course.find('y'))
print(Course.find('Y'))
print(Course.replace('Beginners', 'Absolute Beginners'))
print(Course.replace('P', 'J'))
print('Python' in Course)
print('python' in Course)
print(Split)
