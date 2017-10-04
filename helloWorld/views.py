# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
class HomeView(TemplateView):
    template_name = 'index.html'

from django.shortcuts import render
from django.http import HttpResponse


import requests

# Create your views here.
def index(request):
    #return HttpResponse('Hello from Python!')
    #return render(request, 'index.html')


    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')


