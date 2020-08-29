# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:09:36 2020

@author: andy6
"""


a = True
z = []
x = ["電視","冰箱","洗衣機","烤箱","冷氣機","檯燈"]
print(x)
while a == True:
    y = input("請輸入要購買的物件")
    if y in x:
        if y in z:
            print("已購買")
            b = int(input("如要重複購買請按1"))
            if b == 1:
                z.append(y)
                c = input("離開請打exit")
                if c == "exit":
                    a = False
                else:
                    continue
        else:
            z.append(y)
            c = input("離開請打exit")
        if c == "exit":
            a = False
        else:
            continue
    else:
        print("清單中無此物品")
        c = input("離開請打exit")
        if c == "exit":
            a = False
print(z)












