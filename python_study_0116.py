# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0116.py
@time:2017/9/10  10:41
"""
# -*- coding:utf-8 -*-
"""
@author:Xiaoping
@file:python_study_0115.py
@time:2017/9/7  15:36
"""
#thought works 编程任务代码
from datetime import datetime,date

while True:
    try:
        book_arr = raw_input().split()
#场地的预订和收入
        book_A = []
        book_B = []
        book_C = []
        book_D = []
        book_cost = 0

        if len(book_arr) == 4:
            user_id = book_arr[0]
            book_day1 = book_arr[1]
            book_time = book_arr[2]
            book_area = book_arr[3]
            #判断预订的时间是周一到周五还是周末
            #把字符串转换成时间格式
            book_day = datetime.strptime(book_day1, "%Y-%m-%d").strftime("%w")
            print int(book_day)
            #星期一到星期天 [0-6]
            if int(book_day) <= 5:
                book_start, book_end = book_time.split('~')
                book_start_time = book_start.split(':')
                book_end_time = book_end.split(':')
                start_time  = int(book_start_time[0])
                end_time  =int( book_end_time[0])
                #不是整点 输出错误提示
                if int(book_end_time[1]) !=0 or  int(book_start_time[1]) !=0:
                    print "Error: the booking is invalid!"
                elif  10<=end_time<=22 and  9<=start_time<=21:
                    #对输入的时间段进行判断
                    if  end_time<=start_time:
                        print "Error: the booking is invalid!"
                    #如果符合输入，开始分时间段进行计算
                    else:
                        #12点之前
                        if  end_time<=12:
                             book_cost = (end_time-start_time)*30
                        #18点之前
                        elif 12<=end_time<=18:
                            #开始时间在12点之前
                            if start_time<12:
                                book_cost = (12 - book_start) * 30 +(end_time- 12)*50
                            #开始时间在12点之后
                            else:
                                book_cost =(end_time - start_time) * 50
                        #20点之前
                        elif 18<end_time<=20:
                                #开始时间12点之前
                            if  start_time<12:
                                book_cost = (12 - start_time) * 30 + 300+(end_time-18)*80
                            #开始在12点-18点
                            elif  12<= start_time<18:
                                book_cost = (18-start_time)*50 + (end_time- 18) * 80
                            #开始在18点—20点
                            else:
                                book_cost = (end_time - start_time) * 80
                        #22点之前
                        else :
                             #开始在12点之前
                            if int(book_start_time[0]) < 12:
                                book_cost = (12-start_time)*30 + 300+160+(end_time-20)*60
                            #12点到18点
                            elif 12 <= int(book_start_time[0]) < 18:
                                book_cost =(18 - start_time) * 50 +160+ (end_time - 20)* 60
                            #18点到20 点
                            elif 18<= int(book_start_time[0]) <= 20:
                                book_cost = (20 - start_time) * 80 + (end_time - 20) * 60
                            #20点到22点
                            else:
                                book_cost = (end_time - 20) * 60
                    #不在规定时间内 输出错误提示
                else:
                    print "Error: the booking is invalid!"
            else:
                book_start, book_end = book_time.split('~')
                book_start_time = book_start.split(':')
                book_end_time = book_end.split(':')
                start_time  = int(book_start_time[0])
                end_time  =int( book_end_time[0])
                if int(book_end_time[1]) != 0 or int(book_start_time[1]) != 0:
                    print "Error: the booking is invalid!"
                elif 10 <= end_time <= 22 and 9 <= start_time <= 21:
                    # 对输入的时间段进行判断
                    if end_time <= start_time:
                        print "Error: the booking is invalid!"
                    # 如果符合输入，开始分时间段进行计算
                    else:
                        # 12点之前
                        if end_time <= 12:
                            book_cost = (end_time - start_time) * 40
                        # 18点之前
                        elif 12 <= end_time <= 18:
                            # 开始时间在12点之前
                            if start_time < 12:
                                book_cost = (12 - start_time) * 40 + (end_time- 12) * 50
                            # 开始时间在12点之后
                            else:
                                book_cost =(end_time - start_time) * 50
                        # 22点之前
                        else :
                            # 开始在12点之前
                            if start_time < 12:
                                book_cost = (12 - start_time) * 40 + 300 + (end_time -18) * 60
                            # 12点到18点
                            elif 12 <= start_time < 18:
                                book_cost = (18-start_time)*50+ (end_time - 18) * 60
                             # 18点到22点
                            else:
                                book_cost = (end_time - start_time) * 60
                #不在规定时间内 输出错误提示
                else:
                    print "Error: the booking is invalid!"
            print  book_cost
            #场地进行判断把预订信息添加进数组
            if book_area =="A":
                book_A.append([user_id,book_day1, book_time, book_area, book_cost])
                print "Success: the booking is accepted!"
            elif book_area =="B":
                book_B.append([user_id,book_day1, book_time, book_area, book_cost])
                print "Success: the booking is accepted!"
            elif book_area =="C":
                book_C.append([user_id,book_day1, book_time, book_area, book_cost])
                print "Success: the booking is accepted!"
            elif book_area =="D":
                book_D.append([user_id,book_day1, book_time, book_area, book_cost])
                print "Success: the booking is accepted!"
            else:
                print "Error: the booking is invalid!"

        elif len(book_arr) == 5:
            user_id = book_arr[0]
            book_day = book_arr[1]
            book_time = book_arr[2]
            book_area = book_arr[3]
            book_cancle = book_arr[4]
            if book_cancle !="C":
                print "Error: the booking is invalid!"
            else:
                if book_area == "A":
                    for i in range(len(book_A)):
                        if user_id == i[0] and  book_day == i[1] and book_time ==i[2] :
                            book_cost = book_cost *0.5
                            print book_cost
                        elif book_area == "B":
                            for i in range(len(book_B)):
                                if user_id == i[0] and book_day == i[1] and book_time == i[2]:
                                    book_cost = book_cost * 0.5
                        elif book_area == "C":
                            for i in range(len(book_C)):
                                if user_id == i[0] and book_day == i[1] and book_time == i[2]:
                                    book_cost = book_cost * 0.5
                        elif book_area == "D":
                            for i in range(len(book_D)):
                                if user_id == i[0] and book_day == i[1] and book_time == i[2]:
                                    book_cost = book_cost * 0.5
                        else:
                            print "Error: the booking is invalid!"
        # elif len(book_arr)==1:
            # for

        else:
            #如果是非法输入 则输出错误提示
            print "Error: the booking is invalid!"
    except:
        break
