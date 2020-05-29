from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Item, Category, Branch, Table
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from restaurant.forms import RegistrationForm, EditProfileForm, AddOrderForm

from restaurant.models import Item
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


def addOrder(request):
    if request.method == "POST":
        form = AddOrderForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.OR_CU_id = request.user.pk
            temp = temp.save()
            return redirect('index')
    else:
        form = AddOrderForm()
    context = {
        'form': form
    }
    return render(request, 'addOrder.html', context)



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
        context = super(updateItemView, self).get_context_data(**kwargs)
        context['title'] = 'Update Item'
        context['type'] = 'item'
        context['id'] = self.get_object().IT_PK
        context['deleteButton'] = True
        return context

class deleteItemView(DeleteView):
    model = Item
    template_name = 'restaurant/templates/delete_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(deleteItemView, self).get_context_data(**kwargs)
        context['title'] = 'Delete Item'
        context['name'] = self.get_object().IT_Name
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
        context = super(updateCategoryView, self).get_context_data(**kwargs)
        context['title'] = 'Update Category'
        return context

class deleteCategoryView(DeleteView):
    model = Item
    template_name = 'restaurant/templates/delete_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(deleteCategoryView, self).get_context_data(**kwargs)
        context['title'] = 'Delete Category'
        context['name'] = self.get_object().CA_Name
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
        context = super(updateBranchView, self).get_context_data(**kwargs)
        context['title'] = 'Update Branch'
        return context

class deleteBranchView(DeleteView):
    model = Item
    template_name = 'restaurant/templates/delete_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(deleteBranchView, self).get_context_data(**kwargs)
        context['title'] = 'Delete Branch'
        context['name'] = self.get_object().BR_Name
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

def view_menu(request):
    entree = Item.objects.all().filter(IT_CA = 1)
    main = Item.objects.all().filter(IT_CA = 2)
    dessert = Item.objects.all().filter(IT_CA = 3)
    context = {
        'entrees': entree,
        'mains': main,
        'desserts': dessert
    }
    return render(request, 'view_menu.html', context)

def select_dish(request):
    entree = Item.objects.all().filter(IT_CA = 1)
    main = Item.objects.all().filter(IT_CA = 2)
    dessert = Item.objects.all().filter(IT_CA = 3)
    context = {
        'entrees': entree,
        'mains': main,
        'desserts': dessert
    }
    return render(request, 'select_dish.html', context)

class updateTableView(UpdateView):
    model = Table
    fields = ['TA_BR', 'TA_Code', 'TA_Seats']
    template_name = 'restaurant/templates/add_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(updateTableView, self).get_context_data(**kwargs)
        context['title'] = 'Update Table'
        return context

class deleteTableView(DeleteView):
    model = Item
    template_name = 'restaurant/templates/delete_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(deleteTableView, self).get_context_data(**kwargs)
        context['title'] = 'Delete Table'
        context['name'] = self.get_object().TA_Code
        return context
