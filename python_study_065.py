# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_065.py
@time: 2017/8/13 17:36
"""
while True:
    try:
        a, b = map(int, raw_input().split())
        arrNum =map(int,raw_input().split())
        arrNum.sort()
        c = arrNum[:b]
        for i in c:
            print i,
    except:
        break