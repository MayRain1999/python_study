# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_0120.py
@time: 2017/9/10 19:30
"""
#爱奇艺 编程题3 数字重复 比大小
def repeat1(x,k):
    y= x*k
    return y

while True:
    try:
        m= raw_input().split()
        x1 =m[0]
        k1 =int(m[1])
        x2 =m[2]
        k2 =int(m[3])
        v1 = repeat1(x1,k1)
        v2 = repeat1(x2,k2)
        print v1,v2
        if int(v1) ==int(v2):
           print "Equal"
        elif int(v1) >int(v2):
           print "Greater"
        else:
           print "Less"
    except:
        break