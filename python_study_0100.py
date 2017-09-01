# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0100.py
@time:2017/9/1  21:04
"""
# 字符的截取 ABA ABBA形式
# while True:
#     try:
#         s = raw_input()
#         s1 = s[::-1]
#         f = 0
#         for i in range(1,len(s)+1)[::-1]:
#             if f == 1:
#                 break
#             for j in range(len(s)+1-i):
#                 ts = s[j:j+i]
#                 # print i,j,ts
#                 if s1.count(ts) > 0 and ts == ts[::-1]:
#                     print i
#                     f = 1
#                     break
#     except:
#         break

# 另外一种解法 ：
# 先把字符串反转，求最大的公共子串

# 动态规划算法
def dp_main(s1,s2):
    #生成矩阵，方便后面进行计算
    arr  = [[0 for i in range(len(s2)+1)] for j in range(len(s2)+1) ]
    res = 0
    for i in range(len(s1)):
        for j  in range(len(s2)):
            if s1[i] == s2[j]:
                arr[i+1][j+1] = arr[i][j] + 1
                if arr[i+1][j+1] > res:
                    res = arr[i+1][j+1]
    return res
while True:
    try:
        s1 = raw_input()
        s2 = s1[::-1]
        # print s1
        # print s2
        print dp_main(s1, s2)
    except:
        break