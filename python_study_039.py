# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_039.py
@time:2017/7/3121:49
"""
def covert(n):
    a1 = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve'
    ,'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    a2 = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    result = ""
    if (n//10**2 !=0):
        result+= a1[n//10**2]+ " hundred"
        if(n%10**2 !=0):
            result+= " and "
    if (n%10**2 >=20):
        result+= a2[(n%10**2)//10]
        if(n%10!=0):
            result+=" "+a1[n%10]
    else:
        result+=a1[n%10**2]
    return result

while True:
    try:
        n = int(raw_input())
        eng = ''
        if n/(10**6)!=0:
            eng += covert(n/(10**6))+' million '
            n = n%(10**6)
        if n/(10**3) !=0:
            eng += covert(n/(10**3))+ ' thousand '
            n = n%(10**3)
        eng = eng + covert(n)
        print eng
    except:
        break