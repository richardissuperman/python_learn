from django.http import HttpResponse
from django.shortcuts import render
from . import github


def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    context['woo'] ='you bad boy'
    gh = github.GitHub()
    #issues = gh.repos('michaelliao')('githubpy').issues.get()
    repos= gh.users('richardissuperman').starred.get()
    #for repo in repos:
    #    print(repo['url'])
    #context['issues'] = issues
    context['repos'] = repos
    return render(request, 'hello.html', context)
