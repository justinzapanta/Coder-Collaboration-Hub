from django.urls import path
from . import views
from .api.authentication import authentications
from .api.backend import projects
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, {'current_page': 1, 'search' : ' '}, name='projects'),
    path('projects/<int:current_page>/<str:search>', views.projects, name='projects'),
    path('sign-out', views.sign_out, name='sign out'),
    path('profile/',views.profile, {'user_uuid' : 'current_user'}, name='profile'),
    path('profile/<str:user_uuid>', views.profile, name='profile'),
    path('favorite/', views.favorites, name='favorite'),

    #api
    path('api/auth/login/', authentications.sign_in),
    path('api/auth/sign-up/', authentications.sign_up),

    #projects
    path('api/projects/post/', projects.post_project),
    path('api/projects/favorite/', projects.favorite),
    path('api/projects/delete/', projects.delete_post),
    path('api/projects/update/', projects.update_project),
    path('api/projects/view_owner/', projects.view_owner),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)