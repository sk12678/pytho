# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 22:25:26 2020

@author: user
"""


a1,a2,a3,a4 = eval(input("請輸入等差數列:"))
i = a2 -a1
u = a3 -a2
p = a4 -a3
if i ==u and u ==p:
    print(a4 +p)
    a5 = a4 +p
    print(a1,a2,a3,a4,a5)
else:
    print("false")

