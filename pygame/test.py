
def t(test):
    def me():
        print("{0} is start")
        test()
        print("{0} is stop")
    return me

@t
def ceshi():
    print("this is test")


def t2(app=ceshi):
    def ceshi(func):
        def hi(*args, **kwargs):
            print("{0} is start".format(app))
            result = func(*args, **kwargs)
            print("{0} is stop".format(app))
            return result
        return hi
    return ceshi

@t2('nginx')
def nginx():
    print("nginx is running...")


if __name__ == '__main__':
    ceshi()
    nginx()