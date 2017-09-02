# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0106.py
@time:2017/9/2  14:59
"""
#计算n x m的棋盘格子
def count(n,m):
    if n == 1:
        return m+1
    if m == 1:
        return n+1
    return count(n-1,m)+count(n,m-1)
while True:
    try:
        line = raw_input().split()
        n = int(line[0])
        m = int(line[1])
        print count(n,m)
    except:
        break