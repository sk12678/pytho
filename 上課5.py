# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 21:03:25 2020

@author: andy6
"""

'''
sc = [["小明",85,90,80,0],
      ["小花",95,50,96,0],
      ]
sc[0][4] = sum(sc[0][1:4])
sc[1][4] = sum(sc[1][1:4])
print(sc[0])
print(sc[1])
'''
'''
mysports = ["basketball","baseball"]
friendsports = mysports[:]
print("列出mysports位置    =",id(mysports))
print("列出friendsports位置=", id(friendsports))
print("我喜歡的運動        = ",mysports)
print("我朋友喜歡的運動    =",mysports)
mysports.append("football")
friendsports.append("soccer")
print("--新增運項目--")
print("列出mysports位置   =", id(mysports))
print("列出friendsports位置=", id(friendsports))
print("我喜歡的最新運動    =", mysports)
print("我朋友喜歡的最新運動=", friendsports)
'''

'''
string ="Python"
#正值索引
print("string[0] =",string[0],
      "\n string[1] =",string[1],  
      "\n string[2] =",string[2],
      "\n string[3] =",string[3],
      "\n string[4] =",string[4],
      "\n string[5] =",string[5],
      )
#負值索引
print("string[-1]=",string[-1],
      "\n string[-2]=",string[-2],
      "\n string[-3]=",string[-3],
      "\n string[-4]=",string[-4],
      "\n string[-5]=",string[-5],
      "\n string[-6]=",string[-6],
      )
#多重指定觀念
s1, s2, s3, s4, s5, s6 = string
print("多重指定觀念的輸出測試=",s1,s2,s3,s4,s5,s6)
'''

'''
string = "Deep Learing"
print("列印string第0-2元素   =", string[0:3])
print("列印string第1-3元素   =", string[1:4])
print("列印string第2,4,6元素   =", string[1:6:2])
print("列印string第1到最後元素   =", string[1:])
print("列印string前3元素   =", string[0:3])
print("列印string後3元素   =", string[-3:])
'''

'''
sc = [1,2,3,4,5]
sc[2]=99
print("sc:",sc )
string = "Deep Learning"
string[2]= "E"
print("string:",string)
'''
'''
string = "Deep Learing"    #定義字串
strlen = len(string)
print("字串長度",strlen)
maxstr = max(string)
print("字串最大的unicode碼值和字元", ord(maxstr),maxstr)
minstr = min(string)
print("字串最小的unicode碼值和字元",ord(minstr),minstr)
'''

'''
string = "Deep Learing"
x = list(string) #轉換串列
print("轉換完的輸出",x)

x[1] = "E"
x[2] = "E"       #修改內容
print("修改後的輸出",x)
'''
'''
str1 = "Happy birthday to you"
str2 = "C:\Windows\office"
 
sList1 = str1.split()     #字串轉成陣列
sList2 = str2.split("\\")    #字串轉成陣列


print(str1, "  串列內容是   ", sList1)   #列印串列
print(str1, "  串列內容是   ", len(sList1))   #列印字數
print(str2, "  串列內容是   ", sList2)   #列印串列
print(str2, "  串列內容是   ", len(sList2))   #列印字數
'''

'''
path = ["c:","windows","Temp"]
connect = "\\"     #路徑分隔字元
print(connect.join(path))
connect = "*"     #普通字元
print(connect.join(path))
'''
'''
msg= "CIA Mard told CIA Linda that the secret USB had given to CIA Peter"
print("字串開頭是CIA:", msg.startswith("CIA"))
print("字串結尾是CIA:", msg.endswith("CIA"))
print("CIA出現的次數:",msg.count("CIA"))
msg = msg.replace("Linda","Lxx")
print("新的msg內容:",msg)
'''

































