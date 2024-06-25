from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
import json

@csrf_exempt
def sign_in(request):
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