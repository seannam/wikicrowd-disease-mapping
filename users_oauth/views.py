from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    context = {}
    return render(request, 'users_oauth/index.html', context)


@login_required()
def profile(request):
    context = {}
    return render(request, 'users_oauth/profile.html', context)


def login_oauth(request):
    context = {}
    return render(request, 'users_oauth/login.html', context)
