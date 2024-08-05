from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from ...models import Projects, Favorites, User_UUID

import json

@csrf_exempt
def post_project(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(username = request.user)
            
            project = Projects(
                project_owner = user,
                project_name = request.POST['project-name'],
                project_description = request.POST['project-description'],
                project_tools = request.POST['tools'],
                project_discord_link = request.POST['discord-link'],
                project_github_link = request.POST['github-link'],
                project_date = request.POST['current-date'],
                )
            
            if request.FILES.get('image'):
                project.project_image = request.FILES['image'],
            
            project.search_reference = f'{request.POST['project-name']} {request.POST['tools']} {project.project_owner.first_name} {project.project_owner.last_name}'
            project.save()
            return JsonResponse({'message' : 'success'}, status=200)
    return JsonResponse({'message' : 'Error'}, status=200)


@csrf_exempt
def update_project(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id = request.POST['project_id']
            project = Projects.objects.get(project_id = id)

            if project.project_owner.username == request.user.username:
                project.project_name = request.POST['project-name']
                project.project_github_link = request.POST['github-link']
                project.project_discord_link = request.POST['discord-link']
                project.project_tools = request.POST['tools']
                project.project_description = request.POST['project-description']
                project.search_reference = f'{request.POST['project-name']} {request.POST['tools']} {project.project_owner.first_name} {project.project_owner.last_name}'

                if request.FILES.get('image'):
                    project.project_image = request.FILES['image'] 
                project.save()
                
                return JsonResponse({'message' : 'success'}, status=200)
    return JsonResponse({'message' : 'error'}, status=200)


@csrf_exempt
def delete_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id = request.POST['project_id'].replace('delete-', '')
            project = Projects.objects.get( project_id =  id)

            if project.project_owner.username == request.user.username:
                project.delete()
            return JsonResponse({'message' : 'success'}, status=200)
    return JsonResponse({'message' : 'error'}, status=200)


@csrf_exempt
def favorite(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        if data:
            user = User.objects.get(username = request.user)
            project = Projects.objects.get(project_id = data['project-id'])
            favorite = Favorites.objects.filter(favorite_project = project, user = user)
    
            if not favorite: 
                add_favorite = Favorites(favorite_project = project, user = user)
                add_favorite.save()
            else:
                favorite.delete()
            return JsonResponse({'message' : 'Success'})
    return JsonResponse({'message' : 'Error'})


@csrf_exempt
def view_owner(request):
    data = json.loads(request.body)
    try:
        project = Projects.objects.get(project_id = data['project_id'])
    except:
        project = False

    if project:
        user_uuid = User_UUID.objects.get(user_account = project.project_owner)
        return JsonResponse({'message' : user_uuid.user_UIID}, status = 200)
    return JsonResponse({'message' : 'error'}, status = 200)