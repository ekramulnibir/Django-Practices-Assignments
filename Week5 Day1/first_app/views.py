from django.shortcuts import render,redirect
from .forms import SignupForm, UpdateProfileForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.method == "POST":
        singup_form = SignupForm(request.POST)
        if singup_form.is_valid():
            messages.success(request, 'Account Created Successfully')
            singup_form.save()
            return redirect('profile')
        
    else:
        singup_form = SignupForm()

    return render(request, './first_app/form.html', {'form': singup_form})

def user_login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username = user_name, password = user_pass)

            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile')
        
    else:
        login_form = AuthenticationForm()
        
    return render(request, './first_app/form.html', {'form': login_form})

@login_required  
def profile(request):
    return render(request, './first_app/profile.html')

@login_required  
def update_profile(request):
    if request.method == "POST":
        update_profile_form = UpdateProfileForm(request.POST, instance = request.user)
        if update_profile_form.is_valid():
            messages.success(request, "Profile Updated Successfully")
            update_profile_form.save()
            return redirect('update_profile')

    else:
        update_profile_form = UpdateProfileForm(instance=request.user)
        
    return render(request, './first_app/update_profile.html', {'form':update_profile_form})

@login_required  
def change_pass(request):
    if request.method == "POST":
        change_pass_form = PasswordChangeForm(request.user, request.POST)
        if change_pass_form.is_valid():
            change_pass_form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, change_pass_form.user)
            return redirect('profile')
    
    else:
        change_pass_form = PasswordChangeForm(user = request.user)
    
    return render(request, './first_app/change_pass.html', {'form' : change_pass_form})

def change_pass_wop(request):
    if request.method == "POST":
        change_pass_form = SetPasswordForm(request.user, request.POST)
        if change_pass_form.is_valid():
            change_pass_form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, change_pass_form.user)
            return redirect('profile')
    
    else:
        change_pass_form = SetPasswordForm(user = request.user)
    
    return render(request, './first_app/change_pass.html', {'form' : change_pass_form})


@login_required  
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('login')




