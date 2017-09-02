# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0103.py
@time:2017/9/2  10:43
"""
#扑克牌大小
while True:
    try:
        line = raw_input().split('-')
        line0 , line1 = line[0].split() , line[1].split()
        def transJQKA2(line):
            for i in range(len(line)):
                if line[i] == 'J':
                    line[i] = 11
                if line[i] == 'Q':
                    line[i] = 12
                if line[i] == 'K':
                    line[i] = 13
                if line[i] == 'A':
                    line[i] = 14
                if line[i] == '2':
                    line[i] = 15
            return line
        line0 , line1 = transJQKA2(line0) , transJQKA2(line1)
        if line[0] == 'joker JOKER' or line[1] == 'joker JOKER':
            print 'joker JOKER'
        elif len(line0) == len(line1):
            if int(line0[0]) > int(line1[0]):
                print line[0]
            else:
                print line[1]
        elif len(line0) == 4:
            print line[0]
        elif len(line1) == 4:
            print line[1]
        else:
            print 'ERROR'
    except:
        break