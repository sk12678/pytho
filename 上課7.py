# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 20:42:57 2020

@author: andy6
"""

'''
#定義水果籃串列,與裡面的水果
basket = ["apple", "banana", "orange", "watermelon", "kiwi", "tomato"]
#迴圈開始正常使用方式
for fruit in basket:#
    print("水果:",fruit) #迭代:basket 水果盤
    print("很好吃的樣子")
#第二種一行的迴圈設計方式
for fruit in basket: print("水果:", fruit)
'''

'''
#定義水果籃串列,與裡面的水果
basket = ["apple", "banana", "orange", "watermelon", "kiwi", "tomato"]
#迴圈開始
for fruit in basket[:3]: #迭代:basket 水果盤
    print("水果:",fruit) #列印出水果
print("後三個水果")
for fruit in basket[-3:]: #迭代:basket 水果盤
    print("水果:",fruit) #列印出水果
'''

'''
names = ["王曉明","陳曉東","王大牛","林阿美"]
lastnames = []
for name in names:
    if "王" in name:
        lastnames.append(name)
print(lastnames)
'''

'''
basket = ["apple","banana","orange","watermelon","kiwi","tomato"]
basket2 = ["apple","kiwi","lemon"]
print("目前水果盤2中有的水果是",basket2)
for fruit in basket2[:]: #注意這裡是要做一個copy的動作,不然會有錯
    if fruit in basket:
        basket2.remove(fruit)
        print("移除:", fruit)
print("最後水果盤2剩下",basket2)
'''

'''
example = "foodpanda"
for font in example:
    print(font)
'''

'''
number = []
for x in range(10):
    number.append(x)
print(number)

n = int(input("輸入幾個星號"))
for x in range(n):
    print("*",end ="")#我們不讓她換行,所以end要修改掉"\r"改為""
'''

'''
n = int(input("正整數"))+1
z = 0
for x in range(n):
    z = (z + x)
print(z)
'''
'''
y = []
n = int(input("正整數"))+1
for x in range(n):
    if(x > 10):
        y.append(10**2)
    else:
        y.append(x**2)
print(y)
'''
    






























































