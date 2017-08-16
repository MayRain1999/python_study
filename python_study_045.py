# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_045.py
@time: 2017/7/23 11:29
"""
# 字符串密
while True:
    try:
        lineKey = raw_input()
        line = raw_input()
        code = []
        res = ''
        for i in lineKey:
            if i not in code:
                code.append(i)
        for i in range(97,123):
             if chr(i) not in code:
                 code.append(chr(i))
        for i in line:
            res += code[ord(i) - 97]
        print  res
    except:
        break