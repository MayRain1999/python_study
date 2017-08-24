# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_086.py
@time: 2017/8/23 11:48
"""
def handle(count, pre_station):
    num = 1
    for i in range(count):
        num *=i
    #循环次数
    a = num - 1
    b = -len(pre_station) -1
    for item in range(a):
        for i in range(-2, b, -1):
            if   pre_station [i] <pre_station[i+1]:
                k  = pre_station[i]
                break
        x = pre_station[i+1:]
        r = [item for item in x if item>k]
        y = min(enumerate(r), key = lambda i:i[1])
        x[y[0]], pre_station[i] = k, y[1]
        pre_station = pre_station[:i+1]+ x[::-1]
        print pre_station
while True:
    try:
        count = input()
        start_arr = raw_input().split()
        result  =[]
        handle(count, start_arr)
    except:
        break