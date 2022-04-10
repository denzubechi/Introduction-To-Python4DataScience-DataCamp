# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 22:48:31 2020

@author: Sah Meey
"""

#Converting from json to python
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)