'''
    协程就是协同多任务
    协程在一个进程或者是一个线程中执行
    不需要锁机制
    多多核CPU的利用---多进程+协程

    协程实现：
        v3.5之前：
            使用生成器（yield）实现
        v3.5之后：
            使用async 和await 关键字实现

    async关键字：
        定义特殊函数
            async def asycn_f():
                pass
        当被掉用的时，不执行函数里面的代码，而是返回一个协程对象
        在事件循环中调度其执行前，协程对象不执行任何操作

    await关键字：
        等待协程执行完毕
        当遇到阻塞调用的函数时，使用await方法将协程的控制器让出，已便loop（事件循环队列）调用其它的协程


    asyncio模块：
        get_event_loop()获得事件循环队列
        run_until_complete()注册任务到队列
        在事件循环中调度其执行前，协程对象不执行任何操作
        asyncio模块用于事件循环
'''


#生成器
import time


def count_donw(n):
    ''' 倒计时的实现 '''
    while n >= 0:
        yield n
        time.sleep(1)
        n -= 1


def yield_test():
    ''' 实现协程函数 '''
    while True:
        n = (yield )
        print(n)


if __name__ == '__main__':
    # num = int(6)
    # result = count_donw(num)
    # for i in range(num+1):
    #     print(next(result))
    result = yield_test()
    next(result)
    for i in range(10):
        result.send(i)