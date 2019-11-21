
import random, sys
from datetime import datetime


#自定义游戏进入提示函数
def guide_page(guide_word):
    '''功能描述： 提示玩家进入游戏，并输出提示信息'''
    print("************{0}************".format(guide_word))


#自定义数字类型判断函数
def all_num(n):
    '''功能描述：判断指定的值是否为数字'''
    #判断n是数字组成
    if n.isdigit():
        return True
    #n 不是数字
    else:
        print("你输入的是非数字，请重新启动")
        sys.exit()

#自定义数值合法性判定函数
def num_legal(ls):
    '''功能描述：判定指定序列中的数值是否相等以及记录数字区间起始位置的值是否大于记录数字区间终止位置的值'''
    #判断起始值和结束值相等
    if ls[0] == ls[1]:
        print("你输入的数字区间值相同，请重新启动程序")
        sys.exit()
    #起始值大于结束值
    elif ls[0] > ls[1]:
        print("你输入的起始值大于结束值，请重新启动程序")
        sys.exit()
    #正常情况
    else:
        return True


#自定义产生指定区间随机数函数
def set_final_num(num1,num2):
    '''功能描述：根据参数值，产生一个位于参数值区间以内的随机数'''
    ls = [num1, num2]
    ls = list(filter(all_num, ls))
    if len(ls) == 2:
        l = num_legal(ls)
        if l:
            print('所产生的随机数区间为: {0}'.format(ls))
        return random.randrange(int(num1), int(num2))
    else:
        print("你输入的是非数字字符，请重新启动")
        sys.exit()


#自定义核查数值是否属于指定区间函数
def check_num_legal(num):
    '''功能描述：判定所输入的数值是否在指定的区间'''
    if num < int(i) or num > int(j):
        return False



#自定义日志写入函数
def write_record(times,value):
    '''功能描述：将玩家每一次猜测数字和本次猜测次数两项信息写入日志文件'''
    log_file = "record.txt"
    date_time = datetime.now()
    with open(log_file, "a", encoding="utf8") as f:
        f.write("{0}: 第{1}次你猜的数字为：{2}".format(date_time, times, value))
        f.write("\n")

#自定义main(rand1)函数
def main(rand1):
    '''功能描述：依据所产生的随机数字(rand1)，提示玩家输入猜测数字并进行比对直到猜测到正确数字'''
    '''
    1）设置变量temp接收已产生的随机数字，记录猜测数字的次数（默认为0） 
     （2）设置无限循环：                             
                1.提示用户输入所猜测数字，并转换为int类型 
                2.if判断核查数值函数，如果为真，则输出对不起您输入的数字未在指定区间！！！，跳过本次循环
                3.实现用户输入一次猜测数字，次数+1
                4.调用日志写入函数，传入猜测的次数和用户猜测的数字
                5.使用if语句判断用户猜测的数字，相等，大于，小于的情况，并输出如效果图所示的提示信息
    '''
    times = 0
    while True:
        value = input("请输入您猜测的数字：")
        all_num(value)
        value = int(value)
        times += 1
        if check_num_legal(value):
            print("你所输入的数字不在指定的区间范围内")
        elif value == rand1:
            print("恭喜你！只用了{0}次就赢得了游戏".format(times))
            write_record(times, value)
            break
        elif value < rand1:
            print("*" * 24)
            print("Lower tha the answer")
        elif value > rand1:
            print("*" * 24)
            print("Higher than the answer")
        write_record(times, value)

#控制程序逻辑执行流程
if __name__ == '__main__':
    # 定义标题
    guide_word = '欢迎进入数字猜猜猜小游戏'
    guide_page(guide_word)
    i = input("请输入数字区间起始值：")
    j = input("请输入数字区间结束值：")
    rand1 = set_final_num(i, j)
    main(rand1)

