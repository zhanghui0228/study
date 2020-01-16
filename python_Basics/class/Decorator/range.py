#range函数

#使用迭代器模拟range函数

class IterRange(object):
    '''使用迭代器模拟range函数'''

    def __init__(self, start, end, interval=1):
        """
        初始化传入的参数
        :param start:  开始数字 type: int
        :param end:     结束数字  type: int
        """
        self.start = start - 1
        self.end = end
        self.interval = interval

    def __next__(self):
        '''每执行一次start + 1'''
        self.start += self.interval
        if self.start >= self.end:
            raise StopIteration
        return self.start

    def __iter__(self):
        '''设置为其可迭代'''
        return self


#使用生成器模拟range函数

class GenRange(object):
    '''使用生成器模拟range函数'''

    def __init__(self, start, end, interval=1):
        self.start = start
        self.end = end
        self.interval = interval

    def get_num(self):
        '''使用rield获取数字'''
        while True:
            if self.start == self.end:
                break
            self.start += self.interval
            yield self.start - 1


if __name__ == '__main__':
    iterrange = IterRange(1, 6)
    result = list(iterrange)
    print(result)
    print('*' * 30)
    genrange = GenRange(1, 6)
    resu = genrange.get_num()
    li = list(resu)
    print(li)