from django.conf.urls import url, include


from student import views

urlpatterns = [
    # 聚合及统计
    url(r'^grade/$', views.page_stas, name='page_stas')
]