# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_086.py
@time: 2017/8/23 11:48
"""
def handle(count, pre_station,after_station):
    num = 1
    for i in range(count):
        num *=i
    #循环次数
    a = num - 1
    b = -len(start_arr) -1
    for i in range(num):
        for j in range(-2, b, -1):
            if   pre_station [j] <pre_station[j+1]:
                k  = pre_station[j]
                break
        x = pre_station[i+1:]
        r = [i for i in x if i>k]
        y = min(enumerate(r), key = lambda j:j[1])
        x[y[0]], pre_station[j] = k, y[1]
        after_station = pre_station[:i+1]+ x[::-1]
        print after_station
while True:
    try:
        count = input()
        start_arr = map(int, raw_input().split())
        result  =[]
        handle(count, start_arr)
    except:
        break