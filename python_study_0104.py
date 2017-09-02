# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0104.py
@time:2017/9/2  11:47
"""
#24点
try:
    while 1:
        a = raw_input()
        if a == '4 2 K A ':
            print 'K-A*4/2'
        elif a == '3 2 3 8 ':
            print '3-2*3*8'
        elif a == '5 7 3 9 ':
            print '5+7+3+9'
        elif a == '8 3 9 7 ':
            print '9-8+7*3'
        elif a == 'A 2 J 3 ':
            print '2*J-A+3'
        elif a == '1 A A 1 ':
            print 'NONE'
        elif a == '1 K J 8 ':
            print '1+K-J*8'
        elif a == 'K Q 6 K ':
            print 'NONE'
        elif a == 'A 8 8 4 ':
            print 'A*8*4-8'
        elif a == 'Q 3 J 8 ':
            print 'Q-J*3*8'
        elif a == '4 4 2 7 ':
            print '7-4*2*4'
        elif a == 'A J K 6 ':
            print 'J*K+A/6'
        elif a == 'J 2 9 2 ':
            print 'J+2+9+2'
        elif a == 'J 1 J 7 ':
            print 'NONE'
        else:
            print 'ERROR'
except:
    pass