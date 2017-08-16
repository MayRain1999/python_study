# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_058.py
@time: 2017/8/11 20:25
"""
while True:
    try:
        num1 = int(raw_input())
        listNumber= raw_input().split()
        indexNumber =int( raw_input())
        if indexNumber ==0:
            print  0
        else:
            print  listNumber[-indexNumber]
    except:
        break
