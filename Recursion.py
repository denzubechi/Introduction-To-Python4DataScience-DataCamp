# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:58:27 2020

@author: Sah Meey
"""
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)




    


   