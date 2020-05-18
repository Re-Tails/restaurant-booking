from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Item, Category, Branch, Table
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from restaurant.forms import RegistrationForm, EditProfileForm

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
# Create your views here.

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


class addItemView(CreateView):
    model = Item
    fields = ['IT_Name', 'IT_Price', 'IT_CA', 'IT_Calories', 'IT_GluttenFree', 'IT_Vegetarian', 'IT_Profit', 'IT_Image']
    template_name = 'restaurant/templates/add_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(addItemView, self).get_context_data(**kwargs)
        context['title'] = 'Add Item'
        return context

class updateItemView(UpdateView):
    model = Item
    fields = ['IT_Name', 'IT_Price', 'IT_CA', 'IT_Calories', 'IT_GluttenFree', 'IT_Vegetarian', 'IT_Profit', 'IT_Image']
    template_name = 'restaurant/templates/add_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(addItemView, self).get_context_data(**kwargs)
        context['title'] = 'Update Item'
        return context

class addCategoryView(CreateView):
    model = Category
    fields = ['CA_Name']
    template_name = 'restaurant/templates/add_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(addCategoryView, self).get_context_data(**kwargs)
        context['title'] = 'Add Category'
        return context
    
class updateCategoryView(CreateView):
    model = Category
    fields = ['CA_Name']
    template_name = 'restaurant/templates/add_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(addCategoryView, self).get_context_data(**kwargs)
        context['title'] = 'Update Category'
        return context

class addBranchView(CreateView):
    model = Branch
    fields = ['BR_Name', 'BR_Address']
    template_name = 'restaurant/templates/add_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(addBranchView, self).get_context_data(**kwargs)
        context['title'] = 'Add Branch'
        return context

class updateBranchView(UpdateView):
    model = Branch
    fields = ['BR_Name', 'BR_Address']
    template_name = 'restaurant/templates/add_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(addBranchView, self).get_context_data(**kwargs)
        context['title'] = 'Update Branch'
        return context

class addTableView(CreateView):
    model = Table
    fields = ['TA_BR', 'TA_Code', 'TA_Seats']
    template_name = 'restaurant/templates/add_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(addTableView, self).get_context_data(**kwargs)
        context['title'] = 'Add Table'
        return context

class updateTableView(UpdateView):
    model = Table
    fields = ['TA_BR', 'TA_Code', 'TA_Seats']
    template_name = 'restaurant/templates/add_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(addTableView, self).get_context_data(**kwargs)
        context['title'] = 'Update Table'
        return context

