rom datetime import datetime
import time

global stamps
global now
stamps = time.time()
now = datetime.now()


#简单的获取日期、时间和时间jie
#日期
def date():
    #获取年份
    year = now.year
    #获取月份
    month = now.month
    #获取日期
    day = now.day
    #返回获取值
    return year,month,day


#时间
def time():
    #获取小时
    hour = now.hour
    #获取分钟
    minute = now.minute
    #返回获取值
    return hour,minute

#时间戳
def stamp():
    #运算64位时间戳
    stamp64 = round(stamps * 100000000000000000000000000000000000000000000000000000)
    #运算32位时间戳
    stamp32 = round(stamps * 1000000000000000000000)
    #运算16位时间戳
    stamp16 = round(stamps * 1000000)
    #返回时间戳
    return stamp16,stamp32,stamp64