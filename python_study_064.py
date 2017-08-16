# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_064.py
@time: 2017/8/13 17:20
"""
def perfect(N):
    ll = []
    if N==None or N<=0 or N>=500000:
        print  -1
    else:
        for i in range(1,N+1):
            l = [1]
            for j in range(2,i//2 +1):
                if i%j==0:
                    l.append(j)
            if sum(l)==i:
                ll.append(i)
        print len(ll)-1
while True:
    try:
        N  = int(raw_input())
        perfect(N)
    except:
        break