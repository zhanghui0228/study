# 协程之间的数据通信
'''

    嵌套调用    拿到另一个协程函数中的结果
'''
import asyncio


# async def compute(x, y):
#     ''' 定义一个计算协程函数  '''
#     print(' start compute {0} + {1} '.format(x, y))
#     await asyncio.sleep(5)
#     return x + y
#
#
# async def get_sum(x, y):
#     ''' 获取compute协程函数中返回的结果 '''
#     result = await compute(x, y)
#     print('{0} + {1} = {2}'.format(x, y, result))
#
#
# def main():
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(get_sum(1, 5))
#     loop.close()
#
#
# if __name__ == '__main__':
#     main()
#     print('*' * 60)

#---------------------------------------------------------------------------------------------------
'''
    队列  
'''

async def add(store, name):
    ''' 写入数据到队列 '''
    for i in range(6):
        #往队列中添加数字
        await asyncio.sleep(3)
        await store.put(i)

        print('{2}-->add num ...{0}, size:{1}'.format(i, store.qsize(), name))

async def reduct(store):
    ''' 删除队列中的数据 '''
    for i in range(12):
        result = await store.get()
        print('reduct num ...{0}, size:{1}'.format(result, store.qsize()))

def main():
    store = asyncio.Queue(maxsize=6)
    info_1 = add(store, 'info1')
    info_2 = add(store, 'info2')
    redu = reduct(store)

    #创建协程队列
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(info_1, info_2, redu))
    loop.close()


if __name__ == '__main__':
    main()
