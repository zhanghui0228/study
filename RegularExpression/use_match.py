#使用compile 和 match

import re

# 将正则表达式编译，不区分大小写
pattern = re.compile(r'hello', re.I)

# 通过match进行匹配
#使用编译对象
result = pattern.match("Hello, world, hello")

#不使用编译对象
info = re.match(r'hello', 'Hello, world, helLo', re.I)
print(result)
print(info)

#==========================================================================================
#findall()的使用
'''
    书写格式：
        findall(pattern, string[,flags])
    查找字符串中所有（非重复）出现的正则表达式模式，并返回一个匹配列表
'''

content = 'one1two22Three334four43Five5six66'
pat_num = re.compile(r'\d+', re.I)
#pat_str = re.compile(r'[a-z]+', re.I)

#使用编译的对象
rest_num = pat_num.findall(content)

#不使用编译的对象
rest_str = re.findall(r'[a-z]+', content, re.I)
print(rest_num)
print(rest_str)

#=========================================================================================
#search()的使用
'''
    书写格式：
        search(pattern, string, flags=0)
    使用可选标记搜索字符串中的第一次出现的正则表达式模式。如果匹配成功，则返回匹配对象；如果匹配失败，则返回None
'''

pat_search = re.compile(r'two', re.I)
rest_search = pat_search.search(content)
print(rest_search)

#match VS search
'''
    match   从开头匹配，不全局
    search  全局匹配
'''

#======================================================================================
#group()与groups的使用
'''
    group(num)返回整个匹配对象或编号为num的特定子组
    groups()：返回一个包含所有匹配子组的元组（如果没有成功匹配，则返回一个空元组）
    
'''
con = 'hello world!'
p = re.compile(r'world', re.I)
rsu = p.search(con)
print(rsu)
if rsu:
    print(rsu.group())