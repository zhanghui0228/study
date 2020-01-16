#内存管理机制   *****
'''
    引用计数（reference count）
        每个对象都有存有指向该对象的引用总数
        查看某个对象的引用计数
            sys.getrefcount()
        可以使用del关键字删除某个引用

'''

import sys

l = []

#对象l 被引用的数量
print(sys.getrefcount(l))

#添加对l的引用
l2 = l
l3 = l
l4 = l2
print(sys.getrefcount(l))

#删除一个对l引用的对象
del l3
print(sys.getrefcount(l))

#垃圾回收
'''
    满足特定的条件，自动启动垃圾回收
    当python运行时，会记录其中分配对象（object allocation）和取消分配对象的（object deallocation）的次数
    当两者的差值高于高于某个阈值时，垃圾回收功能才会启动
    查看阈值 gc.get_threshold()
    
    分代回收
        python将所有的对象分为0、1、2三代
        所有新建对象都是0代对象
        当某一代对象经历过垃圾回收，依然存活，那么它就被归入下一代对象
    
    手动回收
        gc.collect()手动回收
        objgraph模块中的count()记录当前类产生的实例对象的个数
        gc.set_threshold(threshold0[, threshold1[, threshold2]])
        
    通过objgraph.count()  来进行观察实例对象的计数
'''

#内存管理机制
'''
    内存池（memory pool）机制
        当创建大量消耗小内存的对象时，频繁调用new/malloc会导致大量的内存碎片，致使效率降低。内存池的概念就是预先在内存中申请一定数量的，大小相等的内存块留作备用，当有新的内存需求的时候，就先从内存池中分配内存给这个需求，不够了之后在申请新的内存，这样最显著的优势就是能够减少内存碎片，提升效率
    
    python3中的内存管理机制----Pymalloc
        针对小对象（<=512bytes）,pymalloc会在内存池中申请内存空间
        当>512bytes，则会PyMem_RawMalloc()和PyMem_RawRealloc()来申请新的内存空间
'''