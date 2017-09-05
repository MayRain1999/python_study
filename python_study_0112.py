# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0112.py
@time:2017/9/4  17:42
"""
#找出数组里每个最大值 并输出
while True:
    try:
        lineNum = int(raw_input())
        arr = []
        result  = []
        for i in range(lineNum):
            arr.append(map(int, raw_input().split()))
        print arr
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                key  = 0
                if arr[i][j] > key:
                    key = arr[i][j]
            result.append(key)
        for i in result:
           print i,
        #print result
    except:
        break