# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_061.py
@time: 2017/8/12 15:33
"""
while True:
    try:
        stringNumber = list(raw_input())
        str1 = []
        n = 1
        f_ch = stringNumber[0]
        for i in range(len(stringNumber)):
            m = i+1
            if m<= len(stringNumber)-1:
                if stringNumber[m]!=stringNumber[i]:
                    n +=1
                else:
                    str1.append(n)
                    n=0
                    f_ch = stringNumber[m]
            else:
                str1.append(n)
        print max(str1)
    except:
        break