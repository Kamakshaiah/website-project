
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

from .forms import ChangePasswordForm
from accounts.admin import UserCreationForm
from .models import MyUser

# Create your views here.

def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        email = request.POST.get('email')
        password = request.POST.get('password1')
        # print(user)
        if form.is_valid():
            form.save()
            user = authenticate(request, email=email, password=password)
            # print(request.user.is_authenticated)
            login(request, user)
            messages.success(request, 'Profile created successfully!.')
            return redirect('home')
             
    else: 
        form = UserCreationForm()
    
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)

def UserProfile(request, id):
    user = MyUser.objects.get(pk=id)
    print(user.image.url)
    context = {
        'user': user
    }
    return render(request, 'registration/profile.html', context)

# def ChangePasswordView(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.POST)
#         new_password = request.POST.get("password")
#         user = request.user
#         user.set_password(new_password)
#         user.save()
#         messages.success(request, 'Password changed successfully!.')
#     else: 
#         form = PasswordChangeForm(request.user)
#     context = {
#         'form': form 
#     }

#     return render(request, 'registration/password_change_form.html', context)

def ChangePasswordView(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change_form.html', {
        'form': form
    })