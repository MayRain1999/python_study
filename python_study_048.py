# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_048.py
@time: 2017/7/31 11:54
"""
# 判断两个IP是否属于同一子网
while True:
    try:
        ip= raw_input( ).split('.')
        ip1 = raw_input( ).split('.')
        ip2 = raw_input( ).split('.')
        if len(ip1) == len(ip2) == 4:
            total = ip + ip1 + ip2
            for t in total:
                if int(t) not in range(0, 256):
                    print 1
        else:
            print 1

        for k in xrange(0, 4 - len(ip)):
            mask.append('0')
        for i in xrange(0, len(ip)):
            sub1 = int(ip[i]) & int(ip1[i])
            sub2 = int(ip[i]) & int(ip2[i])
            if ip1 != ip2:
                print 2
                break
            print 0
    except:
        break