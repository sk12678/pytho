# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 21:42:50 2020

@author: andy6
"""

a = []
x = int(input("輸入數字"))
y = int(input("輸入數字"))
for z in range(1,y):
    if x % z == 0:
        if y % z == 0:
            a.append(z)
print(a)
print(a[-1:])

            
            
    









