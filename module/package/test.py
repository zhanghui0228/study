"""
    这是自定义模块，模块名为test
"""
def func():
    print("this is module package test.txt!")

def add(num1, num2):
    '''
    this is function test.txt!
    '''
    print(num1 + num2)

if __name__ == '__main__':
    add(1, 3)
    print(add.__doc__)