# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:50:13 2017

@author: penjo
"""

name = raw_input("Name? : ")
surname = raw_input("Surname? : ")
count = 0

while count < 5:
    
    num1 = int(raw_input("Give 1st number : "))
    num2 = int(raw_input("Give 2nd number : "))
    
    summary = num1 * num2    
    answer = int(raw_input("What is the total of num1 multiplied by num 2? : "))
    
    if answer == summary:
        
        count += 1
        
if count == 5:
    print("Perases Mr/Ms %s %s!!" %(name, surname))