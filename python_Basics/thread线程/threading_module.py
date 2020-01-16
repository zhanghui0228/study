#实现一个线程
'''
    用threading模块代替thread模块
    实现一个线程：
        用threading.Tread创建线程
        start()启动线程
        join()挂起线程
'''

#threading 模块
import threading
import time

'''
    Thread  表示一个执行线程的对象
    Lock    锁原语对象（和thread模块中的锁一样）
    RLock   可重入锁对象，使单一线程可以（再次）获得已持有的锁（锁归锁）
    Condition   条件变量对象，使得一个线程等待另一个线程满足特定“条件”， 比如改变状态或某个数据值
    Event   条件变量的通用版本，任意数量的线程等待某个事件的发生，在该事件发生后所有线程将被激活
    Semaphore   为线程间共享的有限资源提供一个“计数器”，如果没有可用资源时会被阻塞
    BoundedSemaphore    与Semaphore相似，不过它不允许超过初始值
    Timer   与Thread相似，不过它在运行前等待一段时间
    Barrier     创建一个“障碍”，必须达到指定数量的线程后才可继续
    
    Thread对象数据属性
        name    线程名
        ident   线程标识符
        daemon  布尔标志，表示这个线程是否守是守护线程
        
    Thread对象方法：
        __init__()  实例化一个线程对象，需要拥有一个可调用的target，以及其参数args或kwargs
        start()     开始执行该线程
        run()       定义线程功能的方法（通常在子类中被应用开发者重写）
        join    (timeout=None)  定义直至启动的线程终止之前一直挂起；除非给出了timeout（秒），否则会一直阻塞
        getName()   返回线程名
        setName(name)   设定线程名
        isAlive /is_alive() 布尔标志，表示守护这个线程是否还存活
        isDaemon()  如果是守护进程，则返回True；否则返回False
        setDaemon()     把线程的守护标志设定为布尔值daemonic（必须在现场start()之前调用）             
'''

def loop():
    '''新线程执行的代码'''
    n = 0
    while n < 5:
        print(n)
        time.sleep(1)
        n += 1


def test_thread():
    ''' 使用线程来实现 '''
    #当前正在执行的线程
    now_thread = threading.current_thread()
    print('now thread name: {0}'.format(now_thread.name))
    #设置一个线程
    thread = threading.Thread(target=loop, name="loop_thread")
    #获取当前执行的线程名
    now_run_thread = thread.getName()
    print("now run thread name : {0}".format(now_run_thread))
    #启动线程
    thread.start()
    #挂起线程
    thread.join()


if __name__ == '__main__':
    test_thread()


#自定义线程

class LoopThread(threading.Thread):
    ''' 自定义线程 '''
    x = 0
    thread = threading.current_thread()
    print("this is threading name {0}".format(thread.getName()))
    def run(self):
        now_thread = threading.current_thread()
        print("now_my_thread name : {0}".format(now_thread.name))
        while self.x < 10:
            print(self.x)
            time.sleep(2)
            self.x += 1


if __name__ == '__main__':
    t = LoopThread(name="MyLoopThread")
    t.start()
    t.join()