# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_057.py
@time: 2017/8/8 22:51
"""

while True:
    try:
        str2= list(raw_input())
        str1 = []
        n =1
        f_ch = str2[0]
        for i in range(len(str2)):
            m = i+1
            if  m <= len(str2)-1:
                if str2[m] == str2[i]:
                    n += 1
                else:
                    str1.append(str(n)+ ""+ f_ch)
                    n = 1
                    f_ch = str2[m]
            else:
                str1.append(str(n)+"" + f_ch )
        print ''.join(str1)
    except:
        break