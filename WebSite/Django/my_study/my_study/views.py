import datetime
import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import loader
from django.urls import reverse
from django.views.generic import TemplateView

from . import settings


def index(request):
    #逆向解析active的url
    url = reverse('active_date', args=(2020,))
    #逆向解析命名空间accounts的url
    url_accounts = reverse('accounts:index')        #accounts为全局urls文件里定义的namespace名称；index为其它包模块中urls中定义的name
    return HttpResponse('ok:' + url + url_accounts)


def active(request, year):
    '''获取url中的参数'''
    #url访问方式:http://127.0.0.1:8000/active/2020/?month=12
    month = request.GET.get('month', None)
    # 获取GET中的参数
    day = request.GET.get('day', '00')
    # # 重写500错误代码响应
    # raise
    return HttpResponse('active: ' + year + month + day)


# 使用html文件进行响应
def use_file(request):
    ''' 从HTML文件读取内容，并进行响应 '''
    now = datetime.datetime.now()
    # #原始方法，方法一：
    # file_name = os.path.join(settings.BASE_DIR, 'templates', 'index.html')
    # with open(file_name, 'r', encoding='utf-8') as f:
    #     html = f.read()
    # html = html.replace('0', now.strftime('%Y-%m-%d'))
    # return HttpResponse(html)

    # #方法二：   --使用django中提供的方法
    # temp = loader.get_template('index.html')
    # html = temp.render({        #render传递参数，在htnl模板文件中的参数名必须用{{}}进行括起来
    #     #'模板中的参数': 需要传递的参数
    #     'now_time': now
    # })
    # return HttpResponse(html)

    # #方法三：   --使用render(request, template_name, 参数)函数
    # return render(request, 'index.html', {'now_time': now})

    #方法四：    --使用render_to_response(template_name, 参数)函数
    return render_to_response('index.html', {'now_time':now})


def now_time(request):
    '''
    定义视图，展示当前的时间
    :param request:
    :return:    time
    '''
    now = datetime.datetime.now()
    html = "now : {0}".format(now)
    html = """
    <html>
        <head>
            <title>time</title>
            <style type="text/css">
            body{{color: red;}}
            </style>
        </head>
        <body>
            now : {0}
        </body>
    </html>
    """.format(now)
    #响应
    return HttpResponse(html)


# 重定向
def index_one(request):
    ''' 重定向练习, 访问index1时，重定向到index two '''
    #方法一：
    # url = reverse('index_two')
    # #使用redirect()函数进行重定向
    # return redirect(url)
    # # 使用HttpResponseRedirect()函数进行重定向
    # # return HttpResponseRedirect(url)
    # #return HttpResponse('index one')

    #方法二：   直接指定url中定义的name
    return redirect('index_two')


def index_two(request):
    ''' 重定向练习， index2 '''
    return HttpResponse('index two')

# 重写错误代码
def page_500(request):
    ''' 重写500错误响应视图 '''
    return HttpResponse("系统正在维护中......")


def page_404(request):
    ''' 重写404错误响应视图 '''
    return HttpResponse('访问资源不存在！')


# 请求对象打印
def print_request(request):
    ''' 打印请求对象 '''
    print(request)
    print('-' * 50)
    # ip = request.META['REMOTE_ADDR']  # 远程访问地址
    user_agent = request.META['HTTP_USER_AGENT']    # 用户的浏览器
    print(user_agent)
    print(request.get_host())   # 访问地址
    # print(request.path())   # 请求路径
    print('-' * 50)
    return HttpResponse('hello request')


# 响应对象
def print_resp(request):
    ''' 响应对象  '''
    # 以文本方式进行响应输出
    now = datetime.datetime.now()
    temp = loader.get_template('index.html')
    html = temp.render({        # render传递参数，在htnl模板文件中的参数名必须用{{}}进行括起来
        # '模板中的参数': 需要传递的参数
        'now_time': now
    })
    return HttpResponse(html, content_type='text/plain')


def print_json(request):
    ''' 响应json对象 '''
    user_info = {
        'username': '张三',
        'passwd': '123456'
    }
    # # 方式一： 使用HttpResponse中的application/json进行响应
    # import json
    # # python字典转换为json格式
    # user_info = json.dumps(user_info)
    # return HttpResponse(user_info, content_type='application/json', )

    # 方式二： 使用JsonResponse进行响应
    from django.http import JsonResponse
    return JsonResponse(user_info)


def print_attr(request):
    now = datetime.datetime.now()
    ''' 响应对象 状态码'''
    resp =  HttpResponse('响应对象', status=202)
    # 重新设置HTTP的状态码
    resp.status_code = 206
    # 写入响应内容
    resp.write(now)
    return resp


def print_image(request):
    ''' 打印图片 FileResponse '''
    from django.http import FileResponse
    file_name = os.path.join(settings.BASE_DIR, 'media/images/22.jpg')
    f = open(file_name, 'rb')
    return FileResponse(f, content_type='image/jpg')


# 使用class来改写视图
class ShowClassView(TemplateView):
    ''' class 视图 '''
    template_name = 'show_class.html'


# 模板引擎选择
def templ_show(request):
    '''模板引擎选择'''
    # return render(request, "detail.html")
    return render(request, "app.html")


# 渲染静态图片
def templ_images(request):
    ''' 渲染模板文件 '''
    # 渲染静态图片
    img_url = "/media/images/22.jpg"
    # 渲染dict格式的python对象
    user_info = {
        "name": "张三",
        "age": 18
    }
    # 渲染list格式的python对象
    list_city = ['GJ', 'SH', 'SZ']
    # 渲染list嵌套dict格式的python对象
    list_prods = [
        {"name": "名称一", "price": 100},
        {"name": "名称二", "price": 120},
        {"name": "名称三", "price": 160},
    ]
    return render(request, 'image.html', {'img_url': img_url, "user_info": user_info, "list_city": list_city, "list_prods": list_prods})


# 模板标签使用
def templ_tag(request):
    ''' 模板标签使用 '''
    # 渲染list格式的python对象
    list_city = ['GJ', 'SH', 'SZ']
    # 渲染list嵌套dict格式的python对象
    list_prods = [
        {"name": "名称一", "price": 100},
        {"name": "名称二", "price": 120},
        {"name": "名称三", "price": 160},
        {"name": "名称四", "price": 160},
        {"name": "名称五", "price": 160},
        {"name": "名称六", "price": 160},
    ]
    list_order = []
    # 标签使用for循环对象 渲染对象dict
    list_info = {
        'name': "张三",
        'age': 18,
        'phone': 12345678901
    }
    return render(request, 'tag.html', {'list_city': list_city, 'list_prods': list_prods, 'list_order': list_order, 'list_info': list_info})


# 模板过滤器使用
def templ_filter(request):
    '''模板过滤器使用'''
    # 使用过滤器字母进行大写
    list_word = [
        'name',
        'age',
        'module',
        'STATUS'
    ]
    now = datetime.datetime.now()
    user_info = {
        'name': "张三",
        'age': None,
        'sex': ''
    }
    # 数字四舍五入显示
    import math
    pi = math.pi
    # 富文本展示
    html = '<h1>富文本展示,截取字符串</h1>' # <script>alert("跳转中...")</script>
    return render(request, 'filter.html', {'list_word': list_word, 'now': now, 'user_info': user_info, 'pi': pi, 'html': html})