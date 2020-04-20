from django.conf.urls import url

from . import views

urlpatterns = [
    # 对用户数据进行分页
    url('^user/(?P<page>\d+)/$', views.page_user, name='page_user'),
    # ORM查询练习
    url(r'^search/$', views.search, name='search'),
    # 事务练习
    url(r'^trans/$', views.trans, name='trans'),

]