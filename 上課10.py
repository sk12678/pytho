# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 21:44:36 2020

@author: andy6
"""




'''
def greeting():
    """my first python function"""
    print("welcome")
#以下的程式碼也可稱為主程式
greeting()
greeting()
greeting()
greeting()
greeting()
'''

'''
def greeting(name):
    """Python函數需傳遞名子name"""
    print("Hi,", name, "Good Morning")
    return(name)
net_value = greeting("Nelson")
print("greeting()值回復 = ", net_value)
print(net_value, "的 type = ", net_value)
greeting("Nelson")
'''

'''
def subtract(x1,x2):
    result = x1 -x2
    return result
a = int(input("a ="))
b = int(input("b = "))
print("a - b =", end = "")
c = subtract(a,b)
print(c)
'''

'''
def printmsg():
    msg = "Local Variable"
    print("函數列印:", msg)
msg = "Global Variable"
print("主程式列印", msg)
printmsg()
'''
'''
def d():
    msg = "a"
def g():
    print(msg)

g()   #此為錯誤程式
'''
'''
def d():
    msg = "a"
print(msg)       #錯誤程式
'''
'''
def d():
    msg = ("Java")
    print("更改後:", msg)
msg = "a"
d()
print("全域變數:", msg)
'''
'''
def p():
    global msg
    msg = "Java"
    print(msg)
msg = "Python"
print(msg)
p()
print(msg)
'''

'''
import random
print(random.random())

from random import*
print(random())
'''


'''
from random import seed,random
print(random())
import random as QQ
print(QQ.random())
'''





























