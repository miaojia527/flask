#!/usr/bin/env python3
#coding=utf-8

# 找零钱字典，key为面额,value为最少硬币数
change_dict = {}
 
def rec_change(M, coins):
    change_dict[0] = 0
    s = 0
 
    for money in range(1, M+1):
        num_of_coins = float('inf')
        #意思是要求50的最少找零数，在46,47,49的最少找零数中找到最小的即可
        for coin in coins:
            if money >= coin:
                # 记录每次所用的硬币数量
                if change_dict[money-coin]+1 < num_of_coins:
                    num_of_coins = change_dict[money-coin]+1
                    s = coin #记录每次找零的面额
 
        change_dict[money] = num_of_coins
    return change_dict[M],s
 
# 求出具体的找零方式
# 用path变量记录每次找零的面额
def method(M, coins):
    print('Total denomination is %d.'%M)
    nums, path = rec_change(M, coins)#path为最少硬币数方案中的一个面额值
    print('The smallest number of coins is %d.'%nums)
    print('%s'%path, end='')
 
    while M-path > 0:
        M -= path
        nums, path = rec_change(M, coins)
        print(' -> %s'%path, end='')
    print()
 
coins = (1, 3, 4)
method(50, coins)
