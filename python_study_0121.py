# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_0121.py
@time: 2017/9/10 21:34
"""
#爱奇艺编程题 最长周长的三角形
while True:
    try:
        s1=raw_input().split()
        print s1
        s = []
        for i in s1:
            s.append(int(i))
        s.sort()
        print s
        if s[0]+s[1]>s[2]:
            print s[0]+s[1]+s[2]
        else:
            print s[1]+s[2]
    except:
        break
