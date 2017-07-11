# -*- coding: utf-8 -*-
import sys
while True:
    try:
        n = int(sys.stdin.readline())
        d = {}
        for i in range(n):
            k, v = map(int, sys.stdin.readline().split(''))
            d[k] = d.setdefault(k, 0) +v
        for k in sorted(d.keys()):
            print k, str(d[k])
    except:
        break