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
