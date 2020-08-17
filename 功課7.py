# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 10:03:05 2020

@author: andy6
"""

print(str.lower("ABC"))   #將字串轉成小寫字
print(str.upper("abc"))    #將字串轉成大寫字
print(str.title("abc"))    #將字串轉成第一個字母大寫
print(str.swapcase("abcABC"))   #將字串大寫改小寫,小寫改大寫
print("abc       cccccccccc")   #尚未刪除
str =("abc       cccccccccc")  
print(str.rstrip("c"))      #刪除字串尾指定的字
print("aaaaaaaaa         abc")    #刪除前
str =("aaaaaaaaa         abc")     
print(str.lstrip("a"))    #刪除字串頭指定的字
print("aaaaaaaaaa        abc      ccccccccc")    #尚未刪除
str =("aaaaaaaaaa        abc      ccccccccc")
print(str.strip("a,c"))    #刪除字串頭尾指定的字
str= ("abc")
print(str.center(10,"@"))     #字串加上括號內的指定符號要等於指定寬度 #字串置中
str = ("abc")
print(str.rjust(10,"@"))    #字串加上括號內的指定符號要等於指定寬度  #字串最右
str = ("abc")
print(str.ljust(10,"@"))    #字串加上括號內的指定符號要等於指定寬度  #字串最左
str = ("abc")
print(str.zfill(10))      #字串靠右 #左邊多餘空間補零 #零加字串要等於指定寬度







