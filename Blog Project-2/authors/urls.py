from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('profile/', views.profile, name='profile'),
    path('profile/update_profile/', views.update_profile, name='update_profile'),
    path('profile/update_profile/pass_change/', views.pass_change, name='pass_change'),
    path('logout/', views.user_logout, name='user_logout'),
]
