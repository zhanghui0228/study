#字典的常用操作
'''
    为字典设置默认值；
        dict.setdefault('key', 'default_value')     #设置默认值，如果key已经存在，则忽略；如果key不存在，则设置
    字典的视图；
    字典的格式化输出；
'''
'''
emp1 = {'name':'Jack', 'grade':'B'}
emp2 = {'name':'Liay'}
#设置默认值
emp2.setdefault('grade', 'D')       #方法一：设置默认值
if 'grade' not in emp2:             #方法二：使用成员运算符进行判断设置默认值
    emp2['grade'] = 'C'

print(emp2)
'''
#获取字典的视图
'''
    1、keys  代表获取所有的键    dict.keys()
    2、values 代表获取所有的值   dict.values()
    3、items 代表获取所有的键值对  dict.items()
'''
'''
emp_test = {'name':'Jack', 'grade':'B'}
#1、keys  代表获取所有的键
ks = emp_test.keys()
print(ks)
#2、values 代表获取所有的值
vs = emp_test.values()
print(vs)
#3、items 代表获取所有的键值对
itms = emp_test.items()
print(itms)
'''
#利用字典格式化字符串
'''
    老版本格式化字符串书写格式：  "名称:%(dict_key)s" %dict_name
    新版本格式化字符串书写格式：   "名称:{dict_key}".format_map(dict_name)
'''
#老版本的字符串格式化：
'''
emp_str = "姓名:%(name)s, 评级:%(grade)s" %emp_test
print(emp_str)

#新版本的字符串格式化：
emp_str1 = "姓名:{name}, 评级:{grade}".format_map(emp_test)
print(emp_str1)
'''

#编程练习
# 创建字典dict01
dict01 = {"name":"小王", "age":18, "sex":"女", "dept":"技术部"}
# 使用for循环遍历字典dict01的键值对
for key,value in dict01.items():
    print(key, value)
# 向控制台输出键和值
ks = dict01.keys()
vs = dict01.values()
print (ks)
print (vs)


