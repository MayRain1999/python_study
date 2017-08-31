# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_028.py
@time: 2017/6/29 12:22
"""
import sys
while True:
    try:
        m = int(raw_input())
        d = []
        for i in range(m):
# <<<<<<< HEAD
            d.append(map(int,raw_input().split()))
        print d
        d.sort()
        for  j in d:
            print  j
# =======
            d.append(raw_input())
        d.sort()
        for  j in d:
            print j
# >>>>>>> origin/master
    except:
        break
