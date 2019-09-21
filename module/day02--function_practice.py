#函数综合训练
#assistant  --助理；助手
#python中生成随机数
#通过random产生随机数
'''
import random
r = random.randint(1,33)
print(r)
'''
#小程序  ---YCI生活小助理
'''
    程序功能：
        1、双色球随机选号
            包含7个数字： 6个红色数字（取值规则1~33随机数），1个蓝色数字（取值规则1~16随机数）
            使用random产生随机数字
        2、号码百事通
        3、明日天气预报
'''
import random
def chromosphere():
    print("=========================")
def number():
    print("=========================")
def werther():
    print("=========================")
while True:
    print("1、双色球随机选号\n"
          "2、号码百事通\n"
          "3、明日天气预报\n"
          "0、退出程序")
    entry = input("请选择功能：")
    #执行双色球随机选号模块
    if entry == "1":
        chromosphere()
    #执行号码百事通模块
    elif entry == "2":
        number()
    #执行天气预报模块
    elif entry == "3":
        werther()
    #执行退出程序
    elif entry == "0":
        print("感谢使用本次程序，祝您生活愉快！")
        exit(0)
    else:
        print("您选择的功能暂未支持，请重新输入！")
        print("=========================")
        continue
