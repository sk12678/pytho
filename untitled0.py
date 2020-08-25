# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:01:43 2020

@author: andy6
"""


x = int(input("最大數"))
y = int(input("最小數"))
for z in range(y , x):
    z = z+1
    if z % 2 ==0:
        print(z)


x = int(input("最大數"))
y = int(input("最小數"))
z = y
while z in range(y,x):
    z = z +1
    if z % 2 == 0:
        print(z)
