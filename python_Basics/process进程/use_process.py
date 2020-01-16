#进程
'''
    是一个执行中的程序
    每个进程都有自己的地址空间、内存、数据栈以及其它用于跟踪执行的辅助数据
    操作系统管理其上所有进程的执行，并为这些进程合理分配时间
    进程也可以通过派生（fork或者spawn）新的进程来执行其它任务

    进程模块：
        multiprocessing     实现多进程代码
        multiprocessing.Process     创建进程
        start()             启动进程
        join()              挂起进程
        os.getpid()         获得进程的id
'''


from multiprocessing import Process
import os
import time


def run_proc(name, tim):
    '''子进程运行的代码'''
    print('Run child process {name:^10s} {pid:>10}'.format(name=name, pid=os.getpid()))
    print('process need sleep {} s'.format(tim))
    time.sleep(tim)
    print('time is sleeping done')


def use_process():
    #进程实例化
    p = Process(target=run_proc, args=('process_test', 6))
    #启动进程
    p.start()
    #挂起进程
    p.join()


if __name__ == '__main__':
    use_process()