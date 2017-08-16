# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_047.py
@time: 2017/7/27 20:30
"""
while True:
    try:
        a = int(raw_input())
        if a == '':
            break
        b = 2*2*a*(1-(0.5)**5)-a
        print b
        print a*(0.5)**5
    except:
        break