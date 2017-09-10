# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_0119.py
@time: 2017/9/10 19:22
"""
#爱奇艺 编程题 求RG的涂色的最少次数
while True:
    try:
        s = raw_input()
        s1 = s.count("R")
        s2 = s.count("G")
        res = 0
        for i in range(s1):
            if s[i] != "R":
                res = res+1
        for i in range(s1,len(s)):
            if s[i] != "G":
                res = res +1
        res1 = len(s) - s1
        res2 = len(s) - s2
        print min(res, res1,res2)
    except:
        break
