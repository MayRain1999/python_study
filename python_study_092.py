<<<<<<< Updated upstream
# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_092.py
@time: 2017/8/26 20:17
"""
# 360面试题 2 跳水分数问题
while True:
    try:
        num = int(raw_input())
        arr = map(int, raw_input().split())
        result = []
        for i in range(num):
            if i ==0:
                result.append(0)
            else:
                m =0
                for j in range(i):
                    if arr[j] >arr[i]:
                        m = m+1
                result.append(m)
        for i in result:
            print i,
=======
# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_092.py
@time:2017/8/25  17:29
"""
# 二维数组操作
while True:
    try:

>>>>>>> Stashed changes
    except:
        break