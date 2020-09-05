# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 23:20:58 2020

@author: andy6
"""



e = True
a = {"大雄":"台南市西門路五段十巷二十號","胖虎":"台南市中清路一段一巷一號"}
while e == True:
    b = int(input("1:新增,2:編輯,3:刪除,4:結束"))
    if b == 1:
        c = input("輸入人")
        d = input("輸入住址")
        a[c] = d
    elif b == 2:
        g = True
        while g == True:
            c = input("輸入人")
            if c not in a:
                print("無此人")
            else:
                g = False
        d = input("輸入住址")
        a[c] =  d
    elif b == 3:
        g = True
        while g == True:
            c = input("輸入人")
            if c not in a:
                print("無此人")
            else:
                g = False
        a.pop(c)
    else:
        e = False
print(a)   
        
            

























