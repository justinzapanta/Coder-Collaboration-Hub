from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import Projects, Favorites, User_UUID

# Create your views here.
def index(request):
    return render(request, 'main/views/index.html')


def projects(request, current_page, search):
    data = {}
    data['current_page'] = current_page
    if request.user.is_authenticated:
        data['logined'] = True
        favorites = Favorites.objects.filter(user = request.user).values_list('favorite_project__project_id', flat=True)
        data['favorites'] = favorites

    project = Projects.objects.all().order_by('-project_date')
    if request.method == 'POST' or search:
        if request.POST.get('search'):
            project = Projects.objects.filter(search_reference__icontains = request.POST['search'].lower()).order_by('-project_date')
            data['search'] = request.POST['search']
            data['pagination'] = list(range(1, 2))
            
    pagination = float(len(project) / 10)
    data['pagination'] = list(range(1, int(pagination + 1)))
    if '.' in str(pagination) and pagination > 1:
        data['pagination'] = list(range(1, int(pagination) + 2))
        
    start_at = (current_page - 1) * 10
    end_at = (current_page * 10)
    project = project[start_at: end_at]

    data['project_length'] = len(project)
    data['projects'] = project
    return render(request, 'main/views/projects.html', data)


def sign_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('projects')


def profile(request, user_uuid):
    user_profile = False
    if user_uuid == "current_user":
        user_uuid = User_UUID.objects.get(user_account = request.user)
        user_profile = True
    else:
        user_uuid = User_UUID.objects.get(user_UIID = user_uuid)

    user = User.objects.get(username = user_uuid.user_account.username)
    projects = Projects.objects.filter(project_owner = user).order_by('-project_date')
    favorites = Favorites.objects.filter(user = user).values_list('favorite_project__project_id', flat=True)
    
    return render(request, 'main/views/profile.html', {'projects' : projects, 'user' : user, 'favorites' : favorites, 'user_profile' : user_profile})


def favorites(request):
    if request.user.is_authenticated:
        favorite_content = Favorites.objects.filter(user = request.user).values_list('favorite_project__project_id', flat=True)
        projects = []
        for content in favorite_content:
            project = Projects.objects.get(project_id = content)
            projects.append(project)

        print(projects)
        return render(request, 'main/views/favorite.html', {'projects' : projects, 'user' : request.user, 'favorites' : favorite_content})
    return render(request, 'main/views/favorite.html')

