# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_098.py
@time:2017/9/1  19:14
"""
# 二维数组操作

def init(row, line):
    #生成数组
    if  0<= row <=9 and 0<= line <= 9:
        arr = [[i for i in range(line)] for j in range(row)]
        print 0
        return arr
    else:
        print -1

def exchange(arr, source, dest):
    #数组行列值进行交换
    if 0 <= source[0] < len(arr) and 0 <= source[1] < len(arr[0])\
            and 0 <= dest[0] < len(arr) and 0 <= dest[1] < len(arr[0]):
        arr[dest[0]][dest[1]], arr[source[0]][source[1]] =\
            arr[source[0]][source[1]], arr[dest[0]][dest[1]]
        return 0
    else:
        return -1

def insert_line(arr, ins_line):
    #数组插入行操作
    if 0 <= ins_line < len(arr):
        arr.insert(ins_line, [0 for i in range(len(arr[0]))])
        # for i in a:
        #     print i
        return 0
    else:
        return -1

def insert_column(arr, ins_col):
    if 0<=ins_col<len(arr[0]):
        for i in range(len(arr)):
            arr[i].insert(ins_col,0)
        # for i in a:
        #     print i
        return 0
    else:
        return -1

def search(arr,search_grid,row, line):
    if 0<= search_grid[0] < row and 0<= search_grid[1] < line:
        return 0
    else:
        return -1

while True:
    try:
        #读取输入的两个数
        row, line = [int(x) for x in raw_input().split()]
        #生成数组
        arr = init(row, line)
        # 读取要交换的行列值
        source = [int(x) for x in raw_input().split()]
        # dest = [int(x) for x in raw_input().split()]
        # print source
        # print dest
        # 对交换结果进行输出
        print exchange(arr, source[0:2], source[2:])
        #输入要插入的行的数值
        ins_line = int(raw_input())
        print insert_line(arr, ins_line)

        ins_col = int(raw_input())
        print insert_column(arr, ins_col)
        # print arr
        search_grid = [int(x) for x in raw_input().split()]
        # print search_grid
        print search(arr, search_grid, row, line)
    except:
        break