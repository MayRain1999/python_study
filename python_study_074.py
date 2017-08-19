# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_074.py
@time:2017/8/19  19:50
"""
arrNum = input()
inData = [1] * int(arrNum);
for i in range(int(arrNum)):
    inData[i] = int(input())

oneNum = 0;
twoNum = 0;
threeNum = 0;
for i in range(len(inData)):
    if inData[i] == 1:
        oneNum = oneNum + 1;
    elif inData[i] == 2:
        twoNum = twoNum + 1;
    else:
        threeNum = threeNum + 1;

one = inData[0:oneNum];
two = inData[oneNum:oneNum + twoNum];
three = inData[oneNum + twoNum::];

num = 0;
for i in range(len(one)):
    if one[i] != 1:
        for j in range(len(two)):
            if two[j] == 1:
                tem = two[j];
                two[j] = one[i];
                one[i] = tem;
                num = num + 1;
                break;
            elif j == len(two) - 1:
                for z in range(len(three)):
                    if three[z] == 1:
                        tem = three[z];
                        three[z] = one[i];
                        one[i] = tem;
                        num = num + 1;
                        break;

for i in range(len(two)):
    if two[i] != 2:
        num = num + 1;

print(num);
