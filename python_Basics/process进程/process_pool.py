#进程池
'''
    #now_process = current_process()     #当前进程
'''
import time
from multiprocessing import current_process, Pool


def run(file_name, i):
    '''
    多线程执行的代码    ---写入文件
    :param file_name:   str 文件名称
    :param i:   int 写入的数字
    :return:
    '''
    now_process = current_process()
    with open(file_name, 'a+', encoding='utf-8') as f:
        context = 'RUN process name :{name:>10}, pid：{pid:>10}, num :{num:>10}\n'.format(name=now_process.name, pid=now_process.pid, num=i)
        f.write(context)
        time.sleep(4)
        print(context)
    return 'pass'


def ProcessPool():
    file_name = 'pool.txt'
    #定义开启的进程池个数
    pool = Pool(2)
    for i in range(20):
        #同步添加任务
        #result = pool.apply(run, args=(file_name, i))
        #异步添加任务
        result = pool.apply_async(run, args=(file_name, i))
        print('NUM:{0}-------INFO:{1}'.format(i, result))   #异步任务可以添加result.get(5)   设置超时时间，其效果与同步效果一样
    #关闭进程池
    pool.close()
    pool.join()


if __name__ == '__main__':
    ProcessPool()