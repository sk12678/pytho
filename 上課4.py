# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 19:06:44 2020

@author: user
"""
'''
james = {23, 19, 22, 31, 18}       #定義james串列
print("列印james串列", james)
James = {"Lebron James",23 ,19 ,22 ,31 ,18}  #定義James串列
print("列印James串列",James)
fruits = {"apples", "banana", "orange"}   #定義fruits串列
print("列印fruits串列",fruits)
cfruits = {"蘋果","香蕉", "橘子"}     #定義cfruits串列
print("列印cfruits串列",cfruits)
ielts = {5.5, 6.0, 6.5}       #定義IELTS成績串列
print("列印IELTS成績",ielts)
#列出串列資料形態
print("串列james資料形態是:",type(james))
'''

'''
james = [23,19,22,31,18]   #定義
#讀取串列元素
game1 = james[0]
game2 = james[1]
game3 = james[2]
game4 = james[3]
game5 = james[4]
print("列印james各場次得分", game1,game2,game3,game4,game5)
'''

'''
x = [1,2,3,4,5,6,7,8,9,10]
print("取得串列前n名>>",x[:3])      #取得串列前n名
print("取得串列前面,不含最後n名>>",x[:-3])    #取得串列前面,不含最後n名
print("取得串列索引n到最後>>",x[3:])    #取得串列索引n到最後
print("取得串列後n名>>",x[-3:])     #取得串列後n名
'''


'''
james = [23,19,22,31,18]       #定義james串列
print("列印james第1-3場得分",james[0:3])
print("列印james第2-4場得分",james[1:4])
print("列印james第1,3,5場得分",james[0:6:2])
'''

'''
warriors = ["Curry","Durant","Iquodala","Bell","Thompson"]
print(warriors[-1],warriors[-2],warriors[-3],warriors[-4],warriors[-5])
'''

'''
james = [23,19,22,31,18]
games = len(james)
print("經過%d場比賽得分最高得分="% games, max(james))
print("經過%d場比賽得分最低得分="% games, min(james))
print("經過%d場比賽得分得分總計="% games, sum(james))
'''

'''
james = [23,19,22,31,18]     #定義james的5場比賽得分
print("舊的James比賽分數",james)
james[4] = 28
print("新的James比賽分數", james)
'''

'''
cars1 = ["Toyota","Nissan", "Honda"]
print("舊汽車銷售品牌",cars1)
cars2 = ["Audi","BMW"]
cars1 +=cars2    #串列相加
print("新汽車銷售品牌", cars1)


nums = [1,3,5]
numslist = nums *5    #串列乘以數字
print(numslist)
'''
    
'''
James = ["Lebron James",23,19,22,31,18]    #定義James串列
Love = ["Kevin Love",20,18,30,22,15]     #定義Love串列
game3 = James[4] +Love[4]
LKgame = James[0] + "和" + Love[0] +"第四場總得分="
print(LKgame, game3)
'''
'''
nums1 = [1,3,5]
print("刪除nums1串列索引1元素前 =",nums1)
del nums1[1]
print("刪除nums1串列索引1元素後 =",nums1)
nums2 = [1,2,3,4,5,6]  
print("刪除nums2串列索引[0:2]前 =",nums2)
del nums2[0:2]
print("刪除nums1串列索引[0:2]後 =",nums2)
nums3 = [1,2,3,4,5,6]
print("刪除nums1串列索引[0:6:2]前 =",nums3)
del nums3[0:6:2]
print("刪除nums1串列索引[0:6:2]後 =",nums3)
'''


'''
cars = ["Toyota", "Nissan","Honda"]
print("cars串列長度是= %d" % len(cars))
if len(cars) != 0:
    del cars[0]
    print("刪除cars串列元素成功")
    print("cars串列長度是 = %d" % len(cars))
else:
    print("cars串列內沒有元素資料")
nums = []
print("nums串列長度是 = %d" % len(nums))
if len(nums)!=0:
    del nums[0]
    print("刪除nums串列元素成功")
else:
    print("nums串列內沒有元素資料")

name_list = [1,2,3,4,5,6]
print("name_list 刪除前,印出", name_list)
del name_list
'''


'''
cars = []
print("目前串列內容=" ,cars)
cars.append("Honda")
print("目前串列內容=",cars)
cars.append("Toyota")
print("目前串列內容=",cars)
cars.append("Ford")
print("目前串列內容=",cars)
'''
'''
cars = ["Honda","Toyoya","Ford"]
print("目前串列內容 =",cars)
print("在索引1位置插入Nissan")
cars.insert(1,"Nissan")
print("新的串列內容=",cars)
print("在索引0位置插入BMW")
cars.insert(0,"BMW")
print("最新串連內容=",cars)
'''

'''
cars = ["Honda","Toyota","Ford","BMW"]
print("目前串列內容=",cars)
print("使用pop()刪除串列元素")
popped_car = cars.pop()      #刪除串列未滿值
print("所刪除的串列內容是:",popped_car)
print("新的串列內容=",cars)
print("使用pop(1)刪除串列元素")
popped_car = cars.pop(1)      #刪除串列索引為1的值
print("所刪除的串列內容是:",popped_car)
print("新的串列內容=",cars)
'''

'''
cars = ["Honda","bmw","Toyota","Ford","bmw"]
print("目前串列內容=",cars)
print("使用remove()刪除串列元素")
expensive = "bmw"
cars.remove(expensive)        #刪除第一次出現的元素
print("所刪除的內容是:"+expensive.upper() +"因為太貴了")
print("新的串列內容",cars)
'''
'''
cars = ["Honda","bmw","Toyota","Ford","bmw"]
print("目前串列內容=",cars)
#直接列印cars[::-1]顛倒排序,不更改串列內容
print("列印使用[::-1]顛倒排序\n",cars[::-1])
#更改串連內容
print("使用reverse()顛倒排序串列元素")
cars.reverse()      #顛倒排序串列
print("新的串列內容=",cars)
'''

'''
cars = ["honda","bmw","toyota","ford"]
print("目前串列內容=",cars)
print("使用sort()由小排到大")
cars.sort()
print("排序串列結果=",cars)
print("目前串列內容=",cars)
print("使用sort()由小排到大")
cars.sort(reverse=True)
print("排序串列結果=",cars)

nums = [5,3,9,2]
print("目前串列內容=",nums)
print("使用sort()由小排到大")
nums.sort()
print("排序串列結果=",nums)
print("目前串列內容=",nums)
print("使用sort()由小排到大")
nums.sort(reverse=True)
print("排序串列結果=",nums)
'''

'''
nums = [5,3,9,2]
print("目前串列num內容=",nums)
print("使用sorted()由小排到大")
nums_sorted =sorted(nums)
print("排序串列結果=",nums_sorted)
print("使用sorted()由大排到小")
nums_sorted = sorted(nums,reverse=True)
print("排序串列結果   =",nums_sorted)
print("原先串列num內容=",nums)
'''
'''
cars = ["toyota","nissan","honda"]
search_str = "nissan"
i = cars.index(search_str)
print("所搜尋元素%s第一次出現位置索引是%d" %(search_str, i))
nums = [7,12,30,12,30,9,8]
search_val = 30
j = nums.index(search_val)
print("所搜尋元素%s第一次出現位置索引是%d"%(search_val, j))
'''

'''
cars = ["toyota","nissan","honda"]
search_str = "nissan"
num1 = cars.count(search_str)
print("所搜尋元素%s出現%d次"%(search_str,num1))
nums = [7,12,30,12,30,9,8]
search_val = 30
num2 = nums.count(search_val)
print("所搜尋元素%s出現%d次"%(search_val,num2))
'''

'''
James = [["Lebron James","SF","12/30/84"],23,19,22,31,18]#定義James串列
games = len(James)                          #求元素數量
score_Max = max(James[1:games])              #最高得分
i = James.index(score_Max)                 #場次
name = James[0][0]
position = James[0][1]
born = James[0][2]
print("姓名    :",name)
print("位置    :",position)
print("出生日期:",born)
print("在第%d場得最高分%d"%(i,score_Max))
'''

'''
cars1 = ["toyota","nissan","honda"]
cars2 = ["ford","audi"]
print("原先cars1串列內容 =",cars1)
print("原先cars2串列內容 =",cars2)
cars1.append(cars2)
print("執行append()後串列cars1內容=",cars1)
print("執行append()後串列cars2內容=",cars2)
'''

'''
cars1 = ["toyota","nissan","honda"]
cars2 = ["ford","audi"]
print("原先cars1串列內容 =",cars1)
print("原先cars2串列內容 =",cars2)
cars1.extend(cars2)
print("執行extend()後串列cars1內容=",cars1)
print("執形extend()後串列cars2內容=",cars2)
'''





































