# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0107.py
@time:2017/9/2  15:41
"""
# 最长连续数字子串
while True:
    try:
        line = raw_input()
        digitline = ''
        maxcount = 0
        res = ''
        for i in line:
            if i.isdigit():
                digitline += i
            else:
                digitline += '#'
        digitArray = digitline.split('#')
        for i in digitArray:
            maxcount = max(maxcount,len(i))
        for i in digitArray:
            if len(i) == maxcount:
                res += i
        print res+','+str(maxcount)
    except:
        break