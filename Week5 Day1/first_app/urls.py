from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_login, name = 'login'),
    path('signup/',views.signup, name = 'signup'),
    path('login/',views.user_login, name = 'login'),
    path('logout/',views.user_logout, name = 'logout'),
    path('profile/',views.profile, name = 'profile'),
    path('change_pass/',views.change_pass, name = 'change_pass'),
    path('change_pass_wop/',views.change_pass_wop, name = 'change_pass_wop'),
    path('update_profile/',views.update_profile, name = 'update_profile'),
]