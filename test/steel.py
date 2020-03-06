#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
#钢条切割，已经各长度的钢条和对应的收益，问长度为n的钢条怎么切割收益最大，即n-1最大收益+长度1的收益，n-2最大收益+长度2最大收益
#钢条长度与对应的收益
length = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
profit = (1, 5, 8, 9, 10, 17, 17, 20, 24, 30)

# 参数：profit：收益列表，n：钢条总长度
def bottom_up_cut_rod(profit, n):
    r = [0]  # 收益列表
    s = [0]*(n+1)

    for j in range(1, n+1):
        q = float('-inf')
        #每次循环求出长度为j的钢条切割最大收益r[j]，s[j]则保存切割方案中最长的那一段长度
        for i in range(1, j+1):
            #元组index从1开始
            if max(q, profit[length.index(i)]+r[j-i]) == profit[length.index(i)]+r[j-i]: 
                s[j] = i #如果切割方案为1和2，那么2会覆盖1，即保留最长的一段
            q = max(q, profit[length.index(i)] + r[j-i])
        r.append(q)
        #r[n]保存长度为n钢条最大切割收益
    return r[n], s[n]

#切割方案
def rod_cut_method(profit, n):
    how = []
    while n != 0:
        t,s = bottom_up_cut_rod(profit, n)
        how.append(s)
        n -= s

    return how
#输出长度1~10钢条最大收益和最佳切割方案
for i in range(1, 11):
    t1 = time.time()
    money, s = bottom_up_cut_rod(profit, i)
    how = rod_cut_method(profit, i)
    t2 = time.time()
    print("profit of %d is %d. Cost time is %ss." % (i, money, t2-t1))
    print("Cut rod method:%s\n" % how)