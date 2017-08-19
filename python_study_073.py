# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_073.py
@time:2017/8/19  19:27
"""
while True:
    try:
        m = int(raw_input())
        n = raw_input().split()
        n = list(set(n))
        n  = [int(x) for x in n ]
        n.sort()
        print len(n)
        for i in n:
            print i,
    except:
        break