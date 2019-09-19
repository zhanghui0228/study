#元组(tuple)
'''
    元组是"不可变"的列表（list）
    元组使用小括号来进行表示
    元组书写格式：
        格式一：    tup1 = ('abc', 'bcd', 123, 456)
        格式二：    tup2 = 'abc', 'bcd', 1, 2, 3
'''

#元组的读写
'''
    元组的读取方式与列表读取的方式是相同的
    元组创建完元素后，元素不允许修改，如果元组内持有列表，则元组内的列表可以被修改
    元组允许使用"元组运算符"来进行创建新的元组      元组运算符同样适用于列表
'''
t1 = (['张三', 20, 2000], ['李四', 22, 2200])
#print(t1[0])
item = t1[0]
item[1] = 25
print(t1)

#使用“元组运算符”创建新的元组
new_tup1 = (1, 2, 3) + (4, 5, 6)
new_tup2 = ("i", 'love') * 2
new_tup3 = ('me',) * 2       #如果元组中只有一个元素时，必须在元素后面添加一个逗号，说明这是一个元组，否则python会将其看作一个字串串来进行运行
print(new_tup1)
print(new_tup2)
print(new_tup3)


#序列
'''
    序列(sequence)是指”有序“的队列，  是一种数据结构的统称
    符合以下两种即可称之为序列：
        序列中的元素顺序按添加顺序排列；
        序列中的数据是通过”索引“来进行获取的
    序列包含的数据结构：
        字符串(str)、列表(list)、元组(tuple)、数字序列(range)
        
数字序列(range)：
    用于表示数字序列，内容不可变
    使用range()函数来进行创建
    语法：
        range(起始值,结束值)  --左闭右开
'''
#range
r = range(1,10)
print(type(r), r)
r1 = r[8]       #range取值
print(r1)
#设置range的步长（间隔）
r2 = range(1,10, 2)
print(r2[4])
#使用成员运算符进行判断
print(5 in r2)
print(6 in r2)

#打印斐波那契数列
result = []
for i in range(0,50):
    if i == 0 or i == 1:
        result.append(1)
    else:
        result.append(result[i - 2] + result[i - 1])
print(result)

#编程练习
'''
有四个数字1、2、3、4，能组成多少个互不相同且数字不重复的两位数
任务
1、 定义变量count，用于存放统计出所组成的两个数的个数
2、定义变量lst，用于存放组成后的两位数
'''
count = 0
for i in range(1,5):
    for n in range(1,5):
        if i != n:
            count += 1
print(count)

#序列类型的互相转换
'''
    list()      转换为列表
    tuple()     转换为元组
    join()、str()    转换为字符串
        str()函数用于将单个数据转为字符串
        join()函数用于对列表进行连接       --要求：必须所有元素都是字符串
'''
L1 = ['a', 'b', 'c']
#使用join函数将列表进行连接
print("".join(L1))      #""表示多个元素的分割符
print(",".join(L1))