#类的高级特性之--  __slots__
'''
    __slots__   :   为指定的类设置一个静态属性列表
                    为属性很少的类节约内存空间
'''

class Info(object):

    tag = 'info'
    __slots__ = ('__name', 'num')
    def __init__(self, name, num):
        self.__name = name
        self.num = num

    @property
    def name(self):
        return self.__name

    def get_info(self):
        info = '部门：{0}，联系方式：{1}'.format(self.__name, self.num)
        return info

class pocli_info(Info):
    #__slots__ = ('posotion', )
    pass

def posotion():
    return '地址为BJ'

if __name__ == '__main__':
    source_info = Info('急救中心', 120)
    result = source_info.get_info()
    print(result)
    # #给实例添加新的属性
    # source_info.posotion = 'BJ'
    # print(source_info.posotion)
    # #给实例添加新的方法
    # source_info.posotion = posotion()
    # print(source_info.posotion)

    # # 使用__slots__后不允许给实例添加新的属性
    # source_info.posotion = 'BJ'
    # print(source_info.posotion)
    # # 使用__slots__后不允许给实例添加新的方法
    # source_info.posotion = posotion()
    # print(source_info.posotion)

    '''
        使用子类继承父类的方法，查看__slots__ 的属性列表 是否继承成功
            结果表明：
                1、子类不会继承父类的__slots__的限制其属性列表
                2、可以在子类中添加__slots__进行限制其属性列表
    '''
    pocli = pocli_info('警察局', 110)
    pocli_result = pocli.get_info()
    print(pocli_result)
    #给子类添加新的属性
    pocli.posotion = 'SH'
    print(pocli.posotion)
    print('*' * 30)


# *******************************************************************************************************************

'''
    类的静态方法和实例方法
        @staticmethod   表示静态方法      无需实例化
        @classmethod    表达类的方法
        
'''

#调用staticmethod 的方法
class Test(object):

    #使用 @staticmethod
    @staticmethod
    def breath():
        print('人都要呼吸')

if __name__ == '__main__':
    #通过类进行调用
    Test.breath()
    #通过实例进行调用
    info = Test()
    info.breath()
    print('*' * 30)

#调用classmethod的方法
class Ceshi(object):

    tag = '类的tag'
    def __init__(self, name):
        self.name = name

    @classmethod
    def show_info(cls, name):
        '''实例的属性'''
        return cls(name)

    def get_info(self):
        print('类的属性：{}，实例的属性：{}'.format(self.tag, self.name))

if __name__ == '__main__':
    result = Ceshi.show_info('测试')
    result.get_info()
    print('#' * 50)

#编程练习
'''
任务
    1、自定义Car类，并重写其构造（初始化）方法__init__( )，将参数l，w，h，brand赋值给实例对象的属性L，W，H，brand。设置类属性description，以列表形式初始化值为：'大众'，'丰田'，'广本'，'沃尔沃'， '凯迪拉克'
    2、自定义该类实例方法modify_des ( )。功能：判断类属性description是否存在，若存在，直接返回；反之，返回“请输入您的车辆描述”
    3、自定义静态方法basic_parameters( )。功能：打印‘已完成车辆基本参数信息的录入！’
    4、自定义类方法upkeep( )，并接收参数desc。功能：判断参数desc是否在类属性description之中，若条件成立则打印“根据汽车保养的相关经验，xx品牌的车应于5000km/次的频率进行专业性保养”；反之则打印“非常抱歉！xx品牌不在我们的保养范围内”
    5、实例化Car类对象car_1，并调用实例方法basic_parameters()
    6、运用if-else结构，调用实例（car_1）方法modify_des( )作为if语句的判断条件，若成立则调用实例的upkeep( )方法，并将实例car_1的brand属性传递给参数desc；反之则打印：'请正确填写相关的车辆信息'
    7、实例化Car类对象car_2，并调用实例方法basic_parameters()
    8、运用if-else结构，调用实例（car_2）方法modify_des( )作为if语句的判断条件，若成立则调用实例的upkeep( )方法，并将实例car_2的brand属性传递给参数desc；反之则打印：'请正确填写相关的车辆信息'
'''


class Car(object):

    description = ('大众', '丰田', '广本', '沃尔沃', '凯迪拉克')
    # Car类的基本车型设置，列表形式
    __slots__ = ('l', 'w', 'h', 'brand')
    # 重写该类的构造方法，并将参数l、w、h、brand赋值给实例对象属性
    def __init__(self, l, w, h, brand):
        self.l = l
        self.w = w
        self.h = h
        self.brand = brand

    # 自定义该类的基本车型检索方法
    def modify_des(self):
        '''功能：判断类属性description是否存在，若存在，直接返回；反之，返回“请输入您的车辆描述”'''
        if self.brand in self.description:
            return self.brand
        else:
            return '请输入您的车辆描述'

    # 自定义静态方法 提示用户：‘已完成车辆基本参数信息的录入！’
    @staticmethod
    def basic_parameters():
        ''' 功能：打印 已完成车辆基本参数信息的录入！ '''
        print('已完成车辆基本参数信息的录入！')

    # 自定义类方法 根据用户车辆的品牌给出相应的合理保养建议
    def upkeep(self, desc):
        '''功能：判断参数desc是否在类属性description之中，若条件成立则打印“根据汽车保养的相关经验，xx品牌的车应于5000km/次的频率进行专业性保养”；反之则打印“非常抱歉！xx品牌不在我们的保养范围内”'''
        if desc in self.description:
            print('根据汽车保养的相关经验，{0}品牌的车应于5000km/次的频率进行专业性保养'.format(desc))
        else:
            print('非常抱歉！{0}品牌不在我们的保养范围内'.format(desc))

if __name__ == '__main__':
    car_1 = Car(4.2, 1.8, 1.5, '大众')
    # 调用实例方法：basic_parameters（）
    car_1.basic_parameters()
    # 利用if语句，调用modify_des()以判断Car的类属性description是否存在
    if car_1.modify_des() in car_1.description:
        #若if判断条件成立 则调用类方法upkeep（）并将对应实例的brand属性传递给参数desc
        car_1.upkeep('大众')
    # 当if语句的判断条件不成立时，打印输出并提示用户：‘请正确填写相关的车辆信息’
    else:
        car_1.upkeep('大众')

    car_2 = Car(4.2, 1.8, 1.5, '保时捷')
    # 调用实例方法：basic_parameters（）
    car_2.basic_parameters()
    # 利用if语句，调用modify_des()以判断Car的类属性description是否存在
    if car_2.modify_des() in car_2.description:
        # 若if判断条件成立，则调用类方法upkeep（）并将对应实例的brand属性传递给参数desc
        car_2.upkeep('保时捷')
    # 当if语句的判断条件不成立时，打印输出并提示用户：‘请正确填写相关的车辆信息’
    else:
        car_2.upkeep('保时捷')
