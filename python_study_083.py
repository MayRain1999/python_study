# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_083.py
@time:2017/8/22  17:21
"""
# 验证尼科彻斯定理，即：
# 任何一个整数m的立方都可以写成m个连续奇数之和
# 首项是n*n -n+1  长度为n的等差数列
while True:
    try:
        m = int(raw_input())
        num = m**2 - n + 1
        string = str(num)
        for i in range(1,m):
            num = num + 2
            string = string + '+' + str(num)
        print string
    except:
        break