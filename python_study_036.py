<<<<<<< HEAD
# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_036.py
@time: 2017/7/11 23:44
=======
# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_036.py
@time:2017/7/1319:35
>>>>>>> origin/master
"""
while True:
    try:
        s = raw_input()
<<<<<<< HEAD
        temp = list(s)
        str1 = filter(lambda x:x.isalpha(), list(s))
        str1.sort(key = str.upper)
        j = 0
        for i in range(len(temp)):
            if temp[i].isalpha():
                temp[i] = str1[j]
                j+=1
        print ''.join(temp)
    except:
        break
=======
        k = int(raw_input())
        l = 0
        m =[]
        if len(s)<k:
            print s[::-1]
        f k<= len(s)<2*k:

>>>>>>> origin/master
