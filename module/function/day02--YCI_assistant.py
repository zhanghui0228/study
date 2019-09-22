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
phone_number = "匪警[110],急救中心[120],火警[119],通用紧急急救[112]"
werther_str = "北京,2019年9月22日,晴,27℃,15℃~杭州,2019年9月22日,多云,26℃,18℃"

def chromosphere():
    #双色球函数
    num = input("您要生成几注双色球号码：")
    print("=========================")
    for n in range(0,int(num)):
        for i in range(0,6):
            red = random.randint(1,33)
            print(red, end=" ")
        blue = random.randint(1,16)
        print(blue)
    print("=========================")
def find_Phone_Number():
    #号码百事通函数
    phone = input("请输入你要查询的机构或者电话号码：")
    phone_list = phone_number.split(",")
    for p in phone_list:
        if p.find(phone) != -1:
            print(p)
    print("=========================")
def werther():
    #天气预报函数
    city = input("请输入您要查询的城市：")
    werther_list = werther_str.split("~")
    weather_data = {}
    for i in range(0,len(werther_list)):
        w = werther_list[i].split(",")
        weather = {"name":w[0], "date":w[1], "weather":w[2], "max":w[3], "min":w[4]}
        weather_data[weather["name"]] = weather
    if city in weather_data:
        w = weather_data.get(city)
        print("{date} {name} {weather} {max}/{min}".format_map(w))
    else:
        print("未查找到{}城市天气信息！".format(city))
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
        find_Phone_Number()
    #执行天气预报模块
    elif entry == "3":
        werther()
    #执行退出程序
    elif entry == "0":
        print("感谢使用本次程序，祝您生活愉快！")
        break
    else:
        print("您选择的功能暂未支持，请重新输入！")
        print("=========================")
        continue
