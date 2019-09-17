#列表在项目中的使用      --多维列表（嵌套列表）
"""
    str.split("")   切割字符串转换成列表，指定切割符号
"""

#例子：    [[姓名，年龄，工资],[姓名，年龄，工资],[姓名，年龄，工资]]

str = "张三,30,3000"
l = str.split(",")  #切割字符串转换为列表，指定切割符合
print(l)

#练习示例
'''
emp_list = []
while True:
    info = input("请输入员工信息，格式：,年龄,工资 :")
    if info == "":
        print("输入信息不能为空，请重新输入！")
        continue
    elif info != 'exit' and info != 'ls':
        info_list = info.split(",")
        if len(info_list) != 3:
            print("输入的格式有问题，请重新输入！")
            continue
        emp_list.append(info_list)
    elif info == "ls" and info != 'exit':
        for emp in emp_list:
            print("姓名:{name},年龄:{age},工资:{salary}".format(name=emp[0],age=emp[1],salary=emp[2]))
    else:
        break
'''

#编程练习
'''
    要求：
        根据提示，在终端输入月份，并判断该月份属于春，夏，秋，冬中的哪一个季节。
    任务 
        1、定义变量reason为外层列表，里面嵌套列表[3, 4, 5]，列表[6, 7, 8]，列表[9, 10, 11]，列表[12, 1, 2]   
        2、定义month接收input函数
        3、使用if判断语句判断输入的月份为什么季节
'''
reason = [[3,4,5],[6,7,8],[9,10,11],[12,1,2]]
month = int(input("请输入月份："))
if month in reason[0]:
    print("{month}月份是春季".format(month=month))
elif month in reason[1]:
    print("{month}月份是夏季".format(month=month))
elif month in reason[2]:
    print("{month}月份是秋季".format(month=month))
elif month in reason[3]:
    print("{month}月份是冬季".format(month=month))
else:
    print("请输入正确的月份")
