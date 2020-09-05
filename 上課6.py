# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 19:32:28 2020

@author: andy6
"""

'''
#猜密碼
password = "applepie"
ch = input("請輸入字元=")
print("猜密碼1:in運算式")
#方法1
if ch in password:
    print("輸入字元在密碼中")
else:
    print("輸入字元不在密碼中")
    
#方式2
print("猜密碼2:not in運算式")
if ch not in password:
    print("輸入字元不在密碼中")
else:
    print("輸入字元在密碼中")
'''

'''
fruits = ["apple","banana","watermelon"]
fruit = input("請輸入水果=")
if fruit in fruits:
    print("這個水果已經有了")
else:
    fruits.append(fruit)
    print("謝謝提醒已經加入水果清單:",fruits)
'''

'''
x = 10 
y = 10 
z = 15
r = z-5
print("is用法")
boolean_value = x is y
print("x位置 = %d,y位置 = %d"%(id(x),id(y)))
print("x = %d, y =%d,%s"%(x,y,boolean_value))#寫法1

boolean_value = x is z
print("x位置 = %d,z位置 = %d"%(id(x),id(z)))
print("x = %d, z =%d, %s"%(x,z,boolean_value))#寫法1

boolean_value = x is r
print("x位置 = %d, r的位置 = %d"%(id(x),id(r)))
print("x = %d, r = %d," %(x,r),boolean_value)#寫法1
print("is not 用法")
boolean_value = x is not y
print("x的位置 = %d, y的位置 = %d"% (id(x),id(y)))
print("x = %d, y = %d,"%(x,y),boolean_value)#寫法2

boolean_value = x is not z
print("x位置 = %d,z位置 = %d"%(id(x),id(z)))
print("x = %d, z =%d,"%(x,z),boolean_value)#寫法2


boolean_value = x is not r
print("x位置 = %d,z位置 = %d"%(id(x),id(r)))
print("x = %d, z =%d,"%(x,r),boolean_value)#寫法2
'''
'''
mysports = ["basketball","baseball"]
sports1 = mysports   #賦值
sports2 = mysports[:]    #切片拷貝新串列
print("我喜歡的運動 =", mysports,"位置是 =" , id(mysports))
print("運動1       =", sports1,"位置是 =" , id(sports1))
print("運動2       =", sports2,"位置是 =" , id(sports2))
boolean_value = mysports is sports1
print("我喜歡的運動 is 運動1    =", boolean_value)

boolean_value = mysports is sports2
print("我喜歡的運動 is 運動2    =",boolean_value)

boolean_value = mysports is not sports1
print("我喜歡的運動 is 運動2    =", boolean_value)

boolean_value = mysports is not sports2
print("我喜歡的運動 is 運動1    =", boolean_value)
'''


'''
x = []
if x is None:
    print("it's None")
else:
    print("it's not None")
'''
'''
drinks = ["coffee","tea","wine"]
enumerate_drinks = enumerate(drinks)    #數值初始是0
print(enumerate_drinks)     #傳回enumerate物件所在記憶體
print("下列輸出enumerate物件類型")
print(type(enumerate_drinks))    #列出物件類型
#下列輸出
print("轉換成串列輸出, 初始索引值是 0 = ", list(enumerate_drinks))
#修改start
enumerate_drinks = enumerate(drinks, start = 10)   #數值初始是10
print("轉成串列輸出,初始索引值是10 =", list(enumerate_drinks))
'''















































