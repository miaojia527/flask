#!/usr/bin/env python3
#coding=utf-8

#基本思想与分治法类似，也是将待求解的问题分解为若干个子问题（阶段），按顺序求解子阶段，前一子问题的解，
#为后一子问题的求解提供了有用的信息

'''
f(n, m) = max{f(n-1, m), f(n-1, m-w[n]) + P(n,m)}
选择价值最大的背包
初始化数据为：n=5，w={2,2,6,5,4}，v={6,3,5,4,6}，Cap=10
情况1:  第i件物品放不下，前i-1件物品放入容量为v的背包中，即f[i-1][v];
情况2:  选择不放入第i件，即变大时f[i-1][v];
        选择放入第i件物品f[i-1][v-w[i]]+v[i]
用m+1行代表容量，n+1列代表重量列表，结果存放在最后一列上
'''
import numpy as np

"""
设子问题：f[i][v]表示允许前i件物品放入容量为v的背包时可以获得的最大价值。注：这里的i从0到5，v从0到10
通过i和v建立二维数组来进行计算
"""

weights=[1,2,5,6,7,9]
price=[1,6,18,22,28,36]

#行李数n, 不超过的重量W, 重量列表w和价值列表p  
#放入物品的容量单位为0，未放入物品的为整数, n为重量列表的个数，W是容器的总量,w为重量列表，p为价值列表
def func(n,W,w,p):
    a = np.array([[0]*(W+1)]*(n+1))    #建立W+1行和n+1列的0矩阵
    #依次计算前i个行李的最大价值，n+1在n的基础上进行，行W+1为容量，列n+1为重量
    for i in range(1, n+1):            #递归取重量列表[1 : (n+1)]
        for j in range(1, W+1):        #递归取容器[1 : (W+1)] 
            if(w[i-1] > j):            #当对应的重量大于容器的遍历数时
                a[i, j] = a[i-1, j]    #将上一列的值赋值给当前列 如 0 1 1 1 1 1 1 1... 记录前一解的值为后面的解提供有用信息
            else:
                a[i ,j] = max(a[i-1, j], p[i-1]+a[i-1, j-w[i-1]]) #取max，上一列的值和价值+ 取2情况下重量值
                # 前i-1件物品放入剩下的容量为v-w[i]的背包中 即 j-w[i-1]
                #       
    print("max value is " + str(a[n, W]))   #取出最后一个单元值：a[6,13]=50

    #p为价值列表，n为重量个数，a[n,W]为最大价值数
    findDetail(p, n, a[n,W])
# 最后一列即为累加最大价值结果

#找到价值列表中的一个子集，使得其和等于前面求出的最大价值，即为选择方案
def findDetail(p,n,v):
    a = np.array([[True]*(v+1)]*(n+1))          #创建v+1行，n+1列的True数组
    for i in range(0, n+1):                    
            a[i][0] = True                      #给第一列 n+1个 赋值True
    for i in range(0, v+1):
            a[0][i] = False                     #给第一行 v+1个 赋值False
    for i in range(1, n+1):                     
            for j in range(1, v+1):             
                    if p[i-1] > j:              #找出价值
                            a[i, j]= a[i-1, j]  #赋值上一行的值
                    else:
                            a[i,j] = a[i-1, j] or a[i-1, j-p[i-1]]  #赋值上一行或剩余重量的值
    print(a)
    if a[n,v]:                                  #如果最后一个元素是真
            i=n                                 #将重量数赋值给i
            result=[]                           
            while i>=0:                            
                    if a[i, v] and not a[i-1,v]:  #定位元素
                            result.append(p[i-1]) #获取价值，添加到结果
                            v-=p[i-1]             #最大价值v 减去已获取的价值
                    if v==0:                        
                            break
                    i-=1
            print(result)
    else:
        print("error")

func(len(weights),13,weights,price)
# 放入28,22，得到最大价值数50

def fun(n,W,w,p):
    a = np.array([[0]*(W+1)]*(n+1))

    for i in range(1, n+1):
        for j in range(1, W+1):
            if w[i-1] > j:
                a[i, j] = a[i-1, j]
            else:
                a[i, j] = max(a[i-1, j], p[i-1] + a[i-1, j-w[i-1]])
    print("Max Value is ", a[n, W])
    findDeal(p,n,a[n, W])

def findDeal(p,n,v):
    a = np.array([[True]*(v+1)]*(n+1))

    for i in range(0, n+1):
        a[i][0] = True
    for j in range(0, v+1):
        a[0][j] = False
    for i in range(1, n+1):
            for j in range(1, v+1):
                if p[i-1] > j:
                    a[i , j] = a[i-1, j]
                else: 
                    a[i , j] = a[i-1, j] or a[i-1, j-p[i-1]]
    if a[n,v]:
            i = n
            result = []
            while i > 0:
                if a[i, v] and not a[i-1 , v]:
                    result.append(p[i-1])
                    v -= p[i-1]
                if v == 0:
                    break
                i -= 1
    else:
        print("errors")    