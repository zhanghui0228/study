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


#带参数的装饰器
