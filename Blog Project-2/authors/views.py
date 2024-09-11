from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from posts.models import Post

# Create your views here.
# def add_author(request):
#     if request.method == 'POST':
#         author_from = forms.AuthorForm(request.POST)
#         if author_from.is_valid():
#             author_from.save()
#             print(author_from.cleaned_data)
#             return redirect('add_author') 
#     else:
#         author_from = forms.AuthorForm()

#     return render(request, './authors/add_author.html', {'form':author_from})


def register(request):
    if request.method == 'POST':
        registration_form = forms.RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('register')
    else:
        registration_form = forms.RegistrationForm()
    
    return render(request, './authors/register.html', {'form': registration_form, 'type': 'Registration'})


def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']

            user = authenticate(username = user_name, password = user_pass)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully')
                return redirect('profile')
            
            messages.warning(request, 'No user Found')
            return redirect('register')
            
    else:
        login_form = AuthenticationForm()
        return render(request, './authors/register.html', {'form': login_form, 'type': 'Login'})

@login_required 
def profile(request):
    data = Post.objects.filter(author = request.user)
    return render(request,'./authors/profile.html', {'data' : data})
    

def pass_change(request):
    if request.method == 'POST':
        pass_change_form = PasswordChangeForm(request.user, request.POST)
        if pass_change_form.is_valid():
            pass_change_form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, pass_change_form.user)
            return redirect('profile')
    else:
        pass_change_form = PasswordChangeForm(user = request.user)

    return render(request, './authors/pass_change.html', {'form' : pass_change_form, 'type' : 'Password Change'})

def update_profile(request):
    if request.method == 'POST':
        update_profile_form = forms.ChangeUserDataForm(request.POST, instance = request.user)
        if update_profile_form.is_valid():
            update_profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('register')
    else:
        update_profile_form = forms.ChangeUserDataForm(instance = request.user)
        return render(request, './authors/update_profile.html', {'form': update_profile_form, 'type': 'Update Profile'})


def user_logout(request):
    logout(request)
    return redirect('homepage')