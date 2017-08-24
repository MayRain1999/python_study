# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_089.py
@time:2017/8/24  20:51
"""
while True:
    try:
        n1 = int(raw_input())
        num1 = map(int, raw_input().split())
        n2 = int(raw_input())
        num2 = map(int, raw_input().split())
        num1.extend(num2)
        num = []
        for i in num1:
            if i not in num:
                num.append(i)
        num.sort()
        string = ''
        for s in num:
            string += str(s)
        print string
    except:
        break

# while True:
#     try:
#         n1 = input()
#         a1 = map(int, raw_input().split())
#         n2 = input()
#         a2 = map(int, raw_input().split())
#         a = list(set(a1 + a2))
#         a.sort()
#
#         print ''.join([str(i) for i in a])
#     except:
#         break