# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_035.py
@time:2017/7/1122:15
"""
while True:
    try:
        line = raw_input().split()
        count = 0
        res = []
        for i in range(int(line[0])):
            if line[-2] != line[1+i] and sorted(line[-2])==sorted(line[1+i]):
                count +=1
                res.append(line[1+i])
        res.sort()
        print count
        if count >= int(line[-1]):
            print  res[int(line[-1])-1]
    except:
        break