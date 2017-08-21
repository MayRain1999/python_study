# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_079.py
@time:2017/8/21  11:38
"""
# 矩阵乘法的运算量
while True:
    try:
        lines = input()
        # 输入行数
        arr = []
        for i in range(lines):
            arr.append(map(int, raw_input().split()))
        # 输入的矩阵的行列
        exp = raw_input()
        res = 0
        arrTemp = []
        # 矩阵的运算表达式
        for  i in exp:
            if i == "(":
                pass
            # 判断括号
            elif i ==")":
                try:
                    b = arrTemp.pop()
                    a = arrTemp.pop()
                    res += a[0]*a[1]*b[1]
                    arrTemp.append([a[0], b[1]])
                # 提取括号的内容并进行运算
                # pop（）方法 默认删除最后一个值 并且返回这个值
                except :
                    break
            else:
                arrTemp.append(arr[ord(i) - 65])
        print res
    except:
        break