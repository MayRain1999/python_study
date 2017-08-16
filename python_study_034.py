# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_034.py
@time: 2017/7/11 11:09
"""
while True:
    try:
        s = raw_input()
        t = list(s)
        numlist = []
        resullt = []
        for i in t:
            numlist.append(t.count(i))
        minlist = min(numlist)
        for j in range(len(s)):
            if numlist[j] !=minlist:
                resullt.append(t[j])
        resullt = ''.join(resullt)
    except:
        print resullt
        break
