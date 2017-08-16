# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_049.py
@time: 2017/7/31 20:19
"""
while True:
    try:
        str = raw_input()
        a = b = c  = d = 0
        for i in str:
            if i.isalpha():
                a  = a+1
            elif i==' ':
                b = b+1
            elif i.isdigit():
                c = c+1
            else:
                d = d+1
        print a
        print b
        print c
        print d
    except:
        break