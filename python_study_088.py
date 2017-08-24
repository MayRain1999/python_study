# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_088.py
@time:2017/8/24  19:54
"""
# 动态规划算法

def similarity(stringA, stringB):
    a = len(stringA) + 1
    b = len(stringB) + 1
    arr = [[0]*(a) for i in range(b)]
    for i in range(a):
        arr[0][i] = i
    for i in range(b):
        arr[i][0] = i
    for i in range(1, b):
        for j in range(1, a):
            x = arr[i -1][j] + 1
            y = arr[i][j-1] + 1
            if stringA[j-1] == stringB[i-1]:
                change =0
            else:
                change=1
            z = arr[i-1][j-1] +change
            arr[i][j] = min(x, y, z)
    print "1/" + str(arr[b - 1][a - 1] + 1)
while True:
    try:
        stringA =raw_input()
        stringB =raw_input()
        similarity(stringA, stringB)
    except:
        break