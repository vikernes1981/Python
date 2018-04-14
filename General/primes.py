# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 18:03:37 2017

@author: penjo
"""



num = int(raw_input("Give number : "))
count = 0
for i in range(1,num + 1):
    for j in range(2,i):
        if i % j == 0:
            count == 1
            break;
    else:
        count == 0 and num != 1
        print("%d\n" %i)
        
x = 10**18
print(x)
