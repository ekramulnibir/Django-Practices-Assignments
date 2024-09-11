from django.shortcuts import render,redirect
from .forms import CategoryForm

# Create your views here.
def add_category(request):
    if request.method == "POST":
        categroy_form = CategoryForm(request.POST)
        if categroy_form.is_valid():
            categroy_form.save()
            return redirect('add_category')
    else:
        categroy_form = CategoryForm(request.POST)

    return render(request, './categories/add_category.html', {'form':categroy_form})
