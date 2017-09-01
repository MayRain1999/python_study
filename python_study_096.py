# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_096.py
@time:2017/9/1  15:41
"""
# 斐波那契（Fibonacci）数列的第n项
# 递归解法（效率很低）
def long_Fibonacci(n):
    if n<=0:
        return 0
    elif n ==1:
        return 1
    else:
        return long_Fibonacci(n-1) + long_Fibonacci(n-2)

while True:
    try:
        n = input()
        print long_Fibonacci(n)
    except:
        break