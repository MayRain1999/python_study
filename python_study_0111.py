# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0111.py
@time:2017/9/2  16:40
"""
#在数字前面加上*
while True:
    try:
        string=list(raw_input())
        i=0
        while i<len(string):
            if string[i].isdigit():
                tmp=1
                try:
                    while string[i+tmp].isdigit():
                        tmp+=1
                except:
                    pass
                string.insert(i+tmp,'*')
                string.insert(i,'*')
                i+=tmp+2
            else:
                i+=1
        print ''.join(string)
    except:
        break
