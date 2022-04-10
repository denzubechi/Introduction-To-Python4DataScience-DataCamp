# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 13:39:15 2020

@author: Sah Meey
"""

#Dictionary is used to store a bunch of key value pairs 
#n we use curly braces to define a dictionary{}
#nb: each key should be unique in a dictionary
# we access each item in the dictionary using square brackets
customer = {
        "name": "Samuel Nzubechi",
        "age": 17,
        "is verified": True
        }
customer["age"] = 16
print(customer["name"])
print(customer.get("age"))
print(customer.get("birthday"))
print(customer.get("birthday", "8th of November 2003"))