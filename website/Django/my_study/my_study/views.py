import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
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
    day = request.GET.get('day', '24')
    return HttpResponse('active: ' + year + month + day)


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