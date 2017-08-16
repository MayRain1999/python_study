# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_053.py
@time: 2017/8/1 16:12
"""
# 漂亮度名字

while True:
    try:
        n=input()
        for i in range(n):
            name=raw_input().strip()
            w=set(list(name))
            d={}
            for x in w:
                d[x]=name.count(x)
            e=sorted(d.iteritems(),key=lambda x:x[1],reverse=True)
            result=0
            for i in range(len(e)):
                result+=e[i][1]*(26-i)
            print result
    except:
        break