# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_082.py
@time:2017/8/22  13:31
"""
while True:
    try:
        m = raw_input().split()
        print len(m)
        for i in m:
            print i
    except:
        break