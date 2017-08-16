# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_050.py
@time: 2017/7/31 20:28
"""
# 称砝码
while True:
    try:
        n = input()
        m = map(int, raw_input().split())
        p = map(int, raw_input().split())
        diff = {0}
        for i in  range(n):
            temp = diff.copy()
            for j in range(p[i]):
                for k in temp:
                    d = k+m[i]*(j+1)
                    if d not in temp:
                        diff.add(d)
        print len(diff)
        print  diff
    except:
        break