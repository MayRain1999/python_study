# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_072.py
@time:2017/8/19  12:41
"""

command = {  # "reset":"reset what",
    "reset board": "board fault",
    "board add": "where to add",
    "board delet": "no board at all",
    "reboot backplane": "impossible",
    "backplane abort": "install first",
    "he he": "unkown command"
}

unknown = "unkown  command"

def recover(s):
    s = s.split()
    if len(s) == 1:
        reset = "reset"
        for i in range(len(s[0])):
            if s[0][i] != reset[i]:
                print unknown
                return
        print "reset what"
    elif len(s) == 2:
        for com in command.keys():
            flag = 0
            com_split = com.split()
            for i in range(len(s[0])):
                if s[0][i] != com_split[0][i]:
                    flag = 1
                    break
            if flag == 0:
                for i in range(len(s[1])):
                    if s[1][i] != com_split[1][i]:
                        flag = 1
                        break
            if flag == 0:  # two command are correct
                print command[com]
                return
        print unknown

    else:
        print unknown

while True:
    try:
        x = raw_input()
        recover(x)
    except:
        break