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
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),
    url(r'^active/(?P<year>[0-9]{4})/$', views.active, name='active_date'),

    # 使用include包含其它模块的url
    url(r'accounts/', include('accounts.urls', namespace='accounts')),
    #定义视图，展示当前的时间
    url(r'^time/$', views.now_time, name='time'),
    #读取html文件响应内容
    url(r'^use/$', views.use_file, name='use'),

    #重定向
    url(r'^index1/$', views.index_one, name='index_one'),
    url(r'^index/two/$', views.index_two, name='index_two')
]
