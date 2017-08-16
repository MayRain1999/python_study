# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_052.py
@time: 2017/8/1 11:58
"""
# coding=utf-8
# 数独解法
import string
import copy
import time
import  sys

#从文件中读取数独问题，每题之间用";"分隔,各数字之间用空格分隔
def read_problem():
    # inputFile=sys.stdin.readline().strip('\n')
    rtnList=[]
    lProblem=[]
    while True:
        line=sys.stdin.readline().strip('\n')
        line=line.strip()
        if len(line) == 0:
            break

        if line==';':
            rtnList.append(copy.deepcopy(lProblem))
            lProblem=[]
            continue

        rowList=line.split(' ')
        numberList=[]
        for number in rowList:
            number=int(number)
            numberList.append(number)
        lProblem.append(numberList)
    return rtnList


#数独求解程序
# lProblem:数独问题，由一个二维数组表示
# logFile: 日志文件，将求解结果输出到这个文件中
def sudoku_solver(lProblem,logFile):
    lSolverStack=[lProblem]
    count=0
    # 若堆栈不为空，则循环
    while len(lSolverStack)>0:
        lCurrSolution=lSolverStack.pop()
        count=count+1
        logFile.write("%d" % count + '\n')
        for row in lCurrSolution:
            outLine=''
            for number in row:
                outLine=outLine + "%d" % number +' '
            logFile.write(outLine+'\n')
        logFile.write("---------------------------\n")
        isResult=True
        #用于存放当前最少候选数列表
        lMinAvailableNumber=range(1,10)
        #当前最少候选数所在位置
        lMinAvailableNumberX=0
        lMinAvailableNumberY=0

        for idx in range(81):
            i=idx%9
            j=idx/9
            if lCurrSolution[i][j]==0:
                isResult=False
                #计算当前位置可以放置的数字列表
                lCurrAvailableNumber=range(1,10)
                #如果同一行中存在相同元素，则排除
                for x in range(9):
                    if lCurrAvailableNumber.count(lCurrSolution[i][x])>0:
                        lCurrAvailableNumber.remove(lCurrSolution[i][x])
                #如果同一列中存在相同元素，则排除
                for y in range(9):
                    if lCurrAvailableNumber.count(lCurrSolution[y][j])>0:
                        lCurrAvailableNumber.remove(lCurrSolution[y][j])
                #如果当前位置所在的小九宫格中存在相同元素，则排除
                for x in range(i/3*3,i/3*3+3):
                    for y in range(j/3*3,j/3*3+3):
                        if lCurrAvailableNumber.count(lCurrSolution[x][y])>0:
                            lCurrAvailableNumber.remove(lCurrSolution[x][y])
                #如果当前单元格中可选数字个数最少，则保留
                if len(lCurrAvailableNumber)<len(lMinAvailableNumber):
                    lMinAvailableNumber=copy.deepcopy(lCurrAvailableNumber)
                    lMinAvailableNumberX=i
                    lMinAvailableNumberY=j

                if len(lMinAvailableNumber)==0:
                    break

        #若当前位置存在可选数字，则将当前位置的所有可选数字，依次作为临时解，并存入堆栈
        if len(lMinAvailableNumber)>0:
            for number in lMinAvailableNumber:
                lNewSolution=copy.deepcopy(lCurrSolution)
                lNewSolution[lMinAvailableNumberX][lMinAvailableNumberY]=number
                lSolverStack.append(lNewSolution)

        if isResult:
            return lCurrSolution
    return []


if __name__=='__main__':
    resultFile=open("Sudoku_output.txt",'w')
    lProblemList=read_problem()
    count=0
    print "Start solving.."
    for lProblem in lProblemList:
        count=count+1
        resultFile.write("Solving Problem:"+"%d" % count + ":" + "\n")
        logFile=open("Problem_"+"%d" % count+".log","w")
        startTime=time.time()
        lResult=sudoku_solver(lProblem,logFile)
        logFile.close()
        endTime=time.time()
        print "  Problem " + "%d" % count + ": finished! Time consuming: " + "%.4f" % (endTime-startTime) + " Seconds"
        if len(lResult)==0:
            resultFile.write("No Answer...\n")
        else:
            for row in lResult:
                outLine=''
                for number in row:
                    outLine=outLine + "%d" % number +' '
                resultFile.write(outLine+"\n")
        resultFile.write("--------------------------------\n")
    resultFile.close()
    print "Done!!"