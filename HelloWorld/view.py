from django.http import HttpResponse
from django.shortcuts import render
from . import github


def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    context['woo'] ='you bad boy'
    gh = github.GitHub(username='usrname', password='password')
    repos = gh.user().starred.get()
#    repos= gh.users('richardissuperman').starred.get()
    context['repos'] = repos
    return render(request, 'hello.html', context)
