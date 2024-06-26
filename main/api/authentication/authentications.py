from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import json

@csrf_exempt
def sign_in(request):
    if not request.user.is_authenticated:
        data = json.loads(request.body)
        if data:
            user = authenticate(
                username=data['email'],
                password=data['password']
                )
            if user:
                login(request, user)
                return JsonResponse({'message': 'success'}, status=200)
    return JsonResponse({'message' : 'Invalid Email or Password'}, status=200)


@csrf_exempt
def sign_up(request):
    if not request.user.is_authenticated:
        data = json.loads(request.body)
        if data:
            user = User.objects.filter(username = data['signup_email'])
            if not user:
                User.objects.create_user(
                    username = data['signup_email'],
                    password = data['signup_password'],
                    first_name = data['first_name'],
                    last_name = data['last_name'],
                    )
                return JsonResponse({'message' : 'Success'}, status=200)
            else:
                return JsonResponse({'message' : 'Email already in use'}, status=200)
    return JsonResponse({'message' : 'error'}, status=200)