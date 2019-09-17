#字典
'''
    字典（dictionary）是python中的内置数据结构
    字典适合表达结构化的数据
    特点：
        采用键(key):值(value)形式表达数据；
        key不允许重复，value允许重复；
        是可以修改的，运行时动态调整存储空间
    创建字典的两种方式：
        1、使用{}创建字典；
        2、使用dict函数创建字典

    dict.fromkeys(['key1', 'key2'], 'N/A')
'''

#字典的创建
#1、使用{}来进行创建
dict1 = {}  #空字典
dict2 = {"name":"张三", "age":29}
print(dict2)
#2、使用dict函数来进行创建
dict3 = dict(name='李四', age=27)     #此刻中的key不需要使用引号， key 和value之间使用 = 来进行衔接
print(dict3, type(dict3))

dict4 = dict.fromkeys(['name', 'age'],'N/A')      #传入一个列表作为key
print(dict4)
'''
#字典的取值
#方式一    --dict['key']
employee = {"name":"张三", "age":29}
name = employee['name']
print(name)
#方式二    --dict.get('key')
get_name = employee.get('name')
print(get_name)
get_name1 = employee.get('old', 'N/A')  #如果不存在值，则输出自定义的value
print(get_name1)

#判断当前的key是否存在在字典中   --使用成员运算符 in
print('name' in employee)
print('class' in employee)
'''
#遍历字典
employee = {"name":"张三", "age":29, "class":'B5'}
#方法一：   遍历字典中的key
for key in employee:
    v = employee[key]
    print("{key}:".format(key=key), v)

#方法二    遍历字典中的key,value
for key,value in employee.items():      #dict.items()   返回字典中的每一个键值对
    print(key, ":", value)


#字典更新与删除操作
