# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_062.py
@time: 2017/8/12 15:53
"""
while True:
    try:
        x, f, d, p = map(int, raw_input( ).split( ))
        n = 0
        while f>0 and d>=x:
            f = f -1
            d = d-x
            n = n+1
        while f==0 and d >= x+p:
            d = d-x-p
            n =n+1
        print n
    except:
        break