<<<<<<< HEAD
# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_039.py
@time: 2017/7/16 1:39
"""
# 密码加密和解密
while True:
    try:
        s1 = raw_input()
        s2 = raw_input()
        add_password = ''
        for i in s1:
            if  i.isdigit():
                n = int(i)
                if n!=9:
                    add_password +=str(n+1)
                else:
                    add_password +='0'
            else:
                if i.islower():
                    if  i !='z':
                        add_password+=chr(ord(i) - 31)
                    else:
                        add_password += 'A'
                else:
                    if i !='Z':
                        add_password += chr(ord(i) + 33)
                    else:
                        add_password += 'a'

        decode_passord =''

        for i in s2:
            if i.isdigit():
                n = int(i)
                if n!=0:
                    decode_passord +=str(n-1)
                else:
                    decode_passord +=str('9')
            else:
                if i.islower():
                    if i != 'a':
                        decode_passord += chr(ord(i)-33)
                    else:
                        decode_passord += 'Z'
                else:
                    if i !='A':
                        decode_passord +=chr(ord(i)+31)
                    else:
                        decode_passord +='z'
        print add_password
        print decode_passord
    except:
        break
=======
# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_039.py
@time:2017/7/3121:49
"""
def covert(n):
    a1 = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve'
    ,'thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    a2 = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    result = ""
    if (n//10**2 !=0):
        result+= a1[n//10**2]+ " hundred"
        if(n%10**2 !=0):
            result+= " and "
    if (n%10**2 >=20):
        result+= a2[(n%10**2)//10]
        if(n%10!=0):
            result+=" "+a1[n%10]
    else:
        result+=a1[n%10**2]
    return result

while True:
    try:
        n = int(raw_input())
        eng = ''
        if n/(10**6)!=0:
            eng += covert(n/(10**6))+' million '
            n = n%(10**6)
        if n/(10**3) !=0:
            eng += covert(n/(10**3))+ ' thousand '
            n = n%(10**3)
        eng = eng + covert(n)
        print eng
    except:
        break
>>>>>>> origin/master
