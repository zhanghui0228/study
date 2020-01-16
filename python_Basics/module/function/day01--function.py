#函数
'''
    函数(function)是实现具有特定功能的代码
    特点：
        隐藏实现功能的细节；
        重用代码；
        提供代码的可读性，便于调试
    定义函数：
    def 函数名(形参1,形参2,...):
        要运行的代码（函数体）
        return 输出的数据（返回值）

    参数是函数的输入数据，而返回值是函数的输出结果
    return 不是必须的，但是return语句执行后，函数将中断执行

#编程练习
def goose():
    # 向控制台输出唐诗《咏鹅》诗句
    print("鹅，鹅，鹅，曲项向天歌。白毛浮绿水，红掌拨清波。")

    # 向控制台输出50个*号分隔符
    print("*" * 50)

# 调用函数实现效果
goose()
goose()
goose()
'''

#函数的形参与实参
'''
    参数就是函数的输入数据，在程序运行时根据参数不同执行不同代码  
    形参用于约束，实参用于传值
'''
def goose(verse_name, is_show_tatle):      #形参
    if is_show_tatle == True:
        print("*" * 50)
        print(verse_name)
    if verse_name == "悯农":
        print("鹅，鹅，鹅，曲项向天歌。白毛浮绿水，红掌拨清波。")
        print("*" * 50)
    elif verse_name == "静夜思":
        print("床前明月光，疑是地上霜。举头望明月，低头思故乡。")
        print("*" * 50)
goose("静夜思", is_show_tatle=True)    #实参

#编程练习
def oper(num, num1, num2):

    # if条件判断num小于100的情况
    if num < 100:
        # 对num1和num2进行乘法运算，并输出结果
        print(num1 * num2)
    else:
        #对num1和num2进行加法运算，并输出结果
        print(num1 + num2)

#调用函数，向函数内传入1314, 52, 0和5, 2, 0两组数据测试结果
oper(1314, 52, 0)
oper(5, 2, 0)


#####函数的返回值

def calc(amt, source, target):
    if source == "CNY" and target == "USD":
        result = amt / 6.7516
        return result
r = calc(100,"CNY", "USD")
print(r)

#编程练习
def login(username,password):
    # 使用if语句，判断用户名和密码为“imooc”和“123456”
    if username == "imooc" and password == "123456":
        #返回登录成功
        return "登陆成功"
    # 使用else子句处理用户名和密码非“imooc”和“123456”的情况
    else:
        #返回请重新登录
        return "请重新登陆"
# 调用函数，向函数内传入'imooc','123456'和'mooc','123456'两组数据测试结果
user = login("imooc", "123456")
user1 = login("admin", "123456")
# 打印函数测试结果
print(user)
print(user1)

