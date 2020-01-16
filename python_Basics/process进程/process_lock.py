#多进程中的锁
'''
    Lock()
    RLock()
'''

#展现出锁
import time
from multiprocessing import Process, Lock, RLock


class WriteProcessLock(Process):
    tag = '写入文件是遇到的锁'

    def __init__(self, file_name, sum, lock, *args, **kwargs):
        self.file_name = file_name
        self.sum = sum
        self.lock = lock
        super().__init__(*args, **kwargs)

    def run(self):
        ''' 写入文件的主要逻辑 '''
        # #方法一 最后需要关闭锁
        # try:
        #     #添加一个锁
        #     self.lock.acquire()
        #     print('locked')
        #     self.lock.acquire()         #此时会产生死锁
        #     print('relocked')
        #     for i in range(5):
        #         context = 'Write Process name {name:>10}, pid {pid:>10}, num {num:>10}\n'.format(name=self.name, pid=self.pid, num=self.sum)
        #         with open(self.file_name, 'a+', encoding='utf-8') as f:
        #             f.write(context)
        #             time.sleep(3)
        #             print(context)
        # finally:
        #     self.lock.release()
        #     self.lock.release()
        #方法二    最后无需关闭锁
        with self.lock:
            print('locked')
            print('relocked')
            for i in range(5):
                context = 'Write Process name {name:>10}, pid {pid:>10}, num {num:>10}\n'.format(name=self.name,
                                                                                                 pid=self.pid,
                                                                                                 num=self.sum)
                with open(self.file_name, 'a+', encoding='utf-8') as f:
                    f.write(context)
                    time.sleep(3)
                    print(context)


def mainLock():
    file_name = 'test.txt'
    #锁对象
    # lock = Lock()     #有两个锁时会产生死锁
    lock = RLock()      #有两个锁时不会产生死锁
    for x in range(5):
        p = WriteProcessLock(file_name, x, lock)
        p.start()


if __name__ == '__main__':
    mainLock()
