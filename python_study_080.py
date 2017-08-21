# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_080.py
@time:2017/8/21  15:51
"""
#1、 正则表达式解法
# import re
# while True:
#     try:
#         a=raw_input().strip()
#         b=raw_input().strip()
#         a=a.replace('*','[1-9a-zA-Z]*').replace('?','.')
#         c=re.findall(a,b)
#         c=''.join(c)
#         if c==b:
#             print 'true'
#         else:
#             print 'false'
#     except:
#         break

# 2 递归解法
def match(text1, i, text2, j):
    """
    p: 匹配模式
    s: 待匹配字符串
    i,j当前匹配字符的下标
    匹配完毕之后，i,j应该等于各自长度
    """
    if len(text1) == i and len(text2)==j :
        return True
    elif len(text1) <= i or len(text2) <= j :
        return False
    elif text1[i] == text2[j]:
        return match(text1, i+1, text2, j+1)
    elif text1[i] == '*' :
        # 此时匹配情况有不匹配/匹配一次/匹配多次
        return match(text1, i, text2, j+1) or match(text1, i+1, text2, j+1) or match(text1,i+1, text2,j)
    elif text1[i] == '?' :
        return match(text1, i+1, text2, j+1)
    else:
        return False
while True:
    try:
        text1 = raw_input().strip()
        text2 = raw_input().strip()
        if not text1 or not text2:
            break
            # 判断是不是空值
        if match(text1, 0, text2, 0 ):
            print 'true'
        else:
            print 'false'
    except:
        break

# 动态规划算法
# while True:
#     try:
#         string1=raw_input()
#         string2=raw_input()
#         l1=len(string1)
#         l2=len(string2)
#         dp=[[False]*(l2+1) for _ in range(l1+1)]
#         dp[0][0]=True
#         if string1[0]=='*':
#             dp[1][0]=True
#         for i in range(1,l1+1):
#             for j  in range(1,l2+1):
#                 if string1[i-1]=='*':
#                     dp[i][j]=dp[i][j-1] or dp[i-1][j]
#                 elif string1[i-1]=='?':
#                     dp[i][j]=dp[i-1][j-1]
#                 else:
#                     dp[i][j]=dp[i-1][j-1] and string1[i-1]==string2[j-1]
#         if  dp[l1][l2]==True:
#             print 'true'
#         else:
#             print 'false'
#     except:
#         break
