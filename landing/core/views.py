from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, 'login.html', {})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {})


@login_required
def soon(request):
    return render(request, 'soon.html', {})
