#datetime模块
'''
    timedelta       对日期/时间进行加减操作时使用
    datetime.datetime.now.date            date类表示一个日期
    datetime.strftime       将datetime对象格式化成字符串
    datetime.strptime       将字符串按照一定的格式转换成datetime对象
    datetime.datetime.now.time            表示一个时间的类
    datetime.now        系统当前的时间
    datetime.datetime.now.day             datetime对象的属性，类似的还有minute,hour等
    days            timedelta的属性，类似的还有minutes,hours等
'''

import datetime
'''
    也可以使用from datetime import datetime
    其书写方法为：datetime.now()       #省略一个datetime

now = datetime.datetime.now()
print("now: {now}".format(now=now))      #当前时间
print("now: {now}".format(now=datetime.datetime.today()))      #当前时间
print("now_day: {now_day}".format(now_day=now.date()))            #当前日期
print("now_time: {now_time}".format(now_time=now.time()))           #当前时间
print("year: {year}".format(year=now.year))         #当前年份
print("month: {month}".format(month=now.month))     #当前月份
print("day: {day}".format(day=now.day))             #当前日期
print("hour: {hour}".format(hour=now.hour))         #当前小时
print("minute: {minute}".format(minute=now.minute))     #当前分钟
print("second: {second}".format(second=now.second))     #当前秒

import time
time.sleep(2)   #等待2秒
print(time.time())      #获取毫秒数
'''
#编程练习
'''
任务
    1、使用两种方法获得当前日期时间，并输出到控制台
    2、在控制台上分别对日期和时间进行输出
    3、使用-拼接年月日得到当前日期

from datetime import datetime
# 得到当前日期时间（两种方法）
print(datetime.now())
print(datetime.today())
# 得到当前日期
print(datetime.now().date())
# 得到当前时间
print(datetime.now().time())
# 得到当前年份用year_变量接收
print("year: {year}".format(year=datetime.now().year))
# 得到当前月份用month_变量接收
print("month: {month}".format(month=datetime.now().month))
# 得到当前天用day_变量接收
print("day: {day}".format(day=datetime.now().day))
# 使用-拼接年月日得到当前日期
print("{year}-{month}-{day}".format(year=datetime.now().year,month=datetime.now().month,day=datetime.now().day))
'''

#datetime模块的时间转换
'''
    dadetime模块转换参数列表：
    %A      星期的名称
    %B      月份名
    %:m     用数字表示的月份
    %d      用数字表示月份中的一天
    %Y      四位的年份
    %y      两位的月份
    %H      24小时制的小时数
    %I      12小时制的小时数
    %p      am或pm
    %M      分钟数
    %S      秒数
'''
from datetime import datetime, date, time
#自定义日期和时间
d = datetime(2019, 10, 14, 17, 40)
print(d)
d2 = date(2020, 1, 13)
print(d2)
t = time(18, 0)
print(t)
print("-----------------------------------")
#日期、时间与字符串之间的相互转换
