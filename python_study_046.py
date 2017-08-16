# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_046.py
@time: 2017/7/27 20:17
"""
# 统计兔子总数
while True:
    try:
        monthNumber = int(raw_input())
        if monthNumber<3:
            print 1
        else:
            a = 1
            b = 1
            for i in range(3, monthNumber+1):
                a, b= b, a+b
            print b
    except:
        break
