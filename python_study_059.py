# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_059.py
@time: 2017/8/12 0:08
"""
def string_Distance(a,b):
    m = len(a)+1
    n = len(b)+1
    dp = [[0]* n for i in range(m)]
    for i in range(m):
        dp[i][0] = i
    for i in range(n):
        dp[0][i] = i
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if a[i-1]==b[j-1] else 1
            substitution = dp[i-1][j-1] +cost
            deletion = dp[i-1][j] + 1
            insertion = dp[i][j-1] + 1
            dp[i][j] = min(substitution, deletion, insertion)
    return  dp[m-1][n-1]

while True:
    try:
        a = raw_input()
        b = raw_input()
        print  string_Distance(a,b)
    except:
        break