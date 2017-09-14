# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0123.py
@time:2017/9/14  8:25
"""
# 约瑟夫循环问题

def josephus(n, k):
    #生成一个列表
    listN = range(n)
    k  = k - 1
    m = k%n
    print m
    while(len(listN) > 2):
        del listN[k]
        k = (k +m )%len(listN)
        # print  k
        print listN
    return listN[0],listN[1]

if __name__ == "__main__":
    while True:
        try:
            # n 个人
            n = int(raw_input())
            # 每隔K个人 退出一个人
            k = int(raw_input())
            #约瑟夫环问题
            print josephus(n, k)
        except:
            break