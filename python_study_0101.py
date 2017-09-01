# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0101.py
@time:2017/9/1  22:03
"""
#二进制中1 最多的连续次数
while True:
    try:
        num = int(raw_input())
        str1 = str(bin(num))[2:]
        count = 0
        max1 = 0
        for i in str1:
            if int(i)==0:
                count =0
            else:
                count += 1
                if count > max1:
                    max1 = count
        print max1
    except:
        break