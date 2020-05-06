from django.conf.urls import url

from . import views

urlpatterns = [
    # 对用户数据进行分页
    url('^user/(?P<page>\d+)/$', views.page_user, name='page_user'),
    # ORM查询练习
    url(r'^search/$', views.search, name='search'),
    # 事务练习
    url(r'^trans/$', views.trans, name='trans'),
    # 使用with进行事务练习
    url(r'^trans_with/$', views.trans_with, name='trans_with'),
    # 手动控制事务
    url(r'^trans_hand/$', views.trans_hand, name='trans_hand'),
    # Q()函数查询使用
    url(r'^q/$', views.page_q, name='page_q'),

]