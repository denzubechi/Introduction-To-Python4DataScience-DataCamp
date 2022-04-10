# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 12:16:46 2020

@author: Sah Meey
"""

command = ""
started = False
stop = False

while command != "quit":
    command = input("> ").lower()
    if command == "start":
        stop = False
        if not started:
            print("Car started")
            started = True
        else:
            print("Car started already!")
    elif command == "help":
        print("""
Start - Starts the car
Stop - Stops the car
Quit - quits the program            
                """)
    elif command == "stop":
        started = False
        if not stop:
           print("Car stopped")
           stop = True
        else:
            print("Car stopped already!")
    elif command == "quit":
        break
    else:
        print("Sorry.. I dont understand")
    
