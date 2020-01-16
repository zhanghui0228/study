#文件备份
'''
    用到模块：
    os
    os.path
    文件读写
'''

import os
import os.path

#当前代码文件的目录名称
Path = os.path.dirname(os.path.abspath(__file__))

class BackFile(object):
    '''
    文本文件备份
    '''

    def __init__(self, src, dest):
        """
        构造方法
        :param src: 需要备份文件路径
        :param dest:    备份到目标的目录
        """
        self.src = src
        self.dest = dest

    def read_file(self):
        """
        读取src目录下的所有文件
        """
        fileList = os.listdir(self.src)
        for f in fileList:
            self.backupFile(f)

    def backupFile(self, file_name):
        '''
        处理文件备份
        要求：
            1、判断dest是否存在，如果不存在，则进行创建
            2、判断文件是不是指定的文件类型（借助文件后缀名进行判断）
            3、读取文件内容
            4、将读取到的内容写入到新的文件中
        :param file_name:
        :return:
        '''
        #判断dest是否存在，如果不存在，则进行创建
        if not os.path.exists(self.dest):
            os.makedirs(self.dest)
            print("{0} 目录创建成功".format(self.dest))

        #拼接为完整的路径
        full_src_path = os.path.join(self.src, file_name)
        full_dest_path = os.path.join(self.dest, file_name)
        #判断文件是不是指定的文件类型（借助文件后缀名进行判断）
        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == '.txt':
            #将读取到的内容写入到新的文件中
            # 读取文件内容
            with open(full_dest_path, 'w', encoding='UTF8') as dest_f,\
            open(full_src_path, 'r', encoding='UTF8') as src_f:
                print('#' * 50)
                print("开始备份>> {0} 文件到 {1}".format(full_src_path,full_dest_path))
                while True:
                    info = src_f.read(100)
                    dest_f.write(info)
                    if not info:
                        break
                dest_f.flush()
                print("完成 {0} 文件到 {1} 的备份".format(full_src_path, full_dest_path))
                print('#' * 50)
        else:
            print('#' * 50)
            print("{0}文件类型不符合备份要求，跳过>>".format(full_src_path))

if __name__ == '__main__':
    src_path = os.path.join(Path, 'src')
    dest_path = os.path.join(Path, 'dest')
    bak = BackFile(src_path, dest_path)
    bak.read_file()