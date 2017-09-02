# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0110.py
@time:2017/9/2  16:27
"""
#人民币转换
numberList = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
integralUnit = ['元', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿', '拾', '佰', '仟']
fractionUnit = ['角', '分']
while True:
    try:
        res = ['人民币']
        integral, fraction = raw_input().split('.')
        integral = integral[::-1]
        for i in range(len(integral))[::-1]:
            if int(integral[i]) == 0:
                res.append('零')
            else:
                res.append(numberList[int(integral[i])] + integralUnit[i])

        if fraction == "00":
            res.append('整')
        else:
            for j in range(len(fraction)):
                res.append(numberList[int(fraction[j])] + fractionUnit[j])
        res = ''.join(res)
        while ('零零' in res):
            res = res.replace('零零', '零')
        res = res.replace('壹拾', '拾')
        res = res.replace('人民币零', '人民币')
        if '零分' in res:
            res = res.replace('零分', '')
        if '零角' in res:
            res = res.replace('零角', '')
        print res
    except:
        break