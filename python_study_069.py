# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_069.py
@time:2017/8/1517:48
"""
def f(m, n):
    if m<0 or n<0:
        return 0
    elif m ==1 or n ==1:
        return  1
    else:
        return f(m, n-1)+f(m-n, n)
while True:
    try:
        m, n = map(int, raw_input().split())
        print f(m, n)
    except:
        break