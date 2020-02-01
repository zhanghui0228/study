from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


def index(request):
    return HttpResponse('accounts')


class ShowClassView(TemplateView):
    ''' class 视图 '''
    template_name = 'showclass.html'