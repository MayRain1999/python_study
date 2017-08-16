# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_068.py
@time:2017/8/1510:37
"""
# 任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，
# 本题目要求输出组成指定偶数的两个素数差值最小的素数
# 在一般领域，对正整数n，如果用2到 根号n之间的所有整数去除，
# 均无法整除，则n为质数。
# 质数大于等于2 不能被它本身和1以外的数整除

def  is_perfer(N):
    if N == 1:
        return False
    i = 2
    while i*i <= N:
        if N%i ==0:
            return False
        i = i+1
    return  True
while True:
    try:
        N = input()
        for i in xrange(N/2, N):
            if is_perfer(i) and is_perfer(N - i):
                print N-i
                print i
                break
    except:
        break