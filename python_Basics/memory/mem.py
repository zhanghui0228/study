#内存管理机制 ----赋值语句内存分析

'''
    使用id()方法访问内存地址

'''


def extend_list(val, l=[]):
    print('----------------')
    print(l, id(l))
    l.append(val)
    print(l, id(l))
    return l

list1 = extend_list(10)
list2 = extend_list(12, [])
list3 = extend_list('a')

print(list1)
print(list2)
print(list3)

"""
    垃圾回收机制：
        以引用计数为主，分代收集为辅
        如果一个对象的引用数为0，python虚拟机就会回收这个对象的内存
        引用计数的缺陷是循环引用的问题
"""

class Test(object):

    def __init__(self):
        print("对象生成了：{}".format(id(self)))

    def __del__(self):
        print("对象删除了：{}".format(id(self)))

def f0():
    '''自动回收内存'''
    while True:
        ''' 不断产生对象，但不使用它 '''
        c = Test()

def f1():
    '''内存一直在被引用，不会被回收'''
    l = []
    while True:
        c = Test()
        l.append(c)
        print(len(l))



if __name__ == '__main__':
    #f0()
    f1()    #电脑内存不大的，不要一直运行此函数