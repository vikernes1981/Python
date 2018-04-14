# -*- coding: utf-8 -*-
"""
Created on Mon May  8 20:09:35 2017

@author: penjo
"""

from random import randrange

num = randrange(0,100)
flag = 0
counter = 0
lamp_state = 0
prisoners = []

for i in range(100):
    prisoners.append(i)
    prisoners[i] = 0
    
while counter < 100:
    
    if ((prisoners[num] == prisoners[0]) and (flag == 0)):
        flag = 1
        counter += 1
        lamp_state = 1
        prisoners[0] = 2
    
    elif ((prisoners[num] == 2) and (flag == 1)):
        
        if lamp_state == 0:
            lamp_state = 1
            counter += 1
    
    elif ((prisoners[num] != 2) and (prisoners[num] == 0)):
        lamp_state = 0
        prisoners[num] = 1
    
print("I'm running freeee...!!!")
