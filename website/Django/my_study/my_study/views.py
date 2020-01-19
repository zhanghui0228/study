import datetime

from django.http import HttpResponse
from django.urls import reverse


def index(request):
    #逆向解析active的url
    url = reverse('active_date', args=(2020,))
    #逆向解析命名空间accounts的url
    url_accounts = reverse('accounts:index')        #accounts为全局urls文件里定义的namespace名称；index为其它包模块中urls中定义的name
    return HttpResponse('ok:' + url + url_accounts)


def active(request, year):
    return HttpResponse('active: '+ year)


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