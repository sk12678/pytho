# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 23:53:59 2020

@author: andy6
"""




def a1():
    global a
    a = {"大雄":"台南市西門路五段十巷二十號","胖虎":"台南市中清路一段一巷一號"}
def a2():
    global b
    b = int(input("1:新增,2:編輯,3:刪除,4:結束"))
def a3():
    c = input("輸入人")
    d = input("輸入住址")
    a[c] = d
def a4():        
    g = True
    while g == True:
        c = input("輸入人")
        if c not in a:
            print("無此人")
        else:
            g = False
    d = input("輸入住址")
    a[c] =  d
def a5():        
    g = True
    while g == True:
        c = input("輸入人")
        if c not in a:
            print("無此人")
        else:
            g = False
        a.pop(c)
def a6():
    print(a)  

e = True
a1()
while e == True:
    a2()
    if b == 1:
        a3()
    elif b == 2:
        a4()
    elif b == 3:
        a5()
    else:
        e = False
a6()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    