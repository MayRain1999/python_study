# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_095.py
@time:2017/9/1  15:26
"""
# 写一个函数，求斐波那契数列的第N项
# 改进的算法：从下往上计算。首先根据f(0)和f(1)算出f(2)
# 再根据f(1)和f(2)算出f(3)。。。。。依此类推就可以算出第n项了。
# 很容易理解，这种思路的时间复杂度是o(n)。
# 实现代码如下：
def long_Fibonacci (n ):
    result = [0,1]
    if n<2:
        return result[n]
    fibNminusOne = 1
    fibNminusTwo = 0
    # 循环进行求解
    for i in range(2, n+1):
        fibN = fibNminusOne+fibNminusTwo
        fibNminusTwo = fibNminusOne
        fibNminusOne = fibN
    return fibN
    #返回这个数字 进行循环

while True:
    try:
        n = input()
        # 输入要求的是第几项
        print long_Fibonacci(n)
    except:
        break
