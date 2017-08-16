# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_043.py
@time: 2017/7/19 23:41
"""
def encode(str0):
    li = map(int, str0.split('.'))
    str1 = ''
    for s in li:
        s1 = bin(s)[2:]
        s1 = (8-len(s1) )* '0' +s1
        str1 +=s1
    int0 = int(str1, base = 2)
    return int0

def decode(int0 ):
    bin0 = bin(int0)[2:]
    n = len(bin0)/8
    length = 8*(n+1)
    bin1 = (length-len(bin0))*'0' + bin0

    if  len(bin0)%8 !=0:
        m=0
    else:
        m=1
    li  = []
    for i in range(m, n+1):
        s = bin1[8*i: 8*i +8]
        int1 = int(s, base = 2)
        li.append(str(int1))
    str1 = '.'.join(li)
    return str1

while True:
    try:
        ip1 = str(raw_input())
        ip2 = int(raw_input())
        ip1_c = encode(ip1)
        ip2_c = decode(ip2)
        print ip1_c
        print ip2_c
    except:
        break