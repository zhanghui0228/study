#次脚本为测试练习使用

'''
    1、定义一个类为Hello
    2、类的传入值为 name, number
    3、设置描述信息
    4、禁止更改number其对应的值

'''

class Hello(object):

    tag = 'info'

    def __init__(self, name, number):
        self.name = name
        self.__number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not isinstance(value, int):
            print('有非法字符， 注：号码只能是数字，不可以是其它字符')
            return 0
        self.__number = value


    def get_info(self):
        info = '名称：{0}, 座机号：{1}'.format(self.name, self.__number)
        return info


if __name__ == '__main__':
    info_1 = Hello('警察局', 110)
    info_2 = Hello('急救中心', 120)
    info_3 = Hello('火警电话', 119)
    result = info_1.get_info()
    print(result)
    info_1.number = '110'
    result = info_1.get_info()
    print(result)