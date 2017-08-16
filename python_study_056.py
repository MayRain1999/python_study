# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_056.py
@time: 2017/8/4 23:55
"""
# 从单向链表中删除指定值的节点

while True:
    try:
        a = []
        s = raw_input().split()
        Node = int(s[0])
        a.append(int(s[1]))
        k =2
        for i in range(Node -1):
            m, n = int(s[k]), int(s[k+1])
            a.insert(a.index(n)+1, m)
            k +=2
        a.remove(int(s[-1]))
        for i in a[:-1]:
            print i,
        print a[-1],
        print ''
    except:
        break