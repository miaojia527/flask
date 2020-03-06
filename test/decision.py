#!/usr/bin/env python3
#coding=utf-8

class Solution:
    
    #有n级台阶，一个人每次上一级或者两级，问有多少种走完n级台阶的方法。1为1种，2为2种
    def up(self, n):
        L =[]
        L.append(1)
        L.append(2)
        for i in range(2, n):
            L.append(L[i - 1] + L[i - 2])
        return L[n-1]
    
    #寻找丑数
    def GetUglyNumber(self,index):
        if index < 1:
            return 0
        if index == 1:
            return 1
        s = []
        s.append(1)
        t1 = 0
        t2 = 0
        t3 = 0
        for i in range(1, index):
            for j in range(i):
                if s[j]*2 > s[i-1]:
                    t1 = j      #找到数值在数组中的位置
                    break
            for j in range(i):
                if s[j]*3 > s[i-1]:
                    t2 = j
                    break
            for j in range(i):
                if s[j]*5 > s[i-1]:
                    t3 = j
                    break
            s.append(min(s[t1]*2, s[t2]*3, s[t3]*5))

        return s

solution = Solution()
s = solution.GetUglyNumber(10)
print(s)

#最短路径和问题
#假设m是m行n列的矩阵，那么我们用dp[m][n]来抽象这个问题，dp[i][j]表示的是从原点到i,j位置的最短路径和。
#我们取左边和上边的较小值，然后加上当前的路径值，就是达到当前点的最短路径。然后从左到右，从上到下依次计算即可。
# m[i][j] = min(m[i-1][j],m[i][j-1]) + p[i][j]


# 此例中有多个相同长度的公共子串，但只能获取第一个子串
def find_lcsubstr(s1, s2): 
    # 下面4行不要直接写在循环中，减少计算
    s1_len = len(s1) + 1 					#为方便后续计算，多了1行1列 
    s2_len = len(s2) + 1
    s3_len = len(s1)
    s4_len = len(s2)
    m = [[0 for j in range(s2_len)] for i in range(s1_len)] #生成0矩阵
    maxNum = 0         #初始最长匹配长度
    p      = 0         #匹配的起始位置
    for i in range(s3_len):
            for j in range(s4_len):
                if s1[i] == s2[j]:                 #相同则累加
                    m[i + 1][j + 1] = m[i][j] + 1  #给相同字符赋值，值为左上角值加1
                if m[i + 1][j + 1] > maxNum:
                    maxNum = m[i + 1][j + 1]       #获取最大匹配长度
                    p = i + 1                      #记录最长匹配长度的终止位置

    return s1[p - maxNum: p], maxNum
