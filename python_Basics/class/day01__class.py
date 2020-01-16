#类及类的定义
'''
    面向对象的基础；
    一种类型
    类的实例称之为对象
    一种用户自定义的类型
   类里面有很多自定义的属性和方法
'''

#类的属性和方法
"""
    类的特殊方法----构造函数
    class cat(object):
        def __init__(self, name, *args, **kwargs):      #self 表示的是类中对象的引用
            self.name = name
            pass
            
    类的特殊方法----析构函数(一般不使用)
    def __del__(self):
        pass
        
    类的特殊方法----其它函数
        __doc__   :文档信息
        __module__  :模块信息
        tag     :自定义的类属性
        catch   :自定义的类方法
        __bases__   :查看继承关系


class cat(object):
    '''
    猫科动物
    '''
    #类的属性
    tag = 'cat bases'
    def __init__(self, name, age):
        #实例化后的属性
        self.name = name
        self.__age = age    #设置为私有
        return name

    def eat(self):
        '''
        吃
        :return:
        '''
        pass

class tiger(cat):
    '''
    继承上面类
    '''
    pass
"""
#类的实现


class cat(object):

    tag = "猫科动物"
    def __init__(self, name, age):
        self.name = name
        self.__age = age    #设置为私有

    def set_age(self, age):
        '''
        改变猫的年龄
        :param age: int
        :return:
        '''
        self.__age = age
        return self.__age

    def show_info(self):
        '''
        显示猫的信息
        :return:
        '''
        result = "我叫{name},今年{age}岁".format(name=self.name, age=self.__age)
        print(result)
        return result

    def eat(self):
        '''
        猫喜欢吃的东西
        :return:
        '''
        print('I like eat fish')

    def catch(self):
        '''
        猫的行为
        :return:
        '''
        print('猫喜欢捉老鼠')

#引用类（实例化）
cat_black = cat('喵喵', 2)
cat_black.show_info()
cat_black.eat()
cat_black.catch()
print("-------------------")
#更改名字
cat_black.name = '花花'
cat_black.__age = 1 #无法更改，因为其类中age设置为了私有变量
#更改年龄
cat_black.set_age(1)
cat_black.show_info()
print("-------------------")
#获取名字
name = cat_black.name
print(name)


#类的实例判断----(判断实例是否类的实例)
result = isinstance(cat_black ,cat)
print(result)

#编程练习
'''
任务
1、自定义一个交通工具类(Vehicle)
2、设置类属性trans_type（固定值为'SUV'）和实例属性速度speed（int 类型，单位为 km/h）、体积size（tuple类型，单位为米。）
3、自定义方法 show_info( )，打印实例的所属类型和速度、体积的值；
4、自定义实例方法如下：
    （1）定义move( )方法，实现打印“我已向前移动了50米”
    （2）定义set_speed(new_speed)方法，设置对应实例的速度为new_speed km/h
    （3）定义get_speed()方法，如果（2）中设置了速度值则打印出来，打印格式为'我的时速为：设置的速度值 km/h'
    （4）定义speed_up()方法，设置每次调用时实例的速度都增加10km/h，并打印“我的速度由xx km/提升到了xx km/h”
    （5）定义speed_down()方法，设置每次调用时实例的速度都降低15km/h，并打印“我的速度由xx km/下降到了xx km/h”
5、自定义方法 transport_identify( )，判断实例是否为Vehicle类型。若是则打印‘类型匹配’，反之则打印‘类型不匹配’
6、初始化实例对象tool_1，并根据上述效果图调用对应方法
'''


class Vehicle(object):

    # 自定义Vehicle类属性
    tag = '交通工具'
    # 自定义实例的初始化方法
    def __init__(self, speed, size, trans_type='SUV'):
        self.speed = speed
        self.size = size
        self.__trans_type = trans_type

    # 自定义实例方法show_info，打印实例的速度和体积
    def show_info(self):
        print("我的所属类型为：{0}，速度：{1}，体积：{2}".format(self.__trans_type, self.speed, self.size))
    # 自定义实例方法move,打印“我已向前移动了50米”
    def move(self):
        print("我已向前移动了50米")
    # 自定义实例方法set_speed，设置对应的速度值
    def set_speed(self, speed):
        self.speed = speed
    # 自定义实例方法get_speed，打印当前的速度值
    def get_speed(self):
        print("当前速度为：{} km/h".format(self.speed))
    # 自定义实例方法speed_up，实现对实例的加速
    def speed_up(self):
        source_speed = self.speed
        new_speed = self.speed + 10
        print('我的速度由{source}km/h 提升到了{dest} km/h'.format(source=source_speed, dest=new_speed))
        self.speed = new_speed
    # 自定义实例方法speed_down，实现对实例的减速
    def speed_donw(self):
        source_speed = self.speed
        new_speed = self.speed - 15
        print('我的速度由{source} km/h 下降到了{dest} km/h'.format(source=source_speed, dest=new_speed))
        self.speed = new_speed
    # 自定义实例方法transport_identify，实现对实例所属类型的判断
    def transport_identify(self):
        if Vehicle.transport_identify:
            print('类型匹配')
        else:
            print('类型不匹配')

if __name__ == "__main__":
    tool_1 = Vehicle(20, (3.6, 1.9, 1.75))
    print('*********************************************************')
    # 调用实例方法 打印实例的速度和体积
    tool_1.show_info()
    # 调用实例方法 实现实例的前移
    tool_1.move()
    tool_1.set_speed(40)
    # 调用实例方法 打印当前速度
    tool_1.get_speed()
    # 调用实例方法 对实例进行加速
    tool_1.speed_up()
    # 调用实例方法 对实例进行减速
    tool_1.speed_donw()
    # 调用实例方法 判断当前实例的类型
    tool_1.transport_identify()