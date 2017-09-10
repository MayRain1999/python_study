# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_0118.py
@time: 2017/9/10 9:42
"""
#大疆笔试题  水桶水位问题
while True:
    try:
        H, x, y, h, s=map(float,raw_input().split())
        t = h/x
        res = 0
        if y>=x:
            if s>=t:
                res = h
            else:
                res = s*x
        else:
            if s>=t:
                res = (s-t)*(x-y)+h
                if res>H:
                    res=H
            else:
                res = s * x
        print int(round(res))
    except:
        break