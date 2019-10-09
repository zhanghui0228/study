#包
'''
    可以用来组织模块（可以包含其他模块的模块）
    目录必须包含文件__init__.py
    可以解决模块重名的问题

    __init.py文件的作用：
        将一个文件夹变为一个模块；
        导入包实际就是导入它的__init.py；
        一般为空，可以批量导入所需的模块

'''

import test_package
print(dir(test_package))
print(test_package.__package__)
print(help(test_package))
test_package