# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_090.py
@time:2017/8/24  21:27
"""
while True:
    try:
        short_string = raw_input()
        long_string = raw_input()
        num = 0
        for i in short_string:
            if i in long_string:
                num  = num +1
        if num == len(short_string):
            print 'true'
        else:
            print 'false'
    except:
        break
