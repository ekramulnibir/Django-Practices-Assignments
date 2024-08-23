from django.shortcuts import render
from task_model.models import TaskModel

def show_task(requeust):
    data = TaskModel.objects.all()
    return render(requeust,'home.html', {'data' : data})