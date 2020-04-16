from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.http import HttpResponse
from weibo.models import WeiboUser as User
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
    # 查询z开头用户
    zero_list = User.objects.filter(nickname__startswith='z')   # startswith    以**开头
    print(zero_list)
    # 查询以1结尾的用户
    end_list = User.objects.filter(nickname__endswith='1')      # endswith      以**结尾
    print(end_list)
    # 查询在**选项（列表）   --in的使用
    in_list = User.objects.filter(status__in=('2'))   # in    查询在**选项（列表）之内的
    print(in_list)
    return HttpResponse('ok')