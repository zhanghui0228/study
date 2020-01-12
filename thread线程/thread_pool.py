#线程的调度和优化

import time
import threading
from concurrent.futures.thread import ThreadPoolExecutor
from multiprocessing.dummy import Pool


def run(n):
    """ 要运行的任务 """

    time.sleep(2)
    print('thread-[{0}], num-[{1}]\n'.format(threading.current_thread().name, n))


#方法一
def use_thread_pool():
    ''' 使用线程池来进行引用 '''
    t1 = time.time()
    #运行任务的参数
    n_list = range(100)
    #定义线程池为 10个线程
    pool = Pool(10)
    pool.map(run, n_list)
    pool.close()
    pool.join() #进行阻塞
    print(time.time() - t1)


#方法二
def use_thread_executor():
    ''' 使用 ThreadPoolExecutor 来进行引用 '''
    t1 = time.time()
    n_list = range(100)
    with ThreadPoolExecutor(max_workers=10) as executor:    #使用with进行阻塞
        executor.map(run, n_list)
    print(time.time() - t1)


if __name__ == '__main__':
    # use_thread_pool()
    use_thread_executor()