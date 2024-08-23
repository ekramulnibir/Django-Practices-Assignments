from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def add_task_category(request):
    if request.method == 'POST':
        task_category_form = forms.TaskCategoryModelForm(request.POST)
        if task_category_form.is_valid():
            task_category_form.save()
            return redirect('add_task_category')
    else:
        task_category_form = forms.TaskCategoryModelForm()

    return render(request,'./task_category_model/add_task_category.html', {'form':task_category_form})