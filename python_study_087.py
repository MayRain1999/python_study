# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_087.py
@time: 2017/8/24 15:39
"""
count = input()
l = map(int,raw_input().split())
result = [l]
# result.append(l)
n=1
for i in l:
    n *=i
n,m = n-1, -len(l)-1
for item in range(n):
    for i in range(-2, m, -1):
        if l[i] < l[i+1]:
            k = l[i]
            break
    x = l[i+1:]
    r = [item for item in x if item>k]
    y = min(enumerate(r), key = lambda i:i[1])
    x[y[0]], l[i] = k, y[1]
    l =l[:i+1] +x[::-1]
    result.append(l)
for i in result:
    for j in i:
        print j,
    print