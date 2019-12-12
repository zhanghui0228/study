#类的高级特性----property
'''
    @property   将类的方法当作属性来使用
'''

class cat(object):

    def __init__(self, name):
        self.name = name

    #描述符
    @property
    def show_info(self):
        return '我叫{}'.format(self.name)

    def __str__(self):
        return "{}说明信息".format(self.name)


if __name__ == '__main__':
    cat_1 = cat('花花')
    rest = cat_1.show_info
    print(rest)