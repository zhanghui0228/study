#类的高级特性----property
'''
    @property   将类的方法当作属性来使用
'''

class cat(object):

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    #描述这个类的一些基本信息
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        #判断value值是否为 int 类型
        if not isinstance(value, int):
            print('年龄只能是整数')
            return 0
        if value < 0 or value > 100:
            print("猫的年龄只能介于0~100之间")
            return 0
        self.__age = value

    #描述符
    @property
    def show_info(self):
        return '我叫{0}, 今年{1}岁'.format(self.name,self.__age)

    def __str__(self):
        return "{}说明信息".format(self.name)


if __name__ == '__main__':
    cat_1 = cat('花花', 2)
    rest = cat_1.show_info
    print(rest)
    cat_1.age = 5
    rest = cat_1.show_info
    print(rest)