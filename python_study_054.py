# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_054.py
@time: 2017/8/2 8:07
"""
while True:
    try:
        m, n = map(int, raw_input( ).split( ))
        p = []
        q = []
        k = []
        l = []
        arr = [[0 for i in range(2)] for j in range(m)]
        for i in range(m) :
            arr[i][0], arr[i][1] = map(int, raw_input( ).split( ))
            p.append(arr[i][0])
            q.append(arr[i][1])
        key0 = p[0]
        value0 = q[0]
        for i in range(m):
            diff = p[i] - key0 - 1
            if diff >= 0 :
                for j in range(diff+1) :
                    key1 = key0 + j
                    value1 = value0 +(q[i]-value0)/(p[i] - key0)*j
                    j = j+1
                    k.append(key1)
                    l.append(value1)
                key0 = p[i]
                value0 = q[i]
            elif diff == -1:
                continue
            else :
                key0 = p[i]
                value0 = q[i]
        for i in range(len(k)):
            print  k[i], l[i]
    except:
        break