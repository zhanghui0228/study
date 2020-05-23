from datetime import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import transaction, connection
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from weibo.models import WeiboUser as User, Comment, WeiBo


# Create your views here.

def page_user(request, page):
    '''对用户进行分页处理'''
    page_size = 2  # 每页展示2条数据
    user_list = User.objects.all()  # 要分页的数据结果集
    # 分页器对象 p
    p = Paginator(user_list, page_size)
    print('总记录数:{}'.format(p.count))
    print('总页数:{}'.format(p.num_pages))
    print('页码范围:{}'.format(p.page_range))
    # 获取某一页数据
    try:
        page_data = p.page(page)
        print('数据列表:', page_data.object_list)
        print('当前页数：', page_data.number)
        print('是否有上一页:', page_data.has_previous())
        print('是否有下一页:', page_data.has_next())
    except PageNotAnInteger as e:
        print("页码错误")
    except EmptyPage as e:
        print("没有数据了")
    return HttpResponse('ok')


# ORM查询条件练习
def search(request):
    ''' ORM查询条件练习 '''
    # user2_list = User.objects.filter(username='user2')  # exact 等于**值
    # print(user2_list)

    # # 用户名称包含（区分大小写）
    # user_list = User.objects.filter(username__contains='user')   # contains 包含**字符,区分大小写
    # print(user_list)

    # # 用户名称包含（不区分大小写）
    # user = User.objects.filter(username__icontains='u')     # icontains 包含**字符，不区分大小写
    # print(user)

    # # 查询z开头用户
    # zero_list = User.objects.filter(nickname__startswith='z')   # startswith    以**开头
    # print(zero_list)

    # # 查询以1结尾的用户
    # end_list = User.objects.filter(nickname__endswith='1')      # endswith      以**结尾
    # print(end_list)

    # # 查询在**选项（列表）   --in的使用
    # in_list = User.objects.filter(status__in=('2'))   # in    查询在**选项（列表）之内的
    # print(in_list)

    # 查询用户状态大于0的结果
    # user_list = User.objects.filter(status__gt=0)   # gt 大于/gte大于等于
    # print(user_list)

    # 查询是否为空值 isnull
    # user_list = User.objects.filter(creaete_time__isnull=True)  # 为空值 NULL
    # print(user_list.count())

    # # 查询是空字符串
    # str_list = User.objects.filter(nickname__exact='')    # 为空字符串
    # print(str_list.count())

    # # 根据时间进行查询
    # user_list = User.objects.filter(creaete_time__date='2020-04-16')
    # print(user_list)

    # # 查询4月15后之后的
    # date = datetime(2020,4,15)
    # date_list = User.objects.filter(creaete_time__gt=date)
    # print(date_list.count())

    # 第一中方法 使用user=用户对象
    # 查询张三的微博评论
    user = User.objects.get(username='zhangsan')
    comment_list = Comment.objects.filter(user=user)
    for item in comment_list:
        print(item.context)

    # 查询张三的微博内容
    weibo_list = WeiBo.objects.filter(user=user)
    for item in weibo_list:
        print(item.context)
    # 第二中方法 使用user__username='zs
    user1_weibo = WeiBo.objects.filter(user__username='user1')
    for item in user1_weibo:
        print(item.context)
    return HttpResponse('ok')

# 事务练习
@transaction.atomic()    # 引用事务
def trans(request):
    """
    事务练习
    用户发布微博的时候，顺便发布一条评论，只能同时成功，不能失败
    """
    user = User.objects.get(username='zhangsan')
    # 发布微博
    weibo = WeiBo.objects.create(user=user, context='trans test 1')
    # 发布评论
    comment = Comment.objects.create(user=user, context='trans comment 1', weibo=weibo)
    return HttpResponse('ok')


# 使用with使用事务，只准用户提交成功
def trans_with(request):
    """
    事务练习
    用户发布微博的时候，顺便发布一条评论，只能同时成功，不能失败
    使用with进行实现
    """
    with transaction.atomic():
        user = User.objects.get(username='zhangsan')
        # 发布微博
        weibo = WeiBo.objects.create(user=user, context='trans test with')
        # 发布评论
        comment = Comment.objects.create(user=user, context='trans comment with', weibo=weibo)
    return HttpResponse('ok')


# 手动控制事务
def trans_hand(request):
    """
    手动控制事务
    用户发布微博的时候，顺便发布一条评论，只能同时成功，不能失败
    """
    try:
        # 放弃自动提交
        transaction.set_autocommit(False)
        user = User.objects.get(username='user1')
        # 发布微博
        weibo = WeiBo.objects.create(user=user, context='trans test hand')
        # 发布评论
        comment = Comment.objects.create(user=user, context='trans comment hand', weibo=weibo)
        # 手动提交事务
        transaction.commit()
    except:
        # 不使用事务， 失败则手动删除数据
        # weibo.delete()
        # comment.delete()
        # 手动控制事务，实现回滚
        transaction.rollback()
    return HttpResponse('ok')


# Q()函数查询使用
def page_q(request):
    """
    Q()函数的查询使用
    """
    # # or |
    # # URL中获取查询参数
    # name = request.GET.get('name', None)    # 前台访问地址，http://127.0.0.1:9000/weibo/q/?name=user2 传入参数
    # query = Q(username=name) | Q(nickname=name)
    # # 查询username或者nickname都为user2的用户
    # # query = Q(username='user2') | Q(nickname='user2')
    # user_list = User.objects.filter(query)
    # print(user_list)

    # and &
    # 查询用户名是xxx，而且昵称是xxx的用户
    # username 按用户名称查询
    username = request.GET.get('username', None)
    if username is not None:
        query = Q(username=username)
    # nickname 按用户昵称查询
    nickname = request.GET.get('nickname', None)
    if nickname is not None:
        query = query & Q(nickname=nickname)
    user_list_q2 = User.objects.filter(query)
    print(user_list_q2)
    for item in user_list_q2:
        print(item.username)

    return HttpResponse("ok")


# raw(sql)函数使用
def page_raw(request):
    """ raw(sql)函数的使用 """
    username = request.GET.get('username', '')
    sql = 'select id,username from weibo_user where username=%s'
    user_list = User.objects.raw(sql, [username])
    for item in user_list:
        print(item)
    # url 访问地址：http://127.0.0.1:8000/weibo/raw/?username=user1
    return HttpResponse('ok')


# 使用sql查询
def page_sql(request):
    """ 使用sql查询 """
    sql = 'select id,username from weibo_user where username=%s'
    # 获取数据库连接

    # 根据连接获取游标
    cursor = connection.cursor()
    # 根据游标执行sql
    result = cursor.execute(sql, ['user3'])
    # 获取查询结果
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return HttpResponse('ok')