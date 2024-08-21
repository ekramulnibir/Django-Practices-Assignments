from django.shortcuts import render
from first_app.forms import StudentRegistrationForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentRegistrationForm()

    return render(request,'./first_app/home.html',{'form':form})
