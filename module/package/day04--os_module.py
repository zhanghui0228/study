#标准模块与第三方模块
'''
    os模块
    os.environ     包含环境变量的映射
    os.system(command)     在子shell中执行操作系统命令
    os.sep         路径中使用分隔符
    os.pathsep     分割不同路径的分隔符
    os.linesep     行分隔符（'\n','\r',或'\r\n'）
    os.urandom(n)      返回n个字节的强加密随机数据
    os.argv        命令行参数，包括脚本名
    os.getcwd      返回当前所在目录
    os.chdir('path')       跳转到指定目录
    os.listdir()       当前路径的所有文件
    os.rename('source_name', 'dest_name')
    os.modules     一个字典，将模块名映射到加载的模块
    os.path        一个列表，包含要在其中查找模块的目录的名称
    os.platform    一个平台标识符，如sunos5或win32
    os.mkdir/os.rmdir     创建和删除文件夹
    os.makedirs      创建多层文件夹
    os.path     文件目录相关操作

    os模块对文件目录的操作：
    os.path.isdir('path')       判断是否是目录
    os.path.isfile('path')      判断是否是文件
    os.path.exists('path')       判断文件目录是否存在
    os.path.dirname('文件的绝对路径')        获取文件所在的路径
    os.path.split('文件的绝对路径')          将文件所在的路径和文件名以元组的形式进行打印
    os.path.basename('文件的绝对路径')         打印文件名称
    os.path.splitext('文件的绝对路径')         将文件所在的路径（包含文件名，不包含后缀）和文件后缀名以元组的形式进行打印
    os.path.join('path1', '子文件夹1', '子文件夹2')     以系统分隔符将内容进行整合拼接

'''

#os模块的使用
import os
print(os.environ)   #查看系统变量
#os.system('calc')   #打开计算器
print(os.sep)              #路径中的分隔符
print(os.getcwd())      #获取当前路径
#os.chdir('C://')        #跳转到指定路径
print(os.listdir())     #查看当前路径存在哪些文件

#os.path对文件目录的操作：
file = 'D:\\projects\\study\\module\\package\\test.txt.py'
print(os.path.isdir('pay'))     #判断是否为一个目录
print(os.path.exists('pay'))    #判断是否存在
print(os.path.isfile('test.txt.py'))    #判断是否是一个文件
print(os.path.dirname(file))        #获取文件所在的路径
print(os.path.split(file))          #将文件的路径和文件名称以元组的形式进行打印
print(os.path.basename(file))       #打印文件的名称
print(os.path.splitext(file))       #将文件的路径（包含文件名，不包含后缀）和后缀名以元组的形式进行打印
print(os.path.join(file, 'test1', 'hh'))      #以系统分隔符将内容进行整合拼接