#类的多重继承
'''
    多重继承：   一个类有多个父类
        如果调用的方法时重名的，调到第一个后，则后面的不进行调用
        继承关系可以顺序延续，后续子类可以继承前驱父类
'''

class zoo(object):
    '''动物园'''
    tag = 'zoo'
    def __init__(self, name):
        self.name = name

    def chara(self):
        print('我叫{}，我在动物园里'.format(self.name))

class Type(object):
    '''类别'''
    def type(self):
        print("我的类型是：")

class meat(Type):
    '''肉食动物'''
    tag = 'meat'
    def eat(self):
        print('我是肉食动物')

class grass(Type):
    '''素食动物'''
    tag = 'trass'
    def eat(self):
        print('我是素食动物')

class tiger(zoo, meat):
    '''老虎'''
    tag = 'tiger'
    # def info(self):
    #     super(tiger, self).chara()
    #     super(tiger, self).eat()

if __name__ == '__main__':
    result = tiger('霸王')
    # result.info()
    print('*************************')
    result.eat()
    result.chara()
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')

#编程练习一：
'''
任务
1、自定义Point类，并重写其构造（初始化）方法__init__( )，将参数x和y赋值给实例对象的属性
2、自定义该类实例方法string( )，功能：打印“{X：xx, Y：xx}”
3、自定义Circle类，继承自Point类，并重写其构造（初始化）方法__init__( )，x、y参数通过调用父类的构造函数进行赋值，radius通过子类重写的 __init__( )进行赋值。
4、自定义该类实例方法string( )，功能：打印“该图形初始化点为：{X：xx, Y：xx}; {半径为：xx}”
5、自定义Size类，并重写其构造（初始化）方法__init__( )，将参数width和height赋值给实例对象的属性
6、自定义该类实例方法string( )，功能：打印“{Width：xx, Height：xx}”
7、自定义Rectangle类，继承自Point类和Size类，并重写其构造（初始化）方法__init__( )，x、y、width、height 4个参数全部通过调用父类的构造函数进行赋值
8、自定义该类实例方法string( )，功能：打印“该图形初始化点为：{X：xx, Y：xx}; 长宽分别为：{Width：xx, Height：xx}
9、初始化Circle类的对象c，并调用其格式化输出函数string( )
10、初始化Rectangle类的对象r1、r2,并分别调用其格式化输出函数string( )
'''


class Point(object):

    # 自定义Point类的构造(初始化)方法
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 自定义Point类对象的格式化输出函数(string())
    def string(self):
        print('{'+'X：{0}, Y：{1}'.format(self.x,self.y)+'}')


class Circle(Point):

    # 自定义Circle类的构造(初始化)方法
    def __init__(self, x, y, radius):
        super(Circle, self).__init__(x, y)
        self.radius = radius

    # 自定义Circle类对象的格式化输出函数(string())
    def string(self):
        print('该图形初始化点为：{'+'X：{0}, Y：{1}'.format(self.x,self.y)+'}; {'+'半径为：{0}'.format(self.radius)+'}')


class Size(object):

    # 自定义Size类的构造(初始化)方法
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 自定义Size类对象的格式化输出函数(string())
    def string(self):
        print('{'+'Width：{0}, Height：{1}'.format(self.width,self.height)+'}')


class Rectangle(Point, Size):

    # 自定义Rectangle类的构造(初始化)方法，并在方法中调用父类的初始化方法以完成初始化
    def __init__(self, x, y, width, height):
        Point.__init__(self, x, y)
        Size.__init__(self, width, height)

    # 自定义Rectangle类对象的格式化输出函数(string())
    def string(self):
        '''功能：打印“该图形初始化点为：{X：xx, Y：xx}; 长宽分别为：{Width：xx, Height：xx}'''
        print('该图形初始化点为：{'+'X：{0}, Y：{1};'.format(self.x,self.y)+' 长宽分别为：{'+'Width：{0}, Height：{1}'.format(self.width,self.height)+'}')


if __name__ == "__main__":
    # 实例化Circle对象，圆心为（5,5），半径为8
    grap_1 = Circle(5, 5, 8)
    grap_1.string()
    # 实例化Rectangle对象，顶点位置（15,15），长和宽分别为15和15
    grap_2 = Rectangle(15, 15, 15, 15)
    grap_2.string()
    # 实例化Rectangle对象，顶点位置（40,30），长和宽分别为11和14
    grap_3 = Rectangle(40, 30, 11, 14)
    grap_3.string()


#编程练习二
'''
任务
1、自定义People类，并重写其构造（初始化）方法__init__( )，将参数n和a赋值给实例对象的属性
2、自定义该类实例方法speak( )，功能：打印“xxx说: 我xxx岁”
3、自定义Speaker类，并重写其构造（初始化）方法__init__( )，将参数n、c、t赋值给实例对象的属性
4、自定义该类实例方法speak( )，功能：打印“我叫xxx,我是一个xxx,我演讲的主题是 xxx”
5、实例化Student类对象s
6、调用父类的speak( )方法
7、根据效果图进行格式化输出
'''


class People(object):

    # 重写People类的构造方法，并将参数n、a赋值给实例属性name、age
    def __init__(self, n, a):
        self.name = n
        self.age = a

    # 自定义实例方法speak（），实现格式化输出
    def speak(self):
        print('{0}说: 我{1}岁'.format(self.name, self.age))


class Speaker(object):

    # 重写Speaker类的构造方法，并将参数n、c、t赋值给实例属性name、career、topic
    def __init__(self, n, c, t):
        self.name = n
        self.career = c
        self.topic = t
    # 自定义实例方法speak（），实现格式化输出
    def speak(self):
        print('我叫{0},我是一个{1},我演讲的主题是 {2}'.format(self.name, self.career, self.topic))


class Student(Speaker, People):
    pass


if __name__ == '__main__':
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    s = Student('Jonh', '演说家', 'Python')
    # s对象调用父类的speak( )方法
    s.speak()
    # 格式化打印Student是否为Speaker的子类
    if issubclass(Student, Speaker):
        print("Student是Speaker的子类")
    else:
        print("Student不是Speaker的子类")
    # 格式化打印Student是否为People的子类
    if issubclass(Student, People):
        print("Student是People的子类")
    else:
        print("Student不是People的子类")
