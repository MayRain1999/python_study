# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_099.py
@time:2017/9/1  20:37
"""
#判断大写字母个数
while True:
    try:
        string = raw_input()
        num = 0
        for s in string:
            if 'A' <= s <= 'Z':
                num += 1
        print num
    except:
        break
