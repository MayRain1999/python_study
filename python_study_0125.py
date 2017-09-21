# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0125.py
@time:2017/9/20  16:08
"""
while True:
    try:
        s1 = raw_input()
        s2 = raw_input()
        if len(s1)>len(s2):
            print len(s2)
        else:
            print  len(s1)
    except:
        break
