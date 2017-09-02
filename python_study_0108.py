# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0108.py
@time:2017/9/2  15:47
"""
def judge(i,n,a,result,s):
    if i == n:
        return abs(result) == s
    else:
        return (judge(i+1,n,a,result+a[i],s) or judge(i+1,n,a,result-a[i],s))
while True:
    try:
        n = int(raw_input())
        num = map(int, raw_input().strip().split(' '))
        if sum(num) % 2 != 0:
            print "false"
        else:
            num5 = []
            num3 = []
            a = []
            for i in range(n):
                if num[i] % 3 == 0:
                    num3.append(num[i])
                elif num[i] % 5 == 0:
                    num5.append(num[i])
                else:
                    a.append(num[i])
            n = len(a)
            s = abs(sum(num5)-sum(num3))
            if judge(0,n,a,0,s):
                print "true"
            else:
                print "false"
    except:
        break