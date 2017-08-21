# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_078.py
@time:2017/8/20  22:05
"""
# 矩阵的乘法
while True:
    try:
        x  = input()
        y  = input()
        z  = input()
        m1 = []
        m2 = []
        for i in range(x):
            m1.append(map(int, raw_input().split()))
        for i in range(y):
            m2.append(map(int, raw_input().split()))
        res = []
        for i in range(x):
            tmp = []
            m1m1 = m1[i]
            for j in range(z):
                tmp_1 = 0
                m2m2 = [x[j] for x in m2]
                for k in range(y):
                    tmp_1 +=m1m1[k]*m2m2[k]
                tmp.append(tmp_1)
            res.append(tmp)
        for s in res:
            print ' '.join(str(ss) for ss in s)
    except:
        break