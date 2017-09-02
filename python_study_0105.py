# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0105.py
@time:2017/9/2  11:55
"""
#合法ip
#
while True:
    try:
        inIP= raw_input().split('.')
        flag = 0
        for i in inIP:
            if int(i) >= 0 and int(i) <= 255:
                pass
            else:
                flag = 1
        if flag == 0:
            print 'YES'
        else:
            print 'NO'
    except:
        break