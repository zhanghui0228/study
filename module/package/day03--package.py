#包
'''
    可以用来组织模块（可以包含其他模块的模块）
    目录必须包含文件__init__.py
    可以解决模块重名的问题

    __init.py文件的作用：
        将一个文件夹变为一个模块；
        导入包实际就是导入它的__init.py；
        一般为空，可以批量导入所需的模块

    引入整个包：  import module
    只引入所需要的属性和方法    from module.xx import xx
    指定别名：       from module.xx import xx as rename
    引入所有：       from module.xx import *

    注意事项：
        其它叫法：   包的引入、模块导入、模块引入
        模块导入的重名名（as）遵循python变量的命名规范

    import顺序：
        1、标准库
        2、第三方包
        3、自定义的包/模块
'''

#包的调用方法
from pay.pay1 import tools
print(dir(tools))
print(tools.__package__)
print(help(tools))
tools.add()

def func():
    from pay import tool
    print(dir(tool))
    print(help(tool))
    tool.update()

def fun1():
    from pay.tool import update
    from pay.pay1.tools import add
    update()
    add()

def fuc():
    import pay
    pay.pay1.tools.add()
if __name__ == '__main__':
    func()
    fun1()
    fuc()