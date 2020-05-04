from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from restaurant.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import views as auth_views


def index(request):
    #return HttpResponse("Hello, world. You're at the index page.")
    return render(request, 'index.html')

def dashboardView(request):
    return render(request, 'dashboard.html')

def registerView(request):
    if request.method == 'POST':
       form = RegistrationForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'restaurant/templates/registration/register.html', args)

def profile(request):
    args = {'user': request.user}
    return render(request, 'registration/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'registration/change_password.html', args)
