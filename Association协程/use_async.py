import asyncio


async def do_sth(x):
    ''' 定义协程函数 '''
    print('sleep {0}...'.format(x))
    await asyncio.sleep(x)
    return 'pass'


#判断是否为协程函数
print(asyncio.iscoroutinefunction(do_sth))

coroutine = do_sth(6)
#事件的循环队列
loop = asyncio.get_event_loop()

#将协程函数加入到事件循环队列
task = loop.create_task(coroutine)
print(task)

#等待协程任务执行完成
loop.run_until_complete(task)
print(task)
print('-' * 60)

