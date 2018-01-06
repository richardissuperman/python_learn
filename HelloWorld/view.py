from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    context['woo'] ='you bad boy'
    return render(request, 'hello.html', context)
