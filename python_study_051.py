# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_051.py
@time: 2017/8/1 9:21
"""

def printf(temp):
    for i in temp:
        print ('(%d,%d)' % (i[0],i[1]))

def maze(xy,array,row,col):
    if xy[0] == row-1 and xy[1] == col-1:
        printf(temp)

    # 判断左方向
    if xy[1]-1 >= 0:
        if array[xy[0]][xy[1]-1] != 1 and array[xy[0]][xy[1]-1] != 'X':
            array[xy[0]][xy[1]-1] = 'X'
            temp.append([xy[0],xy[1]-1])
            maze([xy[0],xy[1]-1],array,row,col)

    # 判断右方向
    if xy[1] + 1 < col:
        if array[xy[0]][xy[1] + 1] != 1 and array[xy[0]][xy[1] + 1] != 'X':
            array[xy[0]][xy[1] + 1] = 'X'
            temp.append([xy[0], xy[1] + 1])
            maze([xy[0], xy[1] + 1], array, row, col)

    # 判断上方向
    if xy[0] - 1 >= 0:
        if array[xy[0] - 1][xy[1]] != 1 and array[xy[0] - 1][xy[1]] != 'X':
            array[xy[0] - 1][xy[1]] = 'X'
            temp.append([xy[0] - 1, xy[1]])
            maze([xy[0] - 1, xy[1]], array, row, col)
    # 判断下方向
    if xy[0] + 1 < row:
        if array[xy[0] + 1][xy[1]] != 1 and array[xy[0] + 1][xy[1]] != 'X':
            array[xy[0] + 1][xy[1]] = 'X'
            temp.append([xy[0] + 1, xy[1]])
            maze([xy[0] + 1, xy[1]], array, row, col)
    if  len(temp) != 0 :
        temp.pop()
    return

while True:
    try:
        # 读取第一行的输入
        rowCol = raw_input().split()
        # 定义路径矩阵的行和列
        row = int(rowCol[0])
        col = int(rowCol[1])
        array = []
        global temp
        temp = [[0,0]]

        for i in range(row):
            temp1 = map(int, raw_input().split())
            array.append(temp1)
        array[0][0] = 'X'
        maze([0,0], array, row, col)
    except:
        break