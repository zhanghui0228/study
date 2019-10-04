"""
    这是自定义模块，模块名为test
"""
def func():
    print("this is module package test!")

def add(num1, num2):
    '''
    this is function test!
    '''
    print(num1 + num2)

if __name__ == '__main__':
    add(1, 3)
    print(add.__doc__)