from django.urls import path
from . import views

urlpatterns = [
    path('add_task_category/', views.add_task_category , name = 'add_task_category'),
]