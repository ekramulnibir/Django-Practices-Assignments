from django.shortcuts import render
from . forms import RegistrationForm

# Create your views here.
def homepage(request):
    # form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = RegistrationForm()
    return render(request,'./first_app/django_form.html',{'form': form})
