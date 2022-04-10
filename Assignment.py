# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:58:27 2020

@author: Sah Meey
"""
User = str(input("Enter username: "))
Password = input("Please enter Pin: ")
print("Password Saved.")

#While loop
Time = 1
while Time < 20:
   logout = str(input("Do you want to log out? [y/n]: "))
   if logout == "y": 
       logged_out = print("Logged out")   
       Count = 1
       while Count < 4:
           Login = input("Enter password to login: ")
           Count += 1
           if Login == Password: 
               print("User Logged in")
               break
           else:
               print("Wrong Password")
          
       break
       
   elif logout == "n":
       print("Still logged in")
         
   else:
       print("Wrong answer")
   Time += 1
   



    


   