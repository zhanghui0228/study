#散列值（Hash）与字典的存储原理（内存时如何存储数据的）
'''
    字典也称“哈希（hash）”,对应“散列值”；
    散列值是从任何一种数据中创建数字“指纹”
    python中提供了hash()函数生成散列值
'''
'''
#生成散列值
ha = hash("test.txt")
print(ha)
ha1 = hash("test.txt")
print(ha1)
'''
#字典在项目中的使用
source = "2323,zs,测试,3000$2324,ls,财务,3500$2325,ww,销售,4000"
emp_list = source.split("$")
#print(emp_list)
all_emp = {}
for i in range(0,len(emp_list)):
    e = emp_list[i].split(",")
    print(e)
    #创建员工字典
    emp_dict = {"nume":e[0], "name":e[1], "job":e[2], "salary":e[3]}
    #print(emp_dict)
    all_emp[emp_dict["nume"]] = emp_dict
#print(all_emp)
emp_input = input("请输入员工编号：")
if emp_input in all_emp:
    emp = all_emp.get(emp_input)
    print("工号：{nume}，姓名：{name}，部门：{job}，工资：{salary}".format_map(emp))
else:
    print("员工工号不正确")