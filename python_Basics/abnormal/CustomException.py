
#自定义异常

'''
    通过继承自Excepttion类来自定义异常
'''


class MyExcept(Exception):
    '''自定义异常'''
    code = '60000'
    msg = '未知错误'

    def __iter__(self, code, msg):
        self.code = self.code if self.code else code
        self.msg = self.msg if self.msg else msg

    def __str__(self):
        return 'Error: {0} - {1}'.format(self.code, self.msg)

class ApiExcept(MyExcept):
    '''参数错误'''
    code = '5000'
    msg = '参数错误'

class NumExcept(MyExcept):
    '''不能为零'''
    code = '50001'
    msg = '除数不能为零'

def test_div(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ApiExcept()       #使用raise触发异常
    if num2 == 0:
        raise NumExcept
    return num1 / num2

if __name__ == '__main__':
    try:
        result = test_div(5, 1)
        print(result)
        print('-' * 50)
        info = test_div(5, '2')
        print(info)
    except MyExcept as error:
        print(error)
    # except ApiExcept as err:
    #     print(err)
    # except NumExcept as e:
    #     print(e)


#抛出异常及异常的传递
'''
    如果在异常产生的地方不能捕获，那么它会一层一层的往上传递
'''


class TestRaise(Exception):
    '''自定义异常'''
    pass

def v_for():
    '''定义for循环'''
    for i in range(1,10):
        if i == 5:
            raise TestRaise
        print(i)

def class_v_for():
    '''调用v_for'''
    print('开始调用v_for')
    try:
        v_for()
    except TestRaise:
        print('这是测试，捕获异常')
    print('结束调用v_for')

def test_v_for():
    '''调用class_v_for'''
    print('程序执行')
    class_v_for()
    print('程序结束')


if __name__ == '__main__':
    test_v_for()