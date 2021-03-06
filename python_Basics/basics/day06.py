#运算符    operator
'''
    算术运算符：也叫基本运算符，是指python中使用的基本数学计算符号
    比较运算符：对两个数值进行比较
    逻辑运算符：指在多个条件组合判断时使用的运算符，    其优先级 not>and>or
    赋值运算符： 包含了加法赋值运算符（i += 1）、减法赋值运算符、乘法赋值运算符、除法赋值运算符（浮点数除法-- "/"、取整除法--"//"、取余除法--"%"）、幂赋值运算符
    成员运算符：判断某个数字在数组里是否存在，使用的关键字  in(找到值返回true，否则返回false) 、not in（找不到值返回true,否则返回false）
    身份运算符：使用的关键字： is(判断两个变量是否引用自一个对象) 、is not(判断两个变量是不是引用自不同对象)
    位运算符
'''
'''
#成员运算符案例：
sheet = ["张三", "李四", "王五"]
if ('张三' in sheet):
    print("张三存在")
else:
    print("张三不存在")

#身份运算符案例
a = 5
b = a
c = 5.0
print(a is b)
print(a is not c)
print(b is c)

#编程练习
# 根据任务，按步骤实现最终的运行结果
str1 = 2020
str2 = "2020"
print (str1 == str2)
print (str1 is str2)
'''

#位运算符
'''
    0 代表 False , 1代表 True
    &   按位与运算符  --与
    |   按位与运算符  --或
    ^   按位异或运算符 --异或
    ~   按位取反运算符 --取反
    <<  左移动运算符  --左移
    >>  右移动运算符  --右移
    二进制进位规则： 逢二进一， 借位规则为：  借二当一
    
    
    二进制转十进制规则： 从右往左用每位数乘以2的N次方（从0开始）后累加
    十进制转二进制规则： 用十进制对2取余，将余数放在二进制左侧（数字的结果一直对2取余，直到除完为止），书写方式：倒位书写（最后一个取余结果写在第一位（最左侧），以此类推）
    
'''
#位运算符使用案例
a = 60  #二进制：00111100
b = 13  #二进制：00001101
c = 0
#&示例
c = a & b   #二进制：00001100
print("a & b:", c)
#|示例
c = a | b   #二进制：00111101   十进制：61
print("a | b:", c)
#^示例
c = a ^ b   #二进制：00110001   十进制：49
print("c ^ b:", c)
#~示例
#取反要求：如果最左侧的数值为1，则代表此数字是一个负数，需要进行再次取反加一
            #如果最左侧的数值为0，则带表此数字是一个正数
c = ~a  #二进制：-（~11000011+1）= -00111100+1 = -00111101   十进制：-61
print("~a:", c)
#<<示例
c = a << 3   #二进制：00111100000   十进制：480
print("a << 3:", c)
#>>示例
c = a >> 3  #二进制：00000111   十进制：7
print("a >> 3:", c)