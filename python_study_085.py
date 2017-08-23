# encoding: utf-8
"""
@author: Xiaoping
@file: python_study_085.py
@time: 2017/8/22 23:09
"""
def  handle(pre_station, in_station, after_station):
    if not pre_station and not in_station:  # 没有待进站的，也没有待出站的车，一种情况产生了
        result.append(" ".join(after_station))
    else:
        if in_station:  # 出站作业，先检查站内是否有车
            after_station.append(in_station.pop( ))
            handle(pre_station, in_station, after_station)
            in_station.append(after_station.pop( ))
        if pre_station:  # 进站作业，先检查是否还有待进站车辆
            in_station.append(pre_station.pop(0))
            handle(pre_station, in_station, after_station)
            pre_station.insert(0, in_station.pop( ))

count = int(raw_input( ))  # 火车数量，没有用到，但是是题目输入格式要求，故保留
row_2 = raw_input( )
result = []  # 记录最终数据
pre_station = [x for x in row_2.split(" ")]  # 待进站的车辆
in_station = []  # 待出站车辆
after_station = []  # 出站后的车辆
handle(pre_station, in_station, after_station)
result.sort( )  # 要字典序输出，排个序咯
for rs in result:
    print rs
