# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_063.py
@time:2017/8/1221:31
"""
def perfect(N):
    perfectNumber=[]
    for i in range(5,N):
        sum1 = 0
        for j in range(1,i//2 + 1):
            if i%j == 0:
                sum1 += j
        if sum1 == i:
            perfectNumber.append(i)
        return perfectNumber

while True:
    try:
        N  = input()
        print perfect(N)
    except:
        break
