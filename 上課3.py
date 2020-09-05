# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:05:42 2020

@author: user
"""
'''
#邏吉符號AND


x = (10 > 8) and ( 20 > 5 )
print("value x :",x)


y= (5.5 > 4) and (7 > 9)
print("value y :",y)


a = (1 > 0) and ( 2> (10/2))
print("value a :",a)


b = (9 > 99)  and (50 < (3 **2))
print("value b :",b)
'''


'''
#邏輯符號 OR

x = (10 > 8) or ( 20 > 5 )
print("value x :",x)


y= (5.5 > 4) or (7 > 9)
print("value y :",y)


a = (1 > 0) or ( 2> (10/2))
print("value a :",a)


b = (9 > 99)  or (50 < (3 **2))
print("value b :",b)
'''

'''
#邏輯符號


x = not(10 > 8)
print("value x :",x)

y = not(7>9)
print("value y :",y)
'''


'''
age = input("請輸入年齡")

if (int(age) <20):
    print("你年齡太小")
    print("需年滿20歲才可以購買菸酒")
'''
'''
#用戶認證系統
#使用者: peter or SUPERVIP


name = input("用戶你好,請輸入使用者名稱:")
if(name == "peter"):
    print("使用者%s,您好,歡迎登入"%name)

if(name == "SUPERVIP"):
    print("~~~歡迎貴賓:%s 登入~~~"% name)
'''
'''
x = eval(input("請輸入數值"))
y = int(x)
if( y>=0 )and( y<=100):
    print(y)
'''
'''
age = input("請輸入考駕照年齡:")
if(int(age) <18):
    print("你年齡太小，無法考取駕照")
else:
    print("歡迎登入考取駕照")
'''
'''
print("奇數偶數判斷")
num = input("請輸入任一整數值")
rem = int(num) %2


#1
if(rem == 0):
    print("%d是偶數"% int(num))
else:
    print("%d是奇數"% int(num))

#2
if(rem):
    print("%d是奇數"%int(num))
else:
    print("%d是偶數"%int(num))
'''
'''
x = input("考試成績")
y = eval(x)
int(y)
if(y>60):
    print("及格")
else:
    print("不及格")
'''
'''
x = eval(input("請輸入第一整數"))
y = int(x)
g = eval(input("請輸入第二整數"))
f = int(g)
if(y>f):
    print(y)
else:
    print(f)
'''

'''
print("計算最後成績")
score = input("請輸入分數:")
sc = int(score)
if(sc>=90):
    print("A")
elif(sc >= 80):
    print("B")
elif(sc>= 70 ):
    print("c")
elif(sc>= 60):
    print("d")
else:
    print("f")
'''

'''
print("計算票價")
age = input("請輸入年齡")
age = int(age)
ticket = 100
if(age >=80) or (age <= 6):
    ticket = ticket * 0.2
    print("票價是: %d" % ticket)
elif age>= 60 or age <=12:
    ticket = ticket * 0.5
    print("票價是: %d" %ticket)
else:
    print("票價是:%d" % ticket)
'''


'''
print("判斷輸入年分是否為閏年")
year = input("請輸入年分:")
rem4 = int(year) %4
rem100 = int(year) % 100
rem400 = int(year) % 400
if rem4 == 0:
    if rem100 !=0 or rem400 == 0:
        print("%s是閏年" %year)
    else:
        print("%s 不是閏年"  %year)
else:
    print("%s 不是閏年"   %year)
'''

'''
x = None 
print(type(x))

flag = None
if flag == None:
    print("尚未定義flag變數內容")

if flag:
    print("有定義")
else:
    print("尚未定義flag變數內容")

'''

'''

x = eval(input("體重 單位為公斤"))
y = eval(input("身高  單位為公尺"))
bmi = x / y**2
print(bmi)
if bmi<18.5:
    print("過輕")
elif 18.5<=bmi and bmi<24:
    print("正常")
elif 24<= bmi and bmi<28:
    print("超重")
elif bmi>=28:
    print("肥胖")

'''

























