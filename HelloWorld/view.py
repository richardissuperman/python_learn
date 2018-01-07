from django.http import HttpResponse
from django.shortcuts import render
from . import github


def hello(request):
    context          = {}
    if request.session.get('token') :
    
        accessToken = request.session['token']
        request.session['token'] = accessToken
        userGh = github.GitHub(access_token=accessToken)
        repos = userGh.user().starred.get()
        context['repos'] = repos
        return render(request, 'hello.html', context)
    else:
        
        code = request.GET.get('code')
        gh =github.GitHub(client_id='61673834ac87164b5488', client_secret='x')
        accessToken = gh.get_access_token(code)
        request.session['token'] = accessToken
        userGh = github.GitHub(access_token=accessToken)
        repos = userGh.user().starred.get()
        context['repos'] = repos
        return render(request, 'hello.html', context)


def login(request):
    context          = {}
    gh = github.GitHub(client_id='61673834ac87164b5488', client_secret='')
    print(gh.authorize_url())
    context['url'] = gh.authorize_url()
    return render(request, 'login.html', context)

