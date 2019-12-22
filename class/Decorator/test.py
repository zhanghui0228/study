#装饰器测试使用

from functools import wraps


def log(name='app'):
    '''记录日志'''

    def functlog(func):
        @wraps(func)
        def warpper(*args, **kwargs):
            print('----{0} start ----'.format(name))
            result = func(*args, **kwargs)
            print('----{0} end ----'.format(name))
            return result

        return warpper

    return functlog


@log('nginx')
def nginxInstall(time):
    print('{0}: hello nginx!'.format(time))

if __name__ == '__main__':
    nginxInstall('2019')