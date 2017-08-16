# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_041.py
@time: 2017/7/18 15:19
"""
m = raw_input()
for i in m:
    if not i.isalpha():
        m = m.replace(i, ' ')
m = m.split()[::-1]
print ' '.join(m)