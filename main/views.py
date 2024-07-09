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


def projects(request, current_page, search):
    data = {}
    data['current_page'] = current_page
    if request.user.is_authenticated:
        data['logined'] = True

    project = Projects.objects.all().order_by('-project_id')
    if request.method == 'POST' or search:
        if request.POST.get('search'):
            project = Projects.objects.filter(search_reference__icontains = request.POST['search'].lower()).order_by('-project_id')
            data['search'] = request.POST['search']
            data['pagination'] = list(range(1, 2))
            
    pagination = float(len(project) / 10)
    data['pagination'] = list(range(1, int(pagination + 1)))
    if '.' in str(pagination) and pagination > 1:
        data['pagination'] = list(range(1, int(pagination) + 2))
        
    start_at = (current_page - 1) * 10
    end_at = (current_page * 10)
    project = project[start_at: end_at]

    data['projects'] = project
    return render(request, 'main/views/projects.html', data)


def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('projects')