# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 17:53:58 2017

@author: penjo
"""

name = raw_input("Name? : ")
surname = raw_input("Surname? : ")
age = int(raw_input("Age? : "))
gender = raw_input("Gender? : ")

if gender == 'm':
    print("Your name is %s %s!" %(name,surname))
    
    if age > 18:
        print("You are %d years old.You HAVE to join the Army!" %age)

elif gender == 'f':
    print("Hello there beautiful!!!")