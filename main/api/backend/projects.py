from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from ...models import Projects, Favorites

import json

@csrf_exempt
def post_project(request):
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username = request.user)
            data = json.loads(request.body)

            project = Projects(
                project_owner = user,
                project_name = data['project-name'],
                project_description = data['project-description'],
                project_tools = data['tools'],
                project_discord_link = data['discord-link'],
                project_github_link = data['github-link'],
                project_date = data['current-date'],
                )
            project.save()
            return JsonResponse({'message' : 'success'}, status=200)
        except:
            return JsonResponse({'message' : 'Try Again'}, status=200)
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