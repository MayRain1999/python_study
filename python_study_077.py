# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_077.py
@time:2017/8/20  21:31
"""
while True:
    try:
        a = input()
        b = input()
        c = list()
        for i in range(a):
            c.append(raw_input())
        if b == 0:
            for i in sorted(c, key=lambda a: int(a.split()[1]), reverse=True):
                print i
        else:
            for i in sorted(c, key=lambda a: int(a.split()[1])):
                print i
    except:
        break