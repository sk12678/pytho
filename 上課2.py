# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:47:12 2020

@author: user
"""
'''

str123 = "Hi python"
print(dir(str123))

'''
'''
num1 = 222
num2 = 333
num3 = num1 + num2

print("這是數值相加", num3)
str1 = str(num1) + str(num2)
print("強制轉換為字串相加",str1 , sep=" $$$ ")
      
num1 = 222
num2 = 333
num3 = num1 + num2
print("這是數值相加",num3, end="\t")      #以Tab鍵值位置分隔2筆資料輸出
str1 = str(num1) +str(num2)
print("強制轉換為字串相加",str1, sep=" $$$ ")
'''
'''
score = 100
name = "Python新手"
count = 1
print("%s你的第 %d次考試成績是%d"%(name, count, score))
'''
'''
score = 100
name = "Python新手"
count = 1
str_value = "%s你的第%d 次考試的成績是%d"
print( str_value % (name, count, score))
x = 100
print("100的16進位 = %x\n100的8進位 = %o"%(x,x))
x = 20
print("整數%d \n浮點數%f \n16進位數%x \n字串%s "%(x ,x ,x,x))
print("-----------------")
y = 9.9
print("整數%d \n浮點數%f \n16進位數%x \n字串%s" %(y, y, int(y),y))
'''
'''
x = 100
print("x=/%6d/"% x)
y = 10.5
print("y=/%6.2f/"%y)
s = "Deep"
print("s=/%6d"% x)
print("以下是保留格數空間不足的實例")
print("x=/%2d/"% x)
print("y=/%3.2f/"% y)
print("s=/%2s/" % s)
x =100
print("x=/%-6d/" % x)
y =10.5
print("y=/%-6.2f/" % y)
s ="Deep"
print("s=/%-6s/"% s)



#增加+
x = 10
print("x=/%+6d/" % x)
y = 10.5
print("y=/%+6.2f/"% y)
'''
'''
print("  姓名     國文   英文    總分")
print(" %3s     %4d   %4d    %4d"%("a", 2 ,5, 7))
print(" %3s     %4d   %4d    %4d"%("b", 1 ,3, 4))
print(" %3s     %4d   %4d    %4d"%("c", 4,6,  10 ))
print(" %3s     %4d   %4d    %4d"%("d", 7 ,9, 16 ))
'''
'''
score = 90
name = "Python 新手"
count = 1
print("{}你的第{}考試成績是{}". format(name, count, score))
score = 90
name = "Python新手"
count = 1
#以下鼓勵使用
print("{0}你的第{1} 次物理考試成績是{2}".format(name,count,score))


#以下語法對但不鼓勵使用
print("{2}你的第{1} 次物理考試成績是{0}".format(score,count,name))
'''
'''
r = 5
PI = 3.14159
area = PI *r **2

print("/半徑{0:3d}園面積是{1:10.2f}/".format(r,area))
print("/半徑{0:>3d}園面積是{1:>10.2f}/".format(r,area))
print("/半徑{0:<3d}園面積是{1:<10.2f}/".format(r,area))
print("/半徑{0:^3d}園面積是{1:^10.2f}/".format(r,area))
print("/半徑{0:^3d}園面積是{1:?^10.2f}/".format(r,area))
'''
'''
fstream1 = open("c:\pythontest\out1.txt", mode="w") #取代先前資料
print("Testing for output", file=fstream1)
fstream1.close( )
fstream2 = open("c:\pythontest\out2.txt", mode="a")#附加資料後面
print("Testing for output", file=fstream2)
fstream2.close()
fstream3 = open("c:\pythontest\out3.txt", mode="x")#新開檔案
print("Testing for output", file = fstream3)
fstream3.close()
'''
'''
print("歡迎使用成績輸入系統")
name = input("請輸入姓名:")
score = input("請輸入英文成績:")
math = input("請輸入數學成績:")
total = int(score) + int(math)
print("%s 你的總分是%d"%(name, total))
lastname = input("請輸入中文姓氏:")
firstname = input("請輸入中文名子:")
fullname = lastname + firstname
print("%s 歡迎使用本系統"% fullname)
'''

numberStr =  input("請輸入數值公式:")
number = eval(numberStr)
print("計算結果 : %5.2f"% number)
n1, n2, n3 = eval(input("請輸入3個數字:"))
average = (n1 + n2 + n3) /3
print("3個數字平均是%6.2f" % average)








































