from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Projects, Favorites

# Create your views here.
def index(request):
    data = {}
    if request.user.is_authenticated:
        data['logined'] = True
    return render(request, 'main/views/index.html', data)


def projects(request):
    data = {}
    if request.user.is_authenticated:
        data['logined'] = True
    
    project = Projects.objects.all()
    data['projects'] = project
    return render(request, 'main/views/projects.html', data)


def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('projects')