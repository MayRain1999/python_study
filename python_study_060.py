# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_060.py
@time: 2017/8/12 11:44
"""
while True:
    try:
        n = int(raw_input())
        m = -1
        if  n <= 2:
            m = -1
        elif n%2 ==1:
            m = 2
        elif n%4 ==0:
            m = 3
        else:
            m = 4
        print m
    except:
        break