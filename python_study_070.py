# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_070.py
@time:2017/8/17 11:05
"""
while True:
    try:
        n = int(raw_input())
        a = range(n + 1)
        order = raw_input()

        head, tail, i = 1, 4, 1
        if n <= 4:
            for s in order:
                if s == 'U':
                    if i == 1:
                        i = n
                    else:
                        i -= 1
                else:
                    if i == n:
                        i = 1
                    else:
                        i += 1
            head, tail = 1, n
        else:
            for s in order:
                if s == 'U':
                    if i == 1:
                        i = n
                        head, tail = n - 3, n
                    else:
                        i -= 1
                        if i < head:
                            head, tail = i, i + 3
                else:
                    if i == n:
                        i = 1
                        head, tail = 1, 4
                    else:
                        i += 1
                        if i > tail:
                            head, tail = i - 3, i
        ans = range(head, tail + 1)
        print ' '.join([str(j) for j in ans])
        print i
    except:
        break