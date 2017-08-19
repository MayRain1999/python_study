# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_075.py
@time:2017/8/19  20:12
"""

while True:
    try:
        nravg = raw_input()
        n, r, avg = map(int, nravg.split(' '))
        nums = []
        alls = n*avg
        used = 0
        for i in range(n):
            tp = [int(i) for i in raw_input().strip().split(' ')]
            nums.append(tp)
            used += tp[0]
        alls -= used
        need = 0
        nums.sort(key=lambda p:p[1])
        if alls >0:
            for i in range(n):
                curNeed = min(alls,r-nums[i][0])
                alls -= curNeed
                need += curNeed * nums[i][1]
                if alls ==0:
                    break
            print need
        else:
            print 0
    except:
        break