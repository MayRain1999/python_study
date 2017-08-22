# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_081.py
@time:2017/8/22  12:41
"""
# 计算日期到天数的转换
while True:
    try:
        year, month, day = map(int, raw_input().split())
        day_number = 0
        arr1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        arr2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if  (year%4==0 and year%100!=0) or year%400==0:
            for i in range(month-1) :
                day_number += arr2[i]
            day_number += day
        else:
            for i in range(month-1):
                day_number += arr1[i]
            day_number += day
        print day_number
    except:
        break

