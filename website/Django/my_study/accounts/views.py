from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


def index(request):
    return HttpResponse('accounts')


class ShowClassView(TemplateView):
    ''' class 视图 '''
    template_name = 'showclass.html'


# 自定义过滤器
def templ_filter_mine(request):
    ''' 自定义的过滤器 '''
    list_filter = ('one', 'two', 'three')
    sum_list = 10000000
    return render(request, 'templ_filter_mine.html', {'list_filter': list_filter, 'sum_list': sum_list})