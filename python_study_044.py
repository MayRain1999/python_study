# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_044.py
@time: 2017/7/20 22:57
"""
# 图片整理排序
while True:
    try:
        str1 = raw_input()
        list1 = list(str1)
        list1.sort()
        result  = ''
        for s in list1:
            result+=s
        print result
    except:
        break