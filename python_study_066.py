# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_066.py
@time: 2017/8/13 18:48
"""
while True:
    try:
        input_string =raw_input()
        for i in input_string:
            if  input_string.count(i) ==1:
                print i
                break
        else:
            print -1
    except:
        break