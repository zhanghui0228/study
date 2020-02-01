from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url('^show/class/$', views.ShowClassView.as_view(), name='show_class'),
]