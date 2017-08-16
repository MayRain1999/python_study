# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_033.py
@time: 2017/7/10 22:07
"""
s=raw_input()
l =[]
t = list(s)
for i in t:
     if i=='Z':
           l.append('a')
     elif 'A'<=i<='Y':
          b = chr(ord(i.lower()) + 1)
          l.append(b)
     elif i==1:
          l.append(1)
     elif 'a'<=i<='c':
          l.append(2)
     elif 'd'<=i<='f':
          l.append(3)
     elif 'g'<=i<='i':
          l.append(4)
     elif 'j'<=i<='l':
          l.append(5)
     elif 'm'<=i<='o':
          l.append(6)
     elif 'p'<=i<='s':
          l.append(7)
     elif 't'<=i<='v':
          l.append(8)
     elif 'w'<=i<='z':
          l.append(9)
     elif  i==0:
          l.append(0)
     else:
          l.append(i)
k="".join(map(str, l))
print k