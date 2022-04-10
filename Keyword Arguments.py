# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:51:08 2020

@author: Sah Meey
"""

def greet_user(first_name, Last_name):
    print(f"Hi {first_name} {Last_name} ")
    print("Welcome aboard")

print("Start")
greet_user("Samuel", Last_name = "Chukwuma")
#Last_name= "Samuel" is a keyword argument.
#Nb you should always use positional argument
greet_user("Sah Meey", "Nzubechi")
print("Finish")   