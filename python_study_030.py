# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_030.py
@time: 2017/6/30 23:20
"""
import  sys
while True:
    try:
        N, m = map(int, raw_input().split())
        goods = []
        for i in range(m):
            goods.append(map(int, raw_input().split()))
        def func_max(N, m, goods):
            a = [[0]*(N+1) for  _  in range(m+1)]
            for i in range(m+1):
                for j in range(1, N+1):
                    if goods[i-1][0]<=j:
                        a[i][j] = max(a[i - 1][j], a[i - 1][j - goods[i - 1][0]] + goods[i - 1][0] * goods[i - 1][1])
                        print int(a[m][N])
        func_max(N, m, goods)
    except:
        break