# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_042.py
@time: 2017/7/18 18:25
"""
import  sys
while True:
    try:
        line = sys.stdin.readline().strip('\n')
        # 读取多行输入
        if line =='' :
            break
        l = len(line)
        maxstr = 1
        # 判断ABA型
        for i in range(1, l):
            count = 1
            k = 1
            while (i-k)>=0 and (i+k)<l and line[i-k]==line[i+k]:
                count+=2
                k+=1
                maxstr = max(count, maxstr)
        # 判断ABBA型
        for i in range(l):
            count=0
            k =1
            while (i-k+1)>=0 and (i+k)<l and line[i-k+1]==line[i+k]:
                count+=2
                k +=1
            maxstr = max(count, maxstr)
        print maxstr
    except:
        break
