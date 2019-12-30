#re模块
'''
    re模块
    findall()的使用
    search()的使用
    group()和groups()的使用
    split()正则分割
    Sub()正则替换
'''
"""
    re模块：
        re.I    re.IGNORECASE   不区分大小写的匹配
        re.L    re.LOCALE       根据所使用的本地语言通过\w、\W、\b、\B、\s、\S实现匹配
        re.M    re.MULTILINE    ^和$分别匹配目标字符串中的起始和结尾，而不是严格匹配整个字符串本身的起始和结尾
        re.S    rer.DOTALL      "."（点号）通常匹配除了\n（换行符）之外的所有单个字符；该标记表示"."（点号）能够匹配全部字符
        re.X    re.VERBOSE      通过反斜线转义，否则所有空格加上#（以及在该行中所有后续文字）都被忽略，除非在一个字符类中或者允许注释并且提高可读性
        


    #re模块   ----compile #推荐编译，但不是必须的
    
        书写形式：
            compile(pattern, flags = 0)             pattern ：正则表达式
        使用任何可选的标记来编译正则表达式的模式，然后返回一个正则表达式对象
        
    re模块    ----match
        书写形式：
            match(pattern, string, flags = 0)
        尝试使用带有可选的标记的正则表达式的模式来匹配字符串。如果匹配成功，就返回匹配对象；如果失败，就返回None
"""