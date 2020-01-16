#文件的写入

'''
    使用write 函数向打开的文件对象写入内容
    使用writelines 函数向打开的文件对象写入多行内容

    换行符： \r、 \n、 \r\n
'''

from datetime import datetime
import random

file_name = "write_test.txt"
def write_file():
    '''
    写入文件
    :return:
    '''
    #打开文件
    with open(file_name, "a", encoding="utf8") as f:        #文件内容以追加的方式进行写入
        #向文件中写入内容
        f.write("hello, world\n")
        f.write("this is test")

def write_lines_file():
    """
    写入多行数据
    :return:
    """
    with open(file_name, 'w', encoding="utf8") as f:
        f.writelines(["第一行","\n","第二行","\r","第三行","\r\n","第四行"])


def write_user_log():
    '''
    模拟记录用户的访问时间
    :return:
    '''
    with open(file_name, 'w', encoding='utf8') as f:
        for i in range(10):
            result = '用户:{0} -- 时间:{1},"\n'.format(random.randint(1, 100), datetime.now())
            f.write(result)


def  read_file():
    '''
    读取写入的文件
    :return:
    '''
    with open(file_name, 'r', encoding="utf8") as f:
        result = f.readlines()
        print("写入文件共", len(result), "行")
        for file in result:
            print(file)

if __name__ == '__main__':
    #write_file()
    #write_lines_file()
    write_user_log()
    read_file()