# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:22:18 2020

@author: andy6
"""

'''
numbers = [1,2,3,4,5]
#方法一
for number in numbers:
    pass
#方法二
while 1 :
    pass
'''

'''
tuple_sample1 = ("ABC", 1, 2, 3)
tuple_sample2 = ("HI")
print(tuple_sample1)  #列印元素1
print(tuple_sample2)   #列印元素2
print(tuple_sample1[0])
print(tuple_sample1[:3])
print(tuple_sample1[-1:])
#個別指定
x , y = ("Apple", "Orange")
print(x , y)   #列印x y
'''


    
'''
tuple_sample = ("Apple","Lemon","Kiwi")
for key in tuple_sample:
    print(key)
tuple_sample = ("Apple","Lemon","Kiwi")
print("初始的元組", tuple_sample)
tuple_sample[0] = "orange"
print("修改後元組" , tuple_sample) 
'''


'''
tuple_sample = ("Apple","Lemon","Kiwi")
print("最初始的元組" , tuple_sample)
print("初始的元組 位置", id(tuple_sample))
tuple_sample = ("Apple", "Lemon", "Orange")
print("修改後元組", tuple_sample)
print("修改後的元組 位置:", id(tuple_sample))
'''

'''
tuple_sample = ("Apple","Lemon","Kiwi") #定義字串是元組或數字
print("tuple_sample元組長度是%d"% len(tuple_sample))
tuple_sample = tuple_sample.pop() #錯誤
tuple_sample.append("banana") #錯誤
'''


'''
tuple_sample = ("Apple","Lemon","Kiwi")
list_keys = list(tuple_sample)  #將元組改為串列
list_keys.append("orange")  #增加元素
tuple_key = tuple(list_keys)
print("列印元組",tuple_sample)
print("列印串列",list_keys)
print("列印轉換後的串列",tuple_key)

'''


'''
fruits = {"西瓜":15, "香蕉":20,"水蜜桃":25}
noodles = {"牛肉麵":100,"肉絲麵":80,"陽春麵":60}
print(fruits)
print(noodles)
#列出字典資料型態
print("字典fruits資料型態是:", type(fruits))
print("水蜜桃一斤 =", fruits ["水蜜桃"],"元")
print("牛肉麵一碗 =", noodles["牛肉麵"],"元")
fruits["橘子"] = 18
print(fruits)
print("橘子一斤 = ", fruits["橘子"], "元")
print("舊價格香蕉一斤 = ", fruits["香蕉"], "元")
fruits["香蕉"] = 12
print("新價格香蕉一斤 = ", fruits["香蕉"], "元")
print("舊fruits字典內容:", fruits)
del fruits["西瓜"]
print("新fruits字典內容:", fruits)
'''
'''
fruits = {0:"西瓜", 1:"香蕉", 2 :"水蜜桃"}
print(fruits[0],fruits[1],fruits[2])
'''

'''
fruits = {"西瓜":15, "香蕉":20,"水蜜桃":25}
print("舊fruits字典內容:", fruits)
del fruits
print("新fruits字典內容:", fruits)  #錯誤!錯誤
'''

'''
fruits = {"西瓜":15, "香蕉":20,"水蜜桃":25}
print("舊fruits字典內容:", fruits)
objKey = "西瓜"
value = fruits.pop(objKey) 
print("刪除內容:", objKey + ":" + str(value))
print("新fruits字典內容:", fruits)
'''
'''
fruits = {"西瓜":15, "香蕉":20,"水蜜桃":25}
print("舊fruits字典內容:", fruits)
fruits.clear()
print("新fruits字典內容:", fruits)
'''
'''
fruits = {"西瓜":15, "香蕉":20,"水蜜桃":25,"蘋果":18}
cfruits = fruits.copy()
print("位置:", id(fruits)," fruits元素 = ", fruits)
print("位置:", id(cfruits)," fruits元素 = " , cfruits)
'''

'''
dict_1 = {"ricky":85, "jack":90, "mark":60}
dict_1["mary"] = 50        #新增成績
dict_1["terry"] =100   #新增成績
listkey = list(dict_1.keys())   #使用keys搜尋所有鍵
listvalue = list(dict_1.values())  #使用values搜尋所有值
for i in range(len(listkey)):
    print(" %s的成績為 %d分" %(listkey[i],listvalue[i]))
'''

'''
dict_1 = {"ricky": 85, "jack":90,"mark":60} 
dict_1["mary"] = 50     #新增成績
dict_1["terry"] = 100   #新增成績
listitem = dict_1.items() #使用item 
for name,score in listitem:    #變數會有兩組
    print("%s 的成績為%d分"%(name,score))
'''

'''
fruits = {"西瓜":15, "香蕉":20,"水蜜桃":25}
n = fruits.get("西瓜")
print("西瓜 無設定default 回傳值:",n)
n = fruits.get("西瓜",100)
print("西瓜 有設定default 回傳值:",n)
n = fruits.get("奇異果")
print("奇異果 無設定default 回傳值:",n)
n = fruits.get("奇異果",80)
print("奇異果 有設定default 回傳值:",n)
print( fruits.items() )
'''
'''
fruits = {"西瓜":15, "香蕉":20,"水蜜桃":25}
n = fruits.setdefault("西瓜")
print("西瓜 無設定default 回傳值:",n)
n = fruits.setdefault("西瓜",100)
print("西瓜 有設定default 回傳值:",n)
n = fruits.setdefault("奇異果")
print("奇異果 無設定default 回傳值:",n)
n = fruits.setdefault("鳳梨",80)
print("鳳梨 有設定default 回傳值:",n)
print( fruits.items() )
'''
'''
fruits = {"西瓜":15, "香蕉":20,"水蜜桃":25}
key = input("請輸入鍵(key)=")
value = input("請輸入值(value)=")
if key in fruits:
    print("%s已經在字典裡了"% key)
else:
    fruits[key] = value
    print("新的fruits字典內容 =", fruits)
'''
'''
season = {"Spring":"春季",
          "Summer":"夏季",
          "Falll":"秋季",
          "Winter":"冬季"}

wd = input("請輸入欲查詢的單字:")
if wd in season:
    print(wd,"中文字義是:", season[wd])
else:
    print("查無此單字")
'''

'''
survey_dict = {}    #建立市場問卷調空字典
market_survey = True  #設定迴圈布林值
#讀取參加市場調查者姓名和旅遊景點
while market_survey == True:
    if market_survey == True:
        name = input("\n請輸入姓名")
        travel_location = input("旅遊景點:")
#將輸入存入survey_dict字典
        survey_dict[name] = travel_location
#可由此決定是否離開市場調查
        repeat = input("是否要離開")
        if repeat != "y":   #不是輸出y,則離開while迴圈
            market_survey = False

#市場調查結果
print("\n\n以下是市場調查的結果")
listitem = survey_dict.items()
for name,travel_location in listitem:
    print("%s %s"%(name,travel_location))
'''




































