# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0114.py
@time:2017/9/6  20:35
"""
# 喝水问题 不全
while True:
    try:
        n, m= map(int, raw_input().split())
        arr = map(int, raw_input().split())
        res =0
        for i in range(arr):
            res = res + arr[i]
        print arr
    except:
        break