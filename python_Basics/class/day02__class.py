#类的继承与多态
'''
    判断是否为其子类
        issubclass(son, male)

    调用父类的方法
        def eat(self):
            super(Cat, self).eat()
            pass
'''

class zoo(object):
    '''
    动物
    '''
    tag = "动物园"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('动物都喜欢吃东西')


class cat(zoo):
    '''
    猫科动物
    '''
    tag = '猫科动物'

    def eat(self):
        #调用父类的方法
        super(cat, self).eat()
        print('猫喜欢吃鱼')


if __name__ == '__main__':
    zoo_cat = cat('小黑', 3)
    zoo_cat.eat()

    #判断是否为其子类
    result = issubclass(cat, zoo)
    print(result)


#编程练习
'''
任务
1、自定义Person类，并重写其构造（初始化）方法__init__( )，将name和gender参数赋值给实例对象的属性
2、自定义实例方法speak( )，功能：打印“hello ! 我是xxx”。relation( )方法主要是占位作用，无其他实质性功能
3、自定义Student类，继承自Person类，并重写其构造（初始化）方法__init__( )，name、gender参数通过调用父类的构造函数进行赋值，score和major通过子类重写的 __init__( )进行赋值。
4、自定义实例方法speak( )，功能：打印 '我的学号为xxxxxxxxxx，很高兴认识大家';
5、自定义实例方法identify_stu( )，功能：判断Student对象的学号。若学号为2018014002，则打印‘我的分组已经完成’，反之则打印‘请稍后，马上为你自动分组’；
6、自定义实例方法set_num( new_num)，功能：将学号重写设置为new_num；
7、自定义实例方法relation( )，功能：判断Student是否为Person的子类。若成立，则打印‘我的父类是Person’，反之则打印‘父类正在查询中······’
8、初始化实例对象stu和stu_2，并根据上述效果图调用对应方法
'''


class Person(object):
    tag = '基本信息'

    # 重写实例对象的构造（初始化）方法
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    # 自定义实例方法，格式化打印实例属性name的值
    def speak(self):
        print('hello ! 我是{}'.format(self.name))

    # 自定义实例方法，占位作用
    def relation(self):
        '''占位'''
        pass


class Student(Person):

    tag = '学生详细信息'

    # 重写实例对象的构造（初始化）方法，并调用父类构造方法，实现对实例属性的赋值
    def __init__(self, name, gender, score, major, stu_num=None):
        super(Student, self).__init__(name, gender)
        self.score = score
        self.major = major
        self.__stu_num = stu_num

    # 自定义实例方法，格式化打印实例属性stu_num的值
    def speak(self):
        super(Student, self).speak()
        print('我的学号为{}，很高兴认识大家'.format(self.__stu_num))

    # 自定义实例方法，判断学号是否为既定值，并根据判断结构 进行分类打印
    def identify_stu(self):
        '''功能：判断Student对象的学号。若学号为2018014002，则打印‘我的分组已经完成’，反之则打印‘请稍后，马上为你自动分组’；'''
        if self.__stu_num == 2018014002:
            print('我的分组已经完成')
        else:
            print('请稍后，马上为你自动分组')

    # 自定义实例方法，设置实例对象的学号为传入的值
    def set_sum(self, new_sum):
        '''功能：将学号重写设置为new_num；'''
        self.__stu_num = new_sum

    # 自定义实例方法，判断该类是否为Person类的子类，并进行分类打印
    def relation(self):
        if issubclass(Student, Person):
            print('我的父类是Person')
        else:
            print('父类正在查询中')


if __name__ == '__main__':
    stu = Student('小明', '男', 90, '数学', 2018014002)
    # 调用speak方法 打印stu对应的值
    stu.speak()
    # 调用实例方法 鉴别学号是否为指定值
    stu.identify_stu()
    # 调用实例方法 鉴别实例对象所属的类的父类是否为Person
    stu.relation()
    print("******************")
    stu_2 = Student('小红', '女', 89, '英语')
    # 调用实例方法 设置stu_2的学号为'2018040625'
    stu_2.set_sum(2018040625)
    # 调用实例方法 打印stu_2对应的值
    stu_2.speak()
    # 调用实例方法 鉴别学号是否为指定值
    stu_2.identify_stu()