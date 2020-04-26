"""my_study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from . import settings
from . import views

# 重新编写错误响应视图页面
# 重新定义500错误视图响应
handler500 = 'my_study.views.page_500'
# 重新定义404错误视图响应
handler404 = 'my_study.views.page_404'


# 定义视图url
urlpatterns = [
    # 微博模块，实现分页
    url(r'^weibo/', include('weibo.urls', namespace='weibo')),
    # 学生程间模块, 进行聚合与统计
    url(r'^student/', include('student.urls', namespace='student')),

    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),
    url(r'^active/(?P<year>[0-9]{4})/$', views.active, name='active_date'),

    # 使用include包含其它模块的url
    url(r'accounts/', include('accounts.urls', namespace='accounts')),
    # 定义视图，展示当前的时间
    url(r'^time/$', views.now_time, name='time'),
    # 读取html文件响应内容
    url(r'^use/$', views.use_file, name='use'),

    # 重定向
    url(r'^index1/$', views.index_one, name='index_one'),
    url(r'^index/two/$', views.index_two, name='index_two'),

    # 打印请求对象
    url(r'^print/request/$', views.print_request, name='print_request'),
    # 响应文本对象
    url(r'^print/resp/$', views.print_resp, name='print_resp'),
    # 响应json对象
    url(r'^print/json/$', views.print_json, name='print_json'),
    # 打印响应对象  状态码
    url(r'^print/resp/attr/$', views.print_attr, name='print_attr'),
    # 打印图片 FileResponse
    url('^print/image/$', views.print_image, name='print_image'),
    # 使用class来改写视图
    url('^show/class/$', views.ShowClassView.as_view(), name='show_class'),
    # 模板引擎选择
    url(r'^templ/show/$', views.templ_show, name='templ_show'),
    # 渲染静态图片 + 渲染python中的对象
    url(r'^templ/images/$', views.templ_images, name='templ_images'),
    # 模板标签使用
    url(r'^templ/tag/$', views.templ_tag, name='templ_tag'),
    # 模板过滤器使用
    url(r'^templ/filter/$', views.templ_filter, name='templ_filter'),
]
# 添加自定义的静态文件目录访问（用户自己上传的一些文件）
urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {
    'document_root': settings.MEDIA_ROOT
    })
]