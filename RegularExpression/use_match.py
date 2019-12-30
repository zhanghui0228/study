#使用compile 和 match

import re

# 将正则表达式编译，不区分大小写
pattern = re.compile(r'hello', re.I)

# 通过match进行匹配
result = pattern.match("Hello, world, hello")
info = pattern.findall("Hello, world, hello")
print(result)
print(info)