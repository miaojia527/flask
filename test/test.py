#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, datetime
import os
import random
import operator

# 打开一个文件
print(random.randint(1000000,9999999))
'''
def funA(fn):
    # 定义一个嵌套函数
    def say(arc):
        print("Python教程:",arc)
        fn(arc)
    return say

def funC(fn):
	def say(arc):
		print("C：", arc)
		fn(arc)
	return say

@funA
@funC
def funB(arc):
    print("funB():", arc)

funB("http://c.biancheng.net/python")
'''

startDate = "2018-10-01"
endDate = "2018-10-31"

###字符转化为日期
timeArray = time.strptime(startDate, "%Y-%m-%d")
startDay  = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
startTime = time.mktime(timeArray)
print(startDay)
print(startTime)

sectime = time.time()
print(int(sectime))

m = 1582732800

str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(m))
print(str)

times = time.mktime(time.strptime(str, "%Y-%m-%d %H:%M:%S"))
print(int(times))

str = "runoob2016"  # 字符串没有空格
print (str.capitalize())

list1, list2, list3 = [123, 'xyz'], [456, 'abc'], [123, 'xyz']

'''
operator.lt(a,b) 等价于 a<b
operator.le(a,b) 等价于 a<=b
operator.eq(a,b) 等价于 a==b
operator.ne(a,b) 等价于 a!=b
operator.gt(a,b) 等价于 a>b
operator.ge(a,b) 等价于 a>=b
'''
print(operator.eq(list1, list2));
print(operator.eq(list2, list1));
print(operator.eq(list1, list3))


seq = ('Google', 'Runoob', 'Taobao')
 
dict = dict.fromkeys(seq)
print("新字典为 : %s" %dict)
 
dict = dict.fromkeys(seq, 10)
print("新字典为 : %s" %dict)








