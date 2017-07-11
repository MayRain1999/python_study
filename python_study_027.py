n = raw_input()
print n[::-1]
# 反转字符输出

n = raw_input()
m = n.split(" ")
m.reverse()
print  " ".join(m)
# 反转句子输出

import sys
m = sys.stdin.readline()
n = m.strip( ).split()
# Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）
# 加入空格再倒序输出
print ' '.join(n[::-1])