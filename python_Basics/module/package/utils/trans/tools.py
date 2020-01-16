from datetime import datetime
import random


def gen_trans_id(date=None):
    '''
    根据所传入的时间得到唯一一个交易流ID
    :param date:日期
    :return:交易流水ID字符串
    '''
    #若没有传入时间，则使用系统当前的时间
    if date is None:
        date = datetime.now()
    #保证字符串唯一性
    #日期+时间+毫秒+随机数(6位数)
    #return date.strftime('%y%m%d%H%M%S%f') + str(random.randint(100000, 999999))
    return '{0}{1}'.format(date.strftime('%y%m%d%H%M%S%f'), random.randint(100000, 999999))