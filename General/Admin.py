# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 19:42:28 2017

@author: penjo
"""
adminName = raw_input("Give Admin Name : ")
adminPass = raw_input("Give Admin Pass : ")
clear = "\n" * 10
print(clear)

for i in range(3):
    
    userName = raw_input("Give User Name : ")
    userPass = raw_input("Give User Pass : ")
    
    if (userName == adminName) and (userPass == adminPass):
        print("You are in!!")
        print(clear)
    elif (userName != adminName) and (userPass == adminPass):
        print("Wrong User Name.")
        print(clear)
    elif (userName == adminName) and (userPass != adminPass):
        print("Wrong User Pass.")
        print(clear)
    else:
        print("Everything is wrong!")
        print(clear)