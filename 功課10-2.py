# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:43:15 2020

@author: andy6
"""




a = "Q"
e = True
grades = {}
while e == True:
    x = input("請輸入姓名")
    y = float(input("請輸入成績"))
    grades[x] = y
    z = input("離開請按Q")
    if z == a:
        e = False
print(grades)



















