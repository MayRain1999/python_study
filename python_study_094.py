# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_094.py
@time: 2017/8/31 20:22
"""
# 第一行输入一个数n，接下来n行，每行一个字符串，表示每个超链接的名称。
# 名称只由小写字母构成，长度不超过20，且所有名称互不相同。（1≤n≤100）
# 接下来输入一个数m，表示用户点击了m个超链接，最后m行表示用户点击过的超链接名称
# ，这m个链接中可能有重复。（1≤m≤100）
# 超链接
while True:
    try:
        n = int(raw_input())
        arrN = []
        arrM = []
        result = []
        for i in range(n):
            arrN.append(raw_input())
        m = int(raw_input())
        for i in range(m):
            arrM.append(raw_input())
        for i in arrN:
            if i not in arrM:
                result.append(i)
                # 对数组中的元素进行判断
        if len(result)>0:
            result.sort()
            # 进行字典排序
            for i in result:
                print i
            # 输出结果
        else:
            break
    except:
        break