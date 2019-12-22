#装饰器
'''
    装饰器     用与拓展原来函数功能的一种函数
               返回函数的函数
               在不用更改原函数的代码前提下给函数增加新的功能
        格式：
            def info(value):
                def warpper():
                    '主体内容'  #value在这里使用
                return warpper

'''
from functools import wraps


#不使用装饰器进行实现以下内容


def python():
    print('正在安装>>>>>>>')

def install_info(info):
    print('准备安装>>>>')
    info()
    print('安装完毕!')


if __name__ == '__main__':
    install_info(python)
    print('*' * 30)


#使用装饰器进行实现以上功能
def star_log(info):
    '''实现装饰器'''
    def warpper():
        print('start >>>>>>>>>')
        info()
        print('end >>>>>>>>')
    return warpper

@star_log   #使用装饰器
def nginx_warpper():
    print('hello nginx')

if __name__ == '__main__':
    nginx_warpper()
    print('*' * 30)


#带参数的装饰器

def log(name='app'):
    '''记录执行日志'''

    def decorator(func):
        def warpper(*args, **kwargs):   #魔法参数
            print('{0} start  >>>>'.format(name))
            resu = func(*args, **kwargs)
            print('{0} end >>>'.format(name))
            return resu
        return warpper
    return decorator


@log('apache')    #使用装饰器
def apache_install():
    print('this is apache')

@log('多参数')
def manay(a, b, *args, **kwargs):
    print(a + b, '{0}'.format(kwargs))

if __name__ == '__main__':
    apache_install()
    manay(2, 8, k='和')
    print('#' * 30)


#带参数装饰器之wraps       --装饰器完善版
def log2(name='app'):
    '''记录执行日志'''

    def decorator(func):
        @wraps(func)        #还原发生改变的函数的一些内置变量(属性和方法 )
        def warpper(*args, **kwargs):   #魔法参数
            print('{0} start  >>>>'.format(name))
            resu = func(*args, **kwargs)
            print('{0} end >>>'.format(name))
            return resu
        return warpper
    return decorator


@log2('check')    #使用装饰器
def check():
    """check good """
    print('this is check')

# @log2('多参数')
# def manay(a, b, *args, **kwargs):
#     print(a + b, '{0}'.format(kwargs))

if __name__ == '__main__':
    check()
    print('name: {0}'.format(check.__name__))
    print('doc: {0}'.format(check.__doc__))


################################################
'''类的装饰器'''

def eat(cls):
    '''吃东西装饰器'''
    cls.eat = lambda self: print('{0} 要吃东西'.format(self.name))
    cls.manay = lambda self: print('{0} 爱睡觉'.format(self.name))
    return cls

@eat
class Cat(object):
    '''猫'''
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    cat = Cat('花花')
    cat.eat()
    cat.manay()