# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0122.py
@time:2017/9/11  11:07
"""
#代码作业
# -*- coding: utf-8 -*-

import time
import os
import json


def calMoney(allInfo, type):
    money = 0

    if allInfo[4] <= 5:
        standard = [30, 50, 80, 60]
        timeLen = [3, 6, 2, 2]
        if allInfo[2] >= 9 and allInfo[2] < 12:
            s = 0
            money = money + (12 - allInfo[2]) * standard[s]
        elif allInfo[2] >= 12 and allInfo[2] < 18:
            s = 1
            money = money + (18 - allInfo[2]) * standard[s]
        elif allInfo[2] >= 18 and allInfo[2] < 20:
            s = 2
            money = money + (20 - allInfo[2]) * standard[s]
        elif allInfo[2] >= 20 and allInfo[2] <= 22:
            s = 3
            money = money + (22 - allInfo[2]) * standard[s]

        if allInfo[3] >= 9 and allInfo[3] < 12:
            e = 0
            money = money + (allInfo[3] - 9) * standard[e]
        elif allInfo[3] >= 12 and allInfo[3] < 18:
            e = 1
            money = money + (allInfo[3] - 12) * standard[e]
        elif allInfo[3] >= 18 and allInfo[3] < 20:
            e = 2
            money = money + (allInfo[3] - 18) * standard[e]
        elif allInfo[3] >= 20 and allInfo[3] <= 22:
            e = 3
            money = money + (allInfo[3] - 20) * standard[e]

        for i in range(s + 1, e):
            money = money + standard[i] * timeLen[i]
        # 算重部分
        if s == e:
            money = money - (allInfo[3] - allInfo[2]) * standard[s]

        if type:
            money = money * 0.5
    else:
        standard = [40, 50, 60]
        timeLen = [3, 6, 4]
        if allInfo[2] >= 9 and allInfo[2] < 12:
            s = 0
            money = money + (12 - allInfo[2]) * standard[s]
        elif allInfo[2] >= 12 and allInfo[2] < 18:
            s = 1
            money = money + (18 - allInfo[2]) * standard[s]
        elif allInfo[2] >= 18 and allInfo[2] <= 22:
            s = 2
            money = money + (22 - allInfo[2]) * standard[s]

        if allInfo[3] >= 9 and allInfo[3] < 12:
            e = 0
            money = money + (allInfo[3] - 9) * standard[e]
        elif allInfo[3] >= 12 and allInfo[3] < 18:
            e = 1
            money = money + (allInfo[3] - 12) * standard[e]
        elif allInfo[3] >= 18 and allInfo[3] <= 22:
            e = 2
            money = money + (allInfo[3] - 18) * standard[e]

        for i in range(s + 1, e):
            money = money + standard[i] * timeLen[i]
        # 算重部分
        if s == e:
            money = money - (allInfo[3] - allInfo[2]) * standard[s]
        if type:
            money = money * 0.25
    return int(money)


def addBook(allInfo):
    bookPath = 'bookInfos.json'
    if os.path.exists(bookPath):

        fileR = open(bookPath, 'r')
        allInfos = json.load(fileR)
        allInfos.append(allInfo)
        #    data={'name':allInfo[0],'date':allInfo[1],'start':allInfo[2],'end':allInfo[3]};
        #    allInfos.append(data);
        fileR.close()

        file = open(bookPath, 'w', encoding='utf-8')
        json.dump(allInfos, file, ensure_ascii=False)
        file.close()
    else:
        data = []
        data.append(allInfo)
        file = open(bookPath, 'w', encoding='utf-8')
        json.dump(data, file, ensure_ascii=False)
        file.close()

    # 计算钱
    moneyStr = str(calMoney(allInfo, False))
    fileName = allInfo[5] + '.txt'
    with open(fileName, "a") as f:
        content = allInfo[1] + " " + str(allInfo[2]) + "点至" + str(allInfo[3]) + "点 由" + allInfo[
            0] + "预定的，正常费用：" + moneyStr + "元\n"
        f.write(content)


def findBook(allInfo):
    bookPath = 'bookInfos.json'
    if os.path.exists(bookPath):
        fileR = open(bookPath, 'r')
        allInfos = json.load(fileR)
        fileR.close()

        for i in range(len(allInfos)):
            # 日期为同一天，同一场地，且起始时间和结束时间有冲突
            if allInfos[i][1] == allInfo[1] and allInfos[i][5] == allInfo[5] and (
                    allInfos[i][3] > allInfo[2] or allInfos[i][2] < allInfo[3]):
                return True
        return False
    else:
        return False


def removeBook(allInfo):
    bookPath = 'bookInfos.json'
    if os.path.exists(bookPath):
        fileR = open(bookPath, 'r')
        allInfos = json.load(fileR)
        fileR.close()

        if allInfo in allInfos:
            allInfos.remove(allInfo)
            file = open(bookPath, 'w', encoding='utf-8')
            json.dump(allInfos, file, ensure_ascii=False)
            file.close()

            # 计算违约金
            moneyStr = str(calMoney(allInfo, True))
            fileName = allInfo[5] + ('.txt')

            with open(fileName, "r") as f:
                lines = f.readlines()
                content = allInfo[1] + " " + str(allInfo[2]) + "点至" + str(allInfo[3]) + "点 由" + allInfo[
                    0] + "预定的，正常费用：" + str(calMoney(allInfo, False)) + "元\n"

                if content in lines:
                    lines.remove(content)

                content = allInfo[1] + " " + str(allInfo[2]) + "点至" + str(allInfo[3]) + "点 由" + allInfo[
                    0] + "取消的，违约费用：" + moneyStr + "元\n"
                lines.append(content)
                f.close()
            with open(fileName, 'w') as f:
                f.writelines(lines)
                f.close()
            return True
        else:
            return False


def printAllInfo():
    place = ['A', 'B', 'C', 'D']
    money = 0
    for i in range(4):
        print("场地：" + place[i])
        fath = place[i] + ".txt"
        m = 0
        if os.path.exists(fath):
            f = open(fath)
            lines = f.readlines()
            f.close()
            for line in lines:
                print(line)
                mstr = line.split("：")[1]
                m = m + int(mstr[0:len(mstr) - 2])
            print("小计：" + str(m) + "元\n")
            money = money + m
        else:
            print("小计：0元\n")
        print("\n\n")
    print("------------")
    print("总计：" + str(money) + "\n")


def isLegal(bookInfo):
    info = bookInfo.split(' ')
    # 结构长度合法
    if len(info) == 4 or len(info) == 5:
        # 检验日期是否合法

        try:
            infoD = time.strptime(info[1], "%Y-%m-%d")
            infoT = info[2].split("~")
            infoS = time.strptime(infoT[0], "%H:%M")
            infoE = time.strptime(infoT[1], "%H:%M")

            # 起止时间非整点,也排除起始时间点比终止时间点大的
            if infoS.tm_min != 0 or infoE.tm_min != 0 or infoS.tm_hour < 9 or infoS.tm_hour > 22 or infoE.tm_hour < 9 or infoE.tm_hour > 22 or infoS.tm_hour >= infoE.tm_hour:
                return False
            # 不是ABCD四个场地
            place = ord(info[3]) - 64
            if place < 1 or place > 4:
                return False
            # 取消订单不是字母C
            if len(info) == 5 and info[4] != 'C':
                return False

            data = [info[0], info[1], infoS.tm_hour, infoE.tm_hour, infoD.tm_wday, info[3]]

            isFind = findBook(data)

            # 取消订单
            if len(info) == 5:
                reSucc = removeBook(data)
                return reSucc
            else:
                # 如果预定时间和日期不冲突则添加
                if not (isFind):
                    addBook(data)
                    return True
                else:
                    return False
        except:
            return False


    else:
        return False


if __name__ == "__main__":
    while True:
        bookInfo = raw_input()
        if bookInfo == "exit":
            break
        else:
            if bookInfo == " ":
                printAllInfo()
            else:
                if isLegal(bookInfo):
                    print("接受指令")
                else:
                    print("指令错误")
'''
a=[]
a.append(['fwe','fds',3,5])

a.append(['fwe','fds',3,5]);
addBook(a)


bookPath='bookInfos.json';
fileR=open(bookPath,'r')
#file=open(bookPath,'w',encoding='utf-8')

allInfos=json.load(fileR);
allInfos.append(['fwe','fds',3,5]);
addBook(allInfos)
'''