#python中常用的高阶函数
'''
    lambda函数
    filter函数       过滤器
    map函数           遍历器
    reduce函数
'''

'''
    lambda函数
        lambda是一种表达式，创建内嵌的简单匿名函数，不是代码块
    
    filter函数使用：
        返回一个filter对象，其中包含对其执行函数时结果为真的所以元素，相当于一个过滤器
        方法签名：filter(func, seq)
'''
#filter使用方法

"""
def use_filter(list):
    '''
    获取指定的列表/元组中的奇数
    :param list:    list/tuple 要过滤的数据
    :return:    过滤好的奇数列表
    '''
    result = filter(lambda n: n % 2 != 0, list)
    return result

if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    rese = use_filter(l)
    print(list(rese))

stus = [
    {"name": "xm", "age": 18},
    {"name": "xw", "age": 20},
    {"name": "xl", "age": 16}
]
stus.sort(key=lambda x: x["age"])
print(stus[1]["name"])
print(stus[0])

#编程练习

任务

1、定义use_filter函数

2、函数体内：实现过滤偶数值的功能


def use_filter(data):
    # 使用result接收filter过滤偶数值的功能
    result = filter(lambda n: n %2 == 0, data)
    return result
if __name__ == '__main__':
    # 使用data接收0-50的数值
    data = list(range(51))
    # 调用use_filter函数传入data,使用result变量接收
    result = use_filter(data)
    print(list(result))
"""

'''
    map函数：
        创建一个列表，其中包含对指定序列包含的项执行指定函数返回的值
        
        map(function, sequence, ...)        #sequence  序列，可以是一个元组，也可以是一个列表
        map(函数， list/tuple)    返回的值为每个list/tuple执行函数后的值
        
'''

#需求：返回一个列表中每个数值的立方根

def pow_number(l):
    '''
    返回一个列表或者元组中每个数值的立方根
    :param l: list/tuple int类型
    :return: 每个数值的立方根
    '''
    number_list = []
    for x in l:
        number_list.append(x * x * x)
    return number_list

def f(n):
    '''
    求数的立方根
    :param n: list/tuple int类型
    :return: 数的立方根
    '''
    return n * n * n


def map_number(l):
    '''
    使用map计算给定的list/tuple中每个数的立方根
    :param l: list/tuple    int类型
    :return:    每个数值的立方根
    '''
    return map(f, l)

def lambda_number(l):
    '''
    使用map计算lambda表达式中每个数的立方根
    :param l:   lambda int类型
    :return:  lambda中每个数值的立方根
    '''
    result = map(lambda n: n * n * n, l)
    return result

if __name__ == '__main__':
    number_list = [1, 3, 4, 5, 6, 7]
    result = pow_number(number_list)
    map_result = map_number(number_list)
    print(result)
    print(list(map_result))
    lambda_result = lambda_number(number_list)
    print(list(lambda_result))

#编程练习
'''
任务

1、函数体内：实现各个元素的5次方功能

2、调用use_map函数传入data，使用result接收
'''
def use_map(data):
    # 使用result接收map实现各个元素的5次方功能
    result = map(lambda n: n * n * n * n * n, data)
    return result

if __name__ == '__main__':
    data = (2,4,6,8,10,12)
    # 调用use_map函数传入data，使用result接收
    result = use_map(data)
    print(tuple(result))

'''
    reduce函数：
        使用指定的函数将序列的前两个元合二为一，再将结果与第三个元素合二为一，依次类推，直到处理完整个序列并得到一个结果
    
    reduce(func, seq[, initial])
    等价于 func(func(func(seq[0], seq[1]),seq[2]), ...)
'''
#需求：计算给定列表中的数值的和
def get_number(list):
    '''
    计算给定列表中的所有数值的和
    :param list:
    :return:
    '''
    result = 0
    for i in list:
        result += i
    return result

def use_py_sum(list):
    '''使用python内置的函数进行求和'''
    return sum(list)

if __name__ == '__main__':
    list_num = [1, 2, 3, 4, 5, 6, 7, 8]
    result = get_number(list_num)
    print(result)
    result_py = use_py_sum(list_num)
    print(result_py)