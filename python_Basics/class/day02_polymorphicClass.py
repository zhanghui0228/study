#面向对象的特性----多态
'''
    每当无需知道对象是什么样的就能对其执行操作时，都是多态其作用（同一个方法在不同的类中最终呈现出不同的结果）

    继承就时多态的体现
'''


class zoo(object):

    def __init__(self, name):
        self.name = name
        print('zoo init')

    def eat(self):
        print("我喜欢吃东西")


class tiger(zoo):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def eat(self):
        # super().eat()
        print("我喜欢吃肉")

    def show_info(self):
        print('{0}的年龄是{1}'.format(self.name,self.age))

if __name__ == '__main__':
    zoo_1 = tiger('武松', 4)
    zoo_1.show_info()
    zoo_1.eat()