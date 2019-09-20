##########集合(set)
'''
    集合（set）是python中的内置数据结构
    集合可以看作是一个没有value的dict
    书写格式：
        方法一：    {'key1', 'key2'}
        方法二：    set()函数创建
    特点：
        集合元素是无序的；
        集合元素是不可重复的；
        集合是可变的；
        集合允许数学运算；
        集合是分散存储的
'''
'''
#集合的创建
games = {"LOL", "CF", "DNF",}
print(games)
#使用set()内置函数从其他数据结构进行转换
ga = set(["LOL", "CF", "DNF"])
print(ga)
#使用set创建字符串的集合
college = set("i lova ")
print(college)

#创建空集合
college1 = set()
print(type(college1))
'''

##########集合关系与数学运算
'''
    集合所特有的：
        交集（intersection）    set1.intersection(set2)
        并集（union）           set1.union(set2)
        差集（difference）      set1.difference(set2)   单向差集
                                set1.symmetric_difference(set2)   双向差集
'''
games1 = {"LOL", "CF", "DNF",}
games2 = {"LOL", "CF", "DNF", "QQ"}

#交集
game1 = games1.intersection(games2)
print(game1)
#并集
game2 = games1.union(games2)
print(game2)
#单向差集
game3 = games2.difference(games1)
print(game3)
#双向差集
game4 = games1.symmetric_difference(games2)
print(game4)

#####编程练习
a_list = [1, 2, 3, 4, 5]
b_list = [1, 4, 7, 9]
#并集
int_set = set(a_list).intersection(set(b_list))
print(list(int_set))
#交集
un_set = set(a_list).union(set(b_list))
print(list(un_set))
#差集
diff_set = set(a_list).difference(set(b_list))
print(list(diff_set))


####集合间的关系操作
'''
    判断一个集合是否是另一个集合的子集   set1.issubset(set2)
    判断集合是否是另一个集合的父集         set2.issuperset(set1)
    判断两个集合内是否有重复的元素    set1.isdisjoint(set2)    --返回True代表不存在，False代表存在重复元素
'''
#判断两个集合是否相等
s1 = {1, 2, 3, 4}
s2 = {4, 3, 2, 1}
print(s1 == s2)
#判断集合是否是另一个集合的子集
s3 = {3, 4, 5}
s4 = {1, 2, 4, 3, 6, 5}
print(s3.issubset(s4))
#判断集合是否是另一个集合的父集（包含另一个子集）
print(s4.issuperset(s3))

#判断两个集合内是否有重复的元素        --返回True代表不存在，False代表存在重复元素
s5 = {5}
s6 = {1, 2, 3, 4, 5, 6}
print(s5.isdisjoint(s6))

######集合的增删改查
'''
    集合不支持更新操作，如若更新需要先删除已有元素，在添加元素
    set.add("元素")       向集合中新增数据
    set.update(["元素1", "元素2"])      向集合中一次性插入多条数据
    set.remove("元素")        删除指定的元素，如若删除不存在的元素，程序则会报错
    set.discard("元素")       删除指定的元素，若若删除不存在的元素，程序则会忽略删除操作
'''
#集合的遍历
games = {"LOL", "CF", "DNF", "QQ"}
for g in games:
    print(g)
#判断元素是否存在
print("LOL" in games)
#集合的查看      ---不支持按索引来提取数据

#集合新增数据     --一次添加一个元素
games.add("绝地求生")
print(games)

#使用update一次进行添加多个元素
games.update(["流星蝴蝶剑", "人类一败涂地"])
print(games)

#集合删除元素
games.remove("QQ")
games.discard("流星蝴蝶剑")
print(games)


###python中三种内置生成式
'''
    生成式语法：  [被追加的数据 循环语句 循环语句或者判断语句]|{}
    列表生成式
    字典生成式
    集合生成式
'''
#正常表达式
lst = []
for i in range(10,20):
    if i % 2 == 0:
        lst.append(i * 10)
print(lst)
#列表生成式
lst1 = [i * 10 for i in range(10,20) if i % 2 == 0]
print(lst1)

#字典表达式
name = ["张三", "李四", "王五"]
dict1 = {i + 1:name[i] for i in range(0,len(name))}
print(dict1)

#集合表达式
set1 = {i * j for i in range(1,4) for j in range(1,4) if i == j}
print(set1)


# 编程练习
'''
    lst = [23,45,22,44,25,66,78]
    用列表生成式完成下面习题：
    1、生成lst列表中所有奇数组成的列表
    2、与lst列表相比较，使用相应的列表生成式，使得输出结果[28, 50, 27, 49, 30, 71, 83]
'''
lst = [23,45,22,44,25,66,78]
list1 = [i for i in lst if i % 2 != 0]
print(list1)
list2 = [i + 5 for i in lst]
print(list2)