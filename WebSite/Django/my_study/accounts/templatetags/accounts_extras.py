from django import template

# 引用template.Library库
register = template.Library()


# 处理变量的函数
def warning(value):
    ''' 将第一个字符变红 '''
    if value:
        return '<span class="text-red">' + value[0] + '</span>' + value[1:]
    return value


# 用逗号分隔数据
def account_sum(value, place=2):
    '''用逗号分隔数据'''
    try:
        place = int(place)
    except:
        place = 2

    try:
        from decimal import Decimal
        value = Decimal(value)
        import locale
        locale.setlocale(locale.LC_ALL, '')
        return locale.format("%.*f", (place, value), 1)
    except Exception as err:
        return value



# 注册过滤器
register.filter('warning', warning)
register.filter('account_sum', account_sum)