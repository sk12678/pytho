# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
x = 10.5
print(x)
print(type(x))    #加法前列出x資料形態
y = int(x) + 5
print(y)
print(type(y))    #加法後列出y資料形態
    
x = 10
print(x)
print(type(x))      #加法前列出x資料形態
y = float(x)+10
print(y)
print(type(y))    #加法後列出y資料形態


'''

'''

x = 0b1101      #這是2進位整數
print(x)     #列出10進位結果
y = 13          #這是10進位整數
print(bin(y))       #列出轉換成2進位的結果

'''

'''
x = 0o57      #這是8進位整數
print(x)        #列出10進位的結果
y = 47        #這是10進位的結果
print(oct(y))      #列出轉換成8進位的結果


'''

'''
x = 0x50   #這是16進位整數
print(x)     #列出10進位結結果
y = 93  #這是10進位整數
print(hex(y))  #列出轉換成16進位的結果

'''
'''
x = -10
print("以下輸出abs()函數的應用")
print(x)      #輸出x變數
print(abs(x))   #輸出abs(x)
      
x = 5
y = 3
print("以下輸出pow()函數的應用")
print(pow(x,y))    #輸出pow(x,y)
x= 47.5
print("以下輸出round(x)函數的應用")
print(x)         #輸出x變數
print(round(x))    #輸出round(x)
x = 48.5
print(x)         #輸出x變數
print(round(x))    #輸出round(x)
x = 49.5
print(x)      #輸出x變數
print(round(x))    #輸出round(x,1)
print("以下輸出round(x,n)函數的應用")
x = 2.15
print(x)       #輸出x變數
print(round(x,1))           #輸出round(x,1) 
x = 2.25
print(x)    #輸出x變數
print(round(x,1))         #輸出round(x,1)
x = 2.151
print(x)   #輸出x變數
print(round(x,1))       #輸出round(x,1)
x = 2.251
print(x)       #輸出x變數
print(round(x,1))        #輸出round(x,1)

'''
'''
x = True
print(x)
print(type(x))      #列出x資料型態
#轉換型態
print(int(x))
print(type(x))      #列出x資料型態



y = False
print(y)
print(type(y))        #列出y資料型態
#轉換型態
print(int(y))
print(type(y))      #列出y資料型態

xt = True
x = 1+xt
print(x)
print(type(x))         #列出x資料型態

yt = False
y = 1 +yt
print(y)
print(type(y))         #列出y資料型態

'''
'''
num1 = 222
num2 =333
num3 = num1 +num2
print("以下是數據相加")
print(num3)
numstr1 = "222"
numstr2 = "333"
numstr3  =numstr1 +numstr2
print("以下是數據組成的字串相加")
print(numstr3)
numstr4 = numstr1 +" " + numstr2
print("以下是由數據組成的字串相加,同時中間加上一空格")
print(numstr4)
str1 ="DeepStone"
str2 ="Deep Learning"
str3 = str1 +str2
print("以下是一般字串相加")
print(str3)
'''
'''



#不管追由什麼目標,都應堅持不懈

'''

str1 = '''Pursue your object, be it what it will,
steadily and indefatigably.'''
print(str1)
#字串內有沒有分行符號
'''
'''
str1_1 = '''Pursue your object, be it what it will,\
           steadily and indefatigably.'''
print(str1_1)
#字串內有分行符號


str2 = "Pursue your object, be it what it will,"\
       "steadily and indefatigably."
print(str2)
#使用\符號

str3 =("Pursue your object, be it what it will,"
       "steadily and indefatigably.")
print(str3) #使用小括號


#以下輸出使用單引號設定的字串,須使用\'
str1 = 'I can\'t stop Loving you.'
print(str1)
#以下輸出使用雙引號設定的字串,不需使用\'
str2 = "I can't stop Loving you."
print(str2)
#以下輸出有\t和\n字元
str3 = "I \tcan't stop \nLoving you."
print(str3)



x = str()
print("印出空字串")
print(x)



y = str("ABCD")
print("列印出字串")
print(y)


z = 12345
z = str(z)
print("印出轉換的字串")
print(z)
print("印出類型")
print(type(z))

x1 = "22"
x2 ="33"
x3 = x1 + x2
print(x3)    #列印字串相加
x4 = int(x1) + int(x2)
print(x4)     #列印整數相加


'''

x1 = "A"
x2 = x1*10
print(x2)     #列印字串乘以整數
x3 ="ABC"
x4= x3 * 5
print(x4)    #列印字串乘以整數


str1 = "資料形態"
str2 = "字串類型應用"
str3 ="斷行演練"
str4 = str1 + "\n" +str2 +"\n" +str3
print(str4)

str1 = "Hello!\nPython"
print("不含r字元輸出")
print(str1)
str2 = r"Hello!\nPython"
print("含r字元的輸出")
print(str2)
'''
chr(97)

chr(0x33)














