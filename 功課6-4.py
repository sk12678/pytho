# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 21:36:30 2020

@author: user
"""



a,b,c = eval(input("請輸入三邊長:"))
if(c>=b) and (c>=a):
    if(c<b+a):
        print(c+b+a)
elif(a>=b) and(a>=c):
    if(a<b+c):
        print(c+b+a)
elif(b>=a) and(b>=c):
    if(b<a+c):
        print(a+b+c)
False==print("無法組成三角形")
  
