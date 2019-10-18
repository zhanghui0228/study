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
    %m     用数字表示的月份
    %d      用数字表示月份中的一天
    %Y      四位的年份
    %y      两位的年份
    %H      24小时制的小时数
    %I      12小时制的小时数
    %p      am或pm
    %M      分钟数
    %S      秒数
'''
'''
from datetime import datetime, date, time, timedelta


#自定义日期和时间
d = datetime(2019, 10, 14, 17, 40)
print(d)
d2 = date(2020, 1, 13)
print(d2)
t = time(18, 0)
print(t)
print("-----------------------------------")
#日期、时间与字符串之间的相互转换
#字符串转换datetime对象
ds = '2019-10-17 11:38:30'
ds_t = datetime.strptime(ds, '%Y-%m-%d %H:%M:%S')
print(ds_t)
print(ds_t.date())

#datetime转换字符串
n = datetime.now()
n_str = n.strftime('%Y-%m-%d %H:%M:%S')
n_year = n.strftime('%Y')       #只获取当前年份
print(n_year)
print(n_str)

#datetime之间的加减操作

#时间的加法
now = datetime.today()
print(now)
next_time = now + timedelta(days=2, hours=12)
print(next_time)

#时间的减法
date1 = datetime(2019, 10, 18)
date2 = datetime(2019, 11, 18)
result = date2 - date1
print(result)
'''

#编程练习一
'''
任务
    1、date_time变量接收自定义日期时间为2019-10-10 8:10
    2、使用time模块的sleep函数停顿2秒
    3、使用date_变量接收自定义日期2019-11-11
    4、使用time_变量接收自定义时间11:11
'''
import datetime, time
# 自定义日期时间为2019-10-10 8:10
date1 = '2019-10-10 8:10:0'
# 打印自定义的日期时间对象
d = datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
print(d)
# 使用time模块的sleep函数停顿2秒
time.sleep(2)
# 自定义日期2019-11-11
date2 = '2019-11-11'
# 打印自定义的日期对象
d2 = datetime.datetime.strptime(date2, '%Y-%m-%d')
print(d2)
# 自定义时间11:11
ti = '23:33:00'
# 打印自定义的时间对象
t = datetime.datetime.strptime(ti, '%H:%M:%S')
print(t)

#编程练习二
'''
任务
    1、定义一个str_字符串为2019-09-10 8:10:56
    2、将str_转换为日期函数2019-09-10 8:10:56，使用str_date变量接收
    3、定义now_变量接收当前的日期时间
    4、将当前日期时间格式化为——四位的年份/月/日 时:分:秒，使用date_str接收
'''
from datetime import datetime
# 定义一个str_字符串为2019-09-10 8:10:56
str_ = '2019-09-10 8:10:56'
# 将str_转换为日期函数2019-09-10 8:10:56
str_date = datetime.strptime(str_, '%Y-%m-%d %H:%M:%S')
# 定义now_变量接收当前的日期时间
now_ = datetime.now()
# 将当前日期时间格式化为——四位的年份/月/日 时:分:秒
date_str = now_.strftime('%Y/%m/%d %H:%M:%S')
print(str_date)
print(date_str)

#编程练习三
'''
任务
    1、定义now_变量接收当前日期时间
    2、使用now_before接收距当前日期时间3天36小时12分钟之前的日期时间
    3、使用now_after接收计算10天之后的日期时间
'''
from datetime import datetime, timedelta
# 定义now_变量接收当前日期时间
now_= datetime.now()
# 计算距当前日期时间3天36小时12分钟之前的日期时间
now_before= now_ - timedelta(days=3, hours=36, minutes=12)
# 计算10天之后的日期时间
now_after= now_ + timedelta(days=10)
print(now_before)
print(now_after)



###################################
#python安装第三方模块
'''
    查看第三方模块的网站：
        www.pypi.org
    安装方法：
        方法一：
            pip install module_name     #直接安装
        方法二：
            python setup.py install     #源码安装       解压后的
            pip install modele_tar      #直接指定下载的压缩模块包进行安装
    卸载方法：
        pip uninstall module_name
'''