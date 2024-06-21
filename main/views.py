from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index(request):
    return render(request, 'main/views/index.html')


def login_view(request):
    data = {}
    if request.user.is_authenticated:
        return redirect('projects')

    if request.method == "POST":
        user = authenticate(
            username=request.POST['email'],
            password=request.POST['password']
            )
        if user:
            login(request, user)
            return redirect('projects')
        else:
            data['notif'] = 'Invalid Email or Password'


    return render(request, 'main/views/login.html', data)


def projects(request):
    data = {}
    if request.user.is_authenticated:
        data['logined'] = True 
    return render(request, 'main/views/projects.html', data)