from django.urls import path
from . import views
from .api.authentication import authentications

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('sign-out', views.sign_out, name='sign out'),
    path('api/auth/login/', authentications.sign_in)
]