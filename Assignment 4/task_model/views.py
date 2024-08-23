from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def add_task(request):
    if request.method == "POST":
        task_model_form = forms.TaskModelForm(request.POST)
        if task_model_form.is_valid():
            task_model_form.save()
            print(task_model_form.cleaned_data)
            return redirect('home')
    else:
        task_model_form = forms.TaskModelForm()
    
    return render(request, './task_model/add_task.html', {'form': task_model_form})

def edit_task(request, id):
    task = models.TaskModel.objects.get(pk=id)
    task_model_form = forms.TaskModelForm(instance=task)

    if request.method == "POST":
        task_model_form = forms.TaskModelForm(request.POST, instance=task)
        if task_model_form.is_valid():
            task_model_form.save()
            return redirect('home')
    
    return render(request, './task_model/add_task.html', {'form': task_model_form})

def delete_task(request, id):
    task = models.TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('home')

