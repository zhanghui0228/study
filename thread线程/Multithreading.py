#多线程

#实现我的余额
import threading
import time

balance = 0

def change_it(n):
    '''改变余额的方法'''
    global balance
    balance = balance + n
    time.sleep(2)
    balance = balance - n
    #time.sleep(1)
    print('--N---{0}; ---balance--{1}'.format(n, balance))


class ChangeBlanceThread(threading.Thread):
    '''改变余额线程'''

    def __init__(self, num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num = num

    def run(self):
        for i in range(100):
            change_it(self.num)


if __name__ == '__main__':
    t1 = ChangeBlanceThread(6, name='first thread')
    t2 = ChangeBlanceThread(10, name='two thread')
    #启动第一个线程
    t1.start()
    t2.start()
    t1.join()
    t2.join()