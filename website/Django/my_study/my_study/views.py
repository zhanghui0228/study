import datetime
import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import loader
from django.urls import reverse

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


#使用html文件进行响应
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


#重定向
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


def page_500(request):
    ''' 重写500错误响应视图 '''
    return HttpResponse("系统正在维护中......")


def page_404(request):
    ''' 重写404错误响应视图 '''
    return HttpResponse('访问资源不存在！')