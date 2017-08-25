# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_091.py
@time:2017/8/24  21:59
"""
#分数分解为埃及分数序列
# 设a、b为互质正整数，a<b 分数a/b 可用以下的步骤分解成若干个单位分数之和：
# 步骤一：用b除以a，得商数q及余数r（r=b-a*q）
# 步骤二：a/b = 1/(q+1) + (a-r)/(b(q+1）)
# 步骤三：对于(a-r)/(b(q+1)),重复一和二，直到分解完毕

from fractions import gcd
# 最大公约数的函数gcd

def realNumber(a, b):
    GCD = gcd(a, b)
    a //=GCD
    b //=GCD
    result = []
    while (b % a != 0):
        q = b // a
        crnt = q + 1
        res = '1/' + str(crnt)
        result.append(res)
        a = a * (q + 1) - b
        b = b * (q + 1)
    crnt = b // a
    res = '1/' + str(crnt)
    result.append(res)
    return '+'.join(result)

while True:
    try:
        a, b = map(int, raw_input().split('/'))
        print realNumber(a, b)
    except:
        break