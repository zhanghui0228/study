#模块的介绍
'''
    DOS常用命令：
        cd   切换目录
        dir    查看目录下的文件夹和文件
        cls     清空屏幕显示的内容
        exit    退出控制台

    模块的定义:
        模块就是程序，模块的名称就是不含.py后缀的文件名
    分类：
        python标准模块（python内置模块、python标准库）
        第三方模块/库（pypi.org）
        自定义模块
    好处：
        可维护性更强；
        方便代码的重用；

    模块导入:   import module_name
    定位： 当前包-->内置函数-->sys.path（环境变量）


    模块的属性：
        dir     --列出对象的所有属性及方法
            ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__','__package__', '__spec__', 'test']
        help    --查看类，方法的帮助信息
        __name__    --模块的名称
        __file__    --文件全路径
import sys
print(sys.path)     #查看当前环境变量

'''
import test
print(dir(test))
print(test.__name__)    #模块的名称
print(test.__doc__)     #模块的注释
print(test.__file__)    #模块文件的路径
test.add(2,5)
print(help(test))