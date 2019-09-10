'''
#编程练习
n = 0
x = 0
y = "*"
while n < 4:
    while x < 4:
        print(" " * (4 - x - 1) + (y * (x * 2 + 1)))
        x = x + 1
    n = n + 1
'''

'''    1、判断某个数字是否是质数；
        2、判断多个数字是否是质数
num = int(input("请输入任意一个数字："))
i = 2
is_prime = True     #标识当前数字是否为质数 True是  False不是
while i < num:
    if num % i == 0:
        is_prime = False
        break
    i = i + 1
if is_prime == False:
    print("{num}不是质数".format(num=num))
else:
    print("{num}是质数".format(num=num))
'''

'''
    打印1000以内的质数
'''
j = 2
while j <= 1000:
    num = j
    i = 2
    is_prime = True  # 标识当前数字是否为质数 True是  False不是
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i = i + 1
    if is_prime == False:
        print("{num}不是质数".format(num=num))
    else:
        print("{num}是质数".format(num=num))
    j = j + 1
