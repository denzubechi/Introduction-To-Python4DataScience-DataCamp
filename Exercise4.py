# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:52:56 2020

@author: Sah Meey
"""

number = input("Enter number: ")
digits_mapping = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine"
        }
output = ""
for character in number:
    output += digits_mapping.get(character, "!") + " "
print(output)
    