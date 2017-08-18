# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_071.py
@time: 2017/8/18 23:27
"""
# 查找最长的公共子串
while True:
    try:
        str1 = raw_input()
        str2 = raw_input()
        if len(str1) < len(str2):
            str_short = str1
            str_long = str2
        else:
            str_short = str2
            str_long = str1
        li = []
        length = []
        for i in range(len(str_short)):
            for j in range(i+2, len(str_short) + 1):
                s = str_short[i:j]
                if s in str_long:
                    li.append(s)
                    length.append(len(s))
        maxl = max(length)
        for i in  range(len(li)):
            if length[i]==maxl:
                print li[i]
                break
    except:
        break
