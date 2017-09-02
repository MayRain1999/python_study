# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0109.py
@time:2017/9/2  16:09
"""
#选票计算
while True:
    try:
        n = int(raw_input().strip())
        voteds = raw_input().strip().split(' ')
        m = int(raw_input().strip())
        votes = raw_input().strip().split(' ')
        dicvoteds = {}
        for name in voteds:
                dicvoteds[name] = 0
        notvotedname = []
        for name in votes:
            if name in dicvoteds:
                dicvoteds[name] += 1
            else:
                notvotedname.append(name)
        for name in voteds:
            print('%s : %d' % (name, dicvoteds.get(name)))
        print('Invalid : %d' % len(notvotedname))
    except:
        break
