#函数的三中使用技巧
"""
    设置参数默认值         添加默认值只需在需要设置默认值的形参上指定其具体值即可
    关键字传参              将实参书写出来，并对应其值即可，没有顺序一说
    混合形式传参              (形参1, *, 形参2,...)       *后面的参数必须以关键字的形式进行传参
"""
#设置默认值
def user(username, password=123456):
    if username == "admin":
        print("username:{},password:{}".format(username, password))
    else:
        return username
user("admin", 123123)
print (user("root"))

#关键字传参
def check(mem, cpu, disk, system):
    print("你的系统运行情况如下:","{", "mem:{mem},cpu:{cpu},disk:{disk},system:{system}".format(mem=mem,cpu=cpu,disk=disk,system=system),"}")

check(mem="ok",cpu="ok",disk="ok",system="ok")

#混合形式传参         ---使用*， 强制将其以关键字形式传参
def health_check(system, *, mem, cpu, disk):
    print("你的系统运行情况如下:", "{","system:{system},mem:{mem},cpu:{cpu},disk:{disk}".format(mem=mem, cpu=cpu, disk=disk, system=system), "}")
health_check("linux",mem="ok",cpu="ok",disk="falsh")

#编程练习
def info(*, desc,birth, name='imooc'):
    # 使用format格式化字符串向控制台输出——imooc-程序员的梦工厂出生于2013年8月
    print ("{name}-{desc}生于{birth}".format(name=name,desc=desc,birth=birth))

# 调用函数，向函数内传入（"程序员的梦工厂"，"2013年8月"）
info(desc="程序员的梦工厂", birth="2013年8月")


####函数的使用技巧二
'''
    序列传参；
    字典传参；
    返回值包含多个数据
'''
#序列传参
def calc(a, b, c):
    return (a + b) * c

l = [1, 10, 4]
print(calc(*l))

#字典传参
def health_check(system, *, mem, cpu, disk):
    print("你的系统运行情况如下:", "{","system:{system},mem:{mem},cpu:{cpu},disk:{disk}".format(mem=mem, cpu=cpu, disk=disk, system=system), "}")
param = {"system":"linux", "mem":"ok", "cpu":"ok", "disk":"ok"}
health_check(**param)

#返回值包含多个数据
def get_info():
    info_list = {
        "check_host" : [
            {"hostname":"host1", "mem":"4G"},
            {"hostname":"host2", "mem":"8G"}
        ],
        "check_vm" : [
            {"hostname":"vm01", "disk":"50G"},
            {"hostname":"vm02", "disk":"100G"}
        ]
    }
    return info_list
print(get_info())
#获取里面单条数据
d = get_info()
d_name = d.get("check_host")[0].get("hostname")
print(d_name)

#编程练习一
'''
    定义seq函数，向函数内传入形参(num, num1, num2)，如果num小于88，返回num1与num2的积，否则返回num1和num2的和，调用函数传参时使用元组传参
'''
def seq(num,num1,num2):
    # if判断num小于88
    if num < 88:
        #返回num1与num2的积
        return num1 * num2
    else:
        #返回num1与num2之和
        return num1 + num2
# 定义变量tuple1的值为(5,2,1)
tuple1 = (5, 2, 1)
# 调用函数，传入参数tuple1，并打印函数返回值
print(seq(*tuple1))

#编程练习二
'''
    定义函数fun_dict实现向控制台输出如效果图所示结果，传入函数的参数类型为字典类型，请运用所学知识完成该题目。
    任务
    1、使用format格式化字符串，使得向控制台输出结果——小葫芦隶属于技术部，电话:18795642135, 入职日期：2017-9-23
    2、创建字典dict1为{'name':'小葫芦','hiredate':'2017-9-23','tel':18795642135,'dept':'技术部'}
    3、使用字典dict1作为参数传入函数fun_dict
'''


def fun_dict(name, hiredate, tel, dept):
    # 使用format格式化字符串，使得向控制台输出结果——小葫芦隶属于技术部，电话:18795642135, 入职日期：2017-9-23,并向控制台输出结果
    print("{name}隶属于{dept},电话:{tel},入职日期:{hiredate}".format(name=name,hiredate=hiredate,tel=tel,dept=dept))

# 创建字典info_list为{'name':'小葫芦','hiredate':'2017-9-23','tel':18795642135,'dept':'技术部'}
info_list = {'name':'小葫芦','hiredate':'2017-9-23','tel':18795642135,'dept':'技术部'}
# 使用字典dict1作为参数传入函数fun_dict
fun_dict(**info_list)