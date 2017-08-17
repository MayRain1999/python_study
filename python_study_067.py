# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_067.py
@time:2017/8/1710:04
"""
while True:
    try:
        stringInput = raw_input()
        number = int(raw_input())
        maxvalue = -1
        count = []

        for i in range(len(stringInput) - number + 1):
            stringTemp = stringInput[i:i+number]
            m  = stringTemp.count('G') + stringTemp.count('C')
            count.append(m)
        print stringInput[count.index(max(count)):count.index(max(count))+number]

        # for i in range(len(stringInput) - number + 1):
        #     stringTemp = stringInput[i:i+number]
        #     count  = stringInput.count('G') + stringInput.count('C')
        #     if  count == maxvalue:
        #         print stringTemp
    except:
        break

# inputStr = raw_input()
# n = input()
# temp = []
# for i in range(0, len(inputStr) - (n - 1)):
#     temp.append(inputStr[i:n + i])
# maxVal = 0
#
# for each in temp:
#     num = each.count('G') + each.count('C')
#     if float(num) / len(each) > maxVal:
#         maxVal = float(num) / len(each)
#         res = each
# print res