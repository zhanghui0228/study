#文件的读取

'''
    'r'     读取模式（默认值）
    'w'     写入模式（每次写入会覆盖掉之前的内容）
    'x'     独占写入模式
    'a'     附加模式（写入模式，追加）
    'b'     二进制模式（与其他模式相结合使用）
    't'     文本模式（默认值，与其他模式结合使用）
    '+'     读写模式（与其他模式结合使用）


    文件的打开和关闭
    使用 open 函数打开文件
    使用close函数关闭文件

    语法：
        f = open('filename', module='r')    --打开文件
        ......
        ......
        f.close()   --关闭文件

    with        --到达语句末尾时，将自动关闭文件
    语法： with open("filename") as f:
                do_somethong(f)
'''



"""
    文件的读取：
        read():读取文件，可以指定参数，表示读几个字符（字节）
        readlin(): 读取一行参数，可以指定参数，表示读前几个字符（字节）
        readlins(): 读取所有的行，并返回列表
"""

def read_file():
    '''
    读取文件
    :return:
    '''
    file_name = 'test.txt'
    #使用绝对路径
    file_path = 'C:\\pycharm\\projects\\study\\module\\file\\test.txt'
    #使用普通方式打开文件
    f = open(file_name, "r", encoding="utf8")
    #读取文件
    #result = f.read()
    #读取指定字符
    result = f.read(2)
    print(result)
    print(f.read(3))        #文件不会从头开始读，会根据上一个继续往下进行截取

    #随机读取
    f.seek(5)   #间隔2个进行读取，只读取英文字符
    print(f.read(4))
    #关闭文件
    f.close()

if __name__ == '__main__':
    read_file()


def readline_file():
    '''
    读取文件一行
    :return:
    '''
    file_name = "test.txt"
    #打开文件
    f = open(file_name, "r", encoding="utf8")
    #按行读取文件
    result = f.readline()
    print(result)
    print(f.readline(6))
    #关闭文件
    f.close()

if __name__ == '__main__':
    readline_file()

def readlines_file():
    '''
    读取文件所有行
    :return:
    '''
    file_name = "test.txt"
    #打开文件
    #f = open(file_name, "r", encoding="utf8")
    with open(file_name, "r", encoding="utf8") as f:    #注意，当使用with 打开文件时，无需使用 close()函数进行关闭文件
        #读取文件所有行
        result = f.readlines(2)     #指定内存大小，防止读取大文件占取大量内存
        print(result)
    #关闭文件
    #f.close()

if __name__ == '__main__':
    readlines_file()