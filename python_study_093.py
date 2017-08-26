# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_093.py
@time: 2017/8/26 16:17
"""
# 滴滴面试题 最大连续子串和
def max_array(numarr):
    max_end = max_start = numarr[0]
    for i in numarr[1:]:
        max_end = max(i, max_end + i)
        max_start = max(max_start, max_end)
    return max_start
while True:
    try:
        numarr = map(int, raw_input().split())
        print max_array(numarr)
    except:
        break

# target = [-1, -1, 3, -4, 5, -6, 6, -7, -8]
# targetIndex = [];
# for i in range(len(target)):
#     if target[i] < 0:
#         targetIndex.append(i)
# arr = []
# arrSum = []
# for i in range(len(targetIndex)):
#     for j in range(i, len(targetIndex)):
#         flag = 0
#         arr.append(target[targetIndex[i] + 1:targetIndex[j]]);
#         arrSum.append(sum(target[targetIndex[i] + 1:targetIndex[j]]));
# max(arrSum)