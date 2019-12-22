#迭代器
'''
    迭代（iterator）    意味着重复多次，就像循环那样（list,tuple）
    迭代器：    实现了方法__iter__的对象是可迭代的，而实现了方法__next__的对象是迭代器
    调用方法__next__时（或next()），迭代器返回其下一个值
    如果迭代器没有可供返回的值，触发StopIteration异常

    从迭代器创建序列：
        通过对可迭代对象调用内置函数iter，可获得一个迭代器
'''

#生成一个计算数的平方的迭代器

class PwdNumber(object):
    '''
    iterator
    生成数的平方
    '''

    value = 0

    def __next__(self):
        '''每执行一次value值就 + 1'''
        self.value += 1
        if self.value > 5:
            raise StopIteration
        print('{0}的平方是{1}'.format(self.value,self.value * self.value))
        return self.value * self.value

    def __iter__(self):
        '''可迭代'''
        return self

if __name__ == '__main__':
    pow = PwdNumber()
    # pow.__next__()
    # pow.__next__()
    # pow.__next__()
    #循环迭代器
    for i in pow:
        pow
    print('#' * 30)

#生成器    generator
'''
    生成器是一种使用普通函数语法定义的迭代器
    包含yield语句的函数都被称为生成器
    不使用return返回一个值，而是可以生成多个值，每次一个
    每次使用yield生成一个值后，函数都将冻结，即在此停止执行
    被重新唤醒后，函数将从停止地方开始继续执行
'''

#示例
list_gen = (x * x for x in [1, 2, 3, 4, 5])

def Num():
    yield 1
    yield 2
    yield 3

def Num_pow(num):
    if isinstance(num, int):
        return (x * x for x in range(1, num + 1))

def Num_pow2(num):
    if isinstance(num, int):
        for y in range(1, num + 1):
            yield y * y     #生成器

if __name__ == '__main__':
    num = Num()
    print(next(num))
    for i in num:
        print(i)
    print('*' * 30)
    num2 = Num_pow2(5)
    print(num2.__next__())
    for x in num2:
       print(x)