# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 14:26:05 2020

@author: andy6
"""

e = True
accounts = []
x = input("建立帳號")
accounts.append(x)
while e == True:
    y = input("輸入帳號")
    if y in accounts:
        print("歡迎進入系統")
        e = False
    else:
        print("輸入錯誤")
       
       
    
    



    
    
    
