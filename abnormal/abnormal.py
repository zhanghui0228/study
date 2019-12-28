#abnormal   异常处理

'''
    内置的异常类：
        exception  几乎所有的异常类都是从它派生而来的
        AttributeError  引用属性或给它赋值失败时引发
        OSError     操作系统不能执行指定的任务（如打开文件）时引发，有多个子类
        IndexError      使用序列中不存在的索引时引发，为LookupError的子类
        KeyError    使用映射中不存在的键时引发，为LookupError的子类
        NameError       找不到名称（变量）时引发
        SyntaxError     代码不正确时引发
        TypeError       将内置操作或者函数用于类型不正确的对象时引发
        ValueError      将内置操作或者函数用于这样的对象时引发：其类型正确但包含的值不合适
        ZeroDIvisionError   在除法或求模运算的第二个参数为零时引发

    捕获异常：
        使用try...except 捕获所有的异常

        使用try...except...finally 处理必不可少的逻辑
'''

def test_div(num1, num2):
    try:
        resutl = num1 / num2
        print( resutl)
    # except TypeError:
    #     print("除数要为数字")
    # except ZeroDivisionError:
    #     print("除数不能为0")
    except (TypeError, ZeroDivisionError) as error:
        print("错误信息：{0}".format(error))


def test_finally():
    try:
        with open("test.txt", 'r', encoding='UTf8') as f:
            info = f.read()
            print(info)
    except:
        print("程序异常")
    finally:
        try:
            print("程序已退出")
        except:
            pass

if __name__ == '__main__':
    test_div(5, 0)
    test_div(6, '2')
    test_div(6, 2)
    print('*' * 30)
    test_finally()


