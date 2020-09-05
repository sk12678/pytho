# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:09:39 2020

@author: andy6
"""


'''
for i in range(1,10):
    for  j in range(1,10):
        result = i* j
        print("%d*%d = %- 4d"%(i,j,result),end = "")#調整格式
    print("")#單純換行輸出
'''

'''
for digit in range(1,11):
    if digit == 5:
        break
    print(digit, end=",")
'''


'''
scores = [33,22,41,25,39,43,27,38,40]
games = 0
for score in scores:
    if score< 30:    #小於三十則不往下執行
        continue
    games += 1     #場次加1
print("有%d場得分超過30分"%games)
'''


'''
num = int(input("請輸入大於1的整數做質數測試 = "))
if num == 2:       #2是質數所以直接輸出
    print("%d是質數"% num)
else:
    for n in range(2,num):   #用2 .. num-1當除數輸出
        if num % n ==0:    #如果整除不是質數
            print("%d不是質數"% num)
            break     #離開迴圈
        
    else:               #否則是質數
        print("%d是質數"% num)
'''

'''
msg1 = "請輸入各種文字,會重複輸出,但"
msg2 = "輸出 q 可以結束對話"
msg = msg1 +"\n" +msg2 +"\n" +"=>"
input_msg = ""   #預設為空字串
while input_msg != "q":
    input_msg = input(msg)
    print(input_msg)
'''

'''
answer = 50   #正確數字
guess = 0   #設定所猜數字的初始值
while guess != answer:
    guess = int(input("請猜1~100的數"))
    if guess > answer:
        print("請猜小一點")
    elif guess < answer:
        print("請猜大一點")
    else:
        print("恭喜答對了")
'''



'''
x = int(input("最大數"))
y = int(input("最小數"))
for z in range(y , x):
    z = z+1
    if z % 2 ==0:
        print(z)
'''
'''
x = int(input("最大數"))
y = int(input("最小數"))
z = y
while z in range(y,x):
    z = z +1
    if z % 2 == 0:
        print(z)
'''
    
    
    
        
    

    
    

























