#可变类型的数据集合
'''
    列表：list
    元组：tuple
    字典：dict
    集合：set
    数据结构：是指计算机存储、组织数据的结构
'''

#列表（list）
'''
    列表中的数据按顺序排列；
    列表有正序和倒叙两种索引
        --正序： 索引从0开始
        --倒叙： 索引从-1开始
    列表中可以存储任意类型的数据，且允许重复
    
    列表格式：
        变量名 = [元素1, 元素2,...]
    取值格式：
        变量名 = list[目标索引位置]
    取值范围：
        变量名 = list[目标起始索引:目标结束索引]
        在python中列表取值范围是“左闭右开”
'''
'''
#示例
list = ['a', 'b', 'c', 'd', 1, 2, 3, 4]
print(list[3])  #list取值
print(list[1:4][-1])    #list范围取值
#获取指定元素的索引值
print(list.index('c'))
'''
#使用for语句遍历列表
'''
    for .. in语句专门用于遍历列表、元组等数据结构
    语法：
        for 迭代变量 in 可迭代对象:
            循环体（必须缩进）
'''
'''
#基础语句
for l in list:
    print(l, list.index(l))
list_test = ['a', 'b', 'c', 'd', 'c', 1, 2, 3, 4]
#进阶语句   --打印同一列表中元素名称一样的索引值
i = 0
for p in list_test:
    if p == 'c':
        print(p, i)
    i += 1

#获取列表的长度
print(len(list_test))
#得到列表中的倒叙索引
i = 0
for p in list_test:
    if p == 'c':
        ri = len(list_test) * -1 + i
        print(p, i, ri)
    i += 1

#使用while语句进行遍历列表
i = 0
while i < len(list_test):
    p = list_test[i]
    ri = len(list_test) * -1 + i
    if p == 'c':
        print(p, i, ri)
    i += 1
'''
#编程练习：
'''
    打印1到10里面的偶数
'''
'''
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numList:
    if i % 2 == 0:
        print(i)
'''

#列表的反转与排序
list_test = ['a', 'b', 'c', 'd', 'c', 1, 2, 3, 4]
list_test.reverse() #reverse方法用于反转列表
print(list_test)

numlist = [1, 5, 2, 23, 14]
numlist.sort()  #sort方法用于排序列表 --默认为升序
#用到的算法 ----冒泡排序
numlist.sort(reverse=True)  #sort(reverse=True)方法用于降序排序列表
print(numlist)

#创建空list
list1 = []
#列表的增删改
'''
    list.append(新元素)    #在列表末端追加新元素
    list.insert(索引，新元素) #在指定索引位置插入新元素
    list[索引] = 新值   #更新指定索引位置的数据
    list[起始索引:结束索引你] = 新列表  #更新指定范围数据
    lisr.remove(元素) #按元素内容删除指定元素
    list.pop(索引)    #按索引删除指定元素
    list[起始索引:结束索引] = []    #指定索引范围删除元素
    list.count(元素)  #统计指定元素在list中出现的次数
    list.extend([元素1， 元素2]) #在list末尾一次性追加多个元素
    元素 in list  #判断指定元素在列表中是否存在，存在返回值True，不存在返回值False
    新变量名 = list.copy    #用于复制列表
    list.clear()    #用于清空列表（删除所有元素）
'''
'''
#列表的其他使用方法
list_test = ['a', 'b', 'c', 'd', 'c', 1, 2, 3, 4]
cnt = list_test.count('c')    #统计指定元素在list中出现的次数
print(cnt)
list_test.extend(['e', 'f'])        #在list末尾一次性追加多个元素
print(list_test)
print ('c' in list_test)

#copy函数用于复制列表
list2 = list_test.copy()
print(list2)

#clear函数用于清空列表
list2.clear()
print(list2)
'''

#编程练习
'''
    定义一个列表list1为[23, 98, 56, 55, 76, 98, 55]，对列表去重之后降序排序

    任务 
        1、定义list2为空列表
        2、循环遍历list1 
        3、if判断list1中的每个元素是否在list2中
        4、如果元素不在list2中，则将元素追加到list2中
        5、使用sort对list2进行降序排序
'''
list1 = [23, 98, 56, 55, 76, 98, 55]
list2 = []
for li in list1:
    if li not in list2:
        list2.append(li)
list2.sort(reverse=True)
print(list2)