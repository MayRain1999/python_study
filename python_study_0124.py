# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0124.py
@time:2017/9/20  15:49
"""
while True:
    try:
        n  = int(raw_input())
        A = []
        B  = []
        for i in range(n):
            A.append(int(raw_input()))
        for i in range(len(A)-1):
            tem = A[i]+A[i+1]
            B.append(tem)
        B.append(A[n-1])
        for i in B:
            print i
    except:
        break



