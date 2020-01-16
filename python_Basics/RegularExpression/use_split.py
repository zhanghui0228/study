#split()正则分割
'''
    书写格式：
        split(pattern, string, max=0)
        根据正则表达式的模式分隔符，split函数将字符串分割为列表，然后返回成功匹配的列表，分割最多操作max次（默认分割为所有匹配成功的位置）
'''
import re

#使用split正则分割字符串
s = 'one1two2three3four4five5six6'
p = re.compile(r'\d+')
result = p.split(s)
print(result)


#sub()正则替换
'''
    书写格式：
        sub(pattern, repl, string, max=0)
    使用repl替换string中每一个匹配的子串后返回替换后的字符串，最多操作max次（默认替换所有）
'''

#使用正则表达式进行替换

pattern = re.compile(r'\d+')
resultSub = pattern.sub('&', s, 6)
print(resultSub)

#使用字符串方式进行替换  replace
resultReplace = s.replace('1', '#').replace('5', '#')
print(resultReplace)

#在原有的基础上替换并改变内容

info = 'hello world'
pattern_info = re.compile(r'(\w+) (\w+)')


def f(m):
    '''使用函数替换规则并改变内容'''
    return m.group(2).upper() + ' ' + m.group(1)


result_change = pattern_info.sub(f, info)
print(result_change)