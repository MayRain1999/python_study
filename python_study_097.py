# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_097.py
@time: 2017/8/26 15:59
"""
# 滴滴笔试题，找出第K大的数
while True:
    try:
        arr= map(int, raw_input().split())
        k = int(raw_input())
        set(arr)
        arr.sort()
        arr.reverse()
        print arr
        print arr[k-1]
    except:
        break