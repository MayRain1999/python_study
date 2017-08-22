# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_084.py
@time:2017/8/22  17:23
"""

# 动态规划算法解决 最长公共子串
def main(s1, s2):
    m = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)]
    # 生成0矩阵，为方便后续计算，比字符串长度多了一列
    res = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i + 1][j + 1] = m[i][j] + 1
                if m[i + 1][j + 1] > res:
                    res = m[i + 1][j + 1]
    return res
while True:
    try:
        s1 = raw_input().lower()
        s2 = raw_input().lower()
        print main(s1, s2)
    except:
        break