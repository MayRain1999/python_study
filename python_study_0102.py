# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0102.py
@time:2017/9/1  22:30
"""
#密码强度等级
# def GetPwdSecurityLevel():
def score(s):
    result, length, upper, lower, digit, other = [0] * 6
    for i in s:
        if i.isdigit():#判断数字
            digit += 1
        elif i.isupper():#大写字母
            upper += 1
        elif i.islower():#小写字母
            lower += 1
        else:                #其他
            other += 1
        length += 1

    if length <= 4: #长度
        result += 5
    elif length <= 7:
        result += 10
    else:
        result += 25
    #   对数字 大小写字母进行判断计分
    if (upper == 0 and lower != 0) or (lower == 0 and upper != 0):
        result += 10
    elif (upper != 0 and lower != 0):
        result += 20

    if digit == 1:
        result += 10
    elif digit >= 2:
        result += 20

    if other == 1:
        result += 10
    elif other > 1:
        result += 25

    if (upper != 0 and lower == 0 and digit != 0 and other == 0):
        result += 2
    elif (lower != 0 and upper == 0 and digit != 0 and other == 0):
        result += 2
    elif (lower != 0 and upper == 0 and digit != 0 and other != 0):
        result += 3
    elif (upper != 0 and lower == 0 and digit != 0 and other != 0):
        result += 3
    elif (upper != 0 and lower != 0 and digit != 0 and other != 0):
        result += 5
    #对安全进行评价
    if result >= 90:
        return 'VERY_SECURE'
    elif result >= 80:
        return 'SECURE'
    elif result >= 70:
        return 'VERY_STRONG'
    elif result >= 60:
        return 'STRONG'
    elif result >= 50:
        return 'AVERAGE'
    elif result >= 25:
        return 'WEAK'
    else:
        return 'VERY_WEAK'
while True:
    try:
        print score(raw_input())
    except:
        break
