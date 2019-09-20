#货币转换服务系统项目
#定义
service_menu = {1:"人民币转换美元", 2:"美元转换人民币", 3:"人民币转换欧元", 0:"结束程序"}
while True:
    print("*****************欢迎使用货币转换服务系统*****************")
    for key,value in service_menu.items():
        print(key,".",value)
    demand = input("请您选择需要的服务：")
    if demand == "1":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("欢迎使用人民币转换美元服务")
        money = int(input("请输入您要转换的人民币金额："))
        print("您需要转换的人民币金额为:{money}".format(money=money))
        print("兑换成美元为:{:0,.2f}$".format(money * 0.7))
    elif demand == "2":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("欢迎使用美元转换人民币服务")
        money = int(input("请输入您要转换的美元金额："))
        print("您需要转换的美元金额为:{money}".format(money=money))
        print("兑换成人民币为:{:0,.2f}$".format(money * 7))
    elif demand == "3":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("欢迎使用人民币转换欧元服务")
        money = int(input("请输入您要转换的人民币金额："))
        print("您需要转换的人民币金额为:{money}".format(money=money))
        print("兑换成欧元为:{:0,.2f}$".format(money * 0.78))
    elif demand == "0":
        print("感谢您的使用，祝您生活愉快，再见！")
        exit(0)
    else:
        print("输入的服务有误，请重新输入正确的服务，谢谢！")
        continue