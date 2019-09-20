'''
#编程练习一：
i = 1
sum = 0
while i <= 8:
    sum = sum + i
    i = i + 1
print(sum)
'''
#退出语句
#continue #用于跳过当前循环的剩余语句
#break #关键字用来终止循环语句
#打印范围内能被8整除的数字
'''
start = 110
end = 190
i = start - 1
while i <= end:
    i = i + 1
    if i % 7 != 0:
        continue
    print(i)
'''

'''
#编程练习二
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
    if is_prime == True:
        print("{num}是质数".format(num=num))
    j = j + 1
'''
