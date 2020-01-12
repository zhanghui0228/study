#多线程中的锁
'''
    Lock()
        threading.lock.acquire()  #获取锁
        threading.lock.release()  #释放锁
    Rlock()
    Condition() 高级锁
'''

#使用多线程中的锁进行优化
#实现我的余额
import threading
import time

balance = 0
my_lock = threading.Lock()      #只能锁住一个
your_lock = threading.RLock()       #同一个线程锁住后，还可以再次锁住（一个线程中可以重复锁定），  锁几次就要释放几次

def change_it(n):
    '''改变余额的方法'''
    global balance
    # #方式一,使用普通方法，需要释放锁
    # try:
    #     #获取锁
    #     #my_lock.acquire()
    #     print('start rlock')
    #     your_lock.acquire()
    #     print('start one rlock')
    #     your_lock.acquire()
    #     print('start two rlock')
    #     balance = balance + n
    #     time.sleep(2)
    #     balance = balance - n
    #     #time.sleep(1)
    #     print('--N---{0}; ---balance--{1}'.format(n, balance))
    # finally:
    #     #释放锁
    #     #my_lock.release()
    #     your_lock.release()
    #     your_lock.release()

    #方式二，使用with， 自动释放锁
    with your_lock:
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