from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from ...models import Projects, Favorites

import json

@csrf_exempt
def post_project(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(username = request.user)
            
            if request.FILES.get('image'):
                project = Projects(
                    project_owner = user,
                    project_name = request.POST['project-name'],
                    project_description = request.POST['project-description'],
                    project_tools = request.POST['tools'],
                    project_discord_link = request.POST['discord-link'],
                    project_github_link = request.POST['github-link'],
                    project_image = request.FILES['image'],
                    project_date = request.POST['current-date'],
                    )
            else:
                project = Projects(
                    project_owner = user,
                    project_name = request.POST['project-name'],
                    project_description = request.POST['project-description'],
                    project_tools = request.POST['tools'],
                    project_discord_link = request.POST['discord-link'],
                    project_github_link = request.POST['github-link'],
                    project_date = request.POST['current-date'],
                    )
            project.save()
            return JsonResponse({'message' : 'success'}, status=200)
    return JsonResponse({'message' : 'Error'}, status=200)


@csrf_exempt
def favorite(request):
    if request.user.is_authenticated:
        data = json.loads(request.body)
        if data:
            user = User.objects.get(username = request.user)
            project = Projects.objects.get(project_id = data['project-id'])
            if data['add']:
                add_favorite = Favorites(
                    favorite_project = project,
                    user = user
                    )
                add_favorite.save()
                return JsonResponse({'message' : 'Success'})
            else:
                remove_favorite = Favorites.objects.get(
                    favorite_project = project,
                    user = user
                    )
                print(remove_favorite)
                remove_favorite.delete()
                return JsonResponse({'message' : 'Success'})
            
    return JsonResponse({'message' : 'Error'})


@csrf_exempt
def delete_post(request):
    pass