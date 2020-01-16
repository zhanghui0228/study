#进程之间的通信
'''
    通过Queue、Pipes等实现进程之间的通信

'''
import os
import random
import time
from multiprocessing import Process, Queue, current_process


class WriteProcess(Process):
    tag = '写进程'

    def __init__(self, q, *args, **kwargs):
        self.q = q
        super().__init__(*args, **kwargs)

    def run(self):
        ''' 实现业务逻辑 '''
        ls = [
            'first',
            'two',
            'three'
        ]
        print('Write process pid is {pid}'.format(pid=os.getpid()))
        for lien in ls:
            print('write info is {0} -- {1}'.format(lien, current_process()))       #current_process() 打印进程的名称, 面向过程形式调用
            self.q.put(lien)
            time.sleep(random.randint(2, 7))


class ReadProcess(Process):
    tag = '读进程'

    def __init__(self, q, *args, **kwargs):
        self.q = q
        super().__init__(*args, **kwargs)

    def run(self):
        print('Read process pid is {pid}'.format(pid=os.getpid()))
        while True:
            context = self.q.get()
            print('read context is {0} -- {1}'.format(context, self.name))      #self.name  面向对象形式调用


def main():
    #通过Queue共享数据
    q = Queue()
    #将写和读的进程进行实例化
    p_write = WriteProcess(q)
    p_read = ReadProcess(q)

    p_write.start()
    p_read.start()
    p_write.join()
    # p_read.join()

    #因为读的进程是死循环，无法等待其结束，所有读不到内容后（写进程执行完毕）强制结束进程
    p_read.terminate()

if __name__ == '__main__':
    main()