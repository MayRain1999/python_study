# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_076.py
@time:2017/8/20  9:36
"""
# 24 点游戏算法
def trans(num, x):
    total = 0
    if len(x) ==1:
        if  abs(num - x[0])<0.01:
            return 1
        else:
            return 0
    else:
        for i in xrange(len(x)):
            a = x[i]
            b = x[:]
            b.pop(i)
            total = total + (trans(num -a, b) +trans(num+a, b) +
                             trans(num*a, b) + trans(num/a, b))
            return total

while True:
    try:
        nums = raw_input().split()
        num = [float(x) for x in nums]
        total = trans(24.0, num)
        if total ==0:
            print False
        else:
            print True
    except:
        break