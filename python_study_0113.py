# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0113.py
@time:2017/9/6  19:10
"""
# 最长子串
while True:
    try:
        line = raw_input()
        digitline = ''
        num =0
        maxcount = 0
        res = []
        for i in line:
            if i.isdigit():
                digitline += i
                num +=1
            else:
                digitline += ' '
        digitArray = digitline.split(' ')
        if num ==0:
            print ""
        else:
            for i in digitArray:
                maxcount = max(maxcount,len(i))
            for i in digitArray:
                if len(i) == maxcount:
                    res.append(i)
            print res[-1]
            print maxcount
    except:
        break