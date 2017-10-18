# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0128.py
@time:2017/10/18 10:29
"""
#最大子序列的和

def  MaxSequenceSum(arr):
    maxSum =0
    arrLen = len(arr)
    for i in range(0, arrLen):
        for j in range(i, arrLen):
            thisSum  = 0
            for k in range(i, j+1):
                thisSum += arr[k]
            if thisSum>maxSum:
                maxSum  = thisSum
    return maxSum
    #时间复杂度为N^3

def  MaxSequenceSum2(arr):
    maxSum =0
    arrLen = len(arr)
    for i in range(0, arrLen):
        thisSum = 0
        for j in range(i, arrLen):
            thisSum += arr[j]
            if thisSum>maxSum:
                maxSum  = thisSum
    return maxSum
 # 时间复杂度 N^2  相对第一个 减少了一个for循环

def  MaxSequenceSum3(arr):
    pass
# 采用分治法实现 总共分三种情况
#第一种 最大子序列和在左边
#第二种 最大子序列和在右边
#第三种 最大子序列 左边 右边的相加

def  MaxSequenceSum4(arr):
    maxSum =0
    thisSum = 0
    arrLen = len(arr)
    for i in range(0, arrLen):
        thisSum += arr[i]
        if thisSum>maxSum:
            maxSum  = thisSum
        elif thisSum<0:
            thisSum  = 0
    return maxSum
# 时间复杂度是N

if __name__ == '__main__':
    while True:
        try:
            arr = map(int, raw_input().split())
           # 4 -3 5 -2 -1 2 6 -2
            print arr
            print MaxSequenceSum(arr)
            print MaxSequenceSum2(arr)
            print MaxSequenceSum3(arr)
            print MaxSequenceSum4(arr)
        except:
            break