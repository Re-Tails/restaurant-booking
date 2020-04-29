from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Item, Category, Branch, Table

def index(request):
    #return HttpResponse("Hello, world. You're at the index page.")
    return render(request, 'index.html')
# Create your views here.

class addItemView(CreateView):
    model = Item
    fields = ['IT_Name', 'IT_Price', 'IT_CA', 'IT_Calories', 'IT_GluttenFree', 'IT_Vegetarian', 'IT_Profit', 'IT_Image']
    template_name = 'restaurant/templates/add_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(addItemView, self).get_context_data(**kwargs)
        context['title'] = 'Add Item'
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
    
    
class addBranchView(CreateView):
    model = Branch
    fields = ['BR_Name', 'BR_Address']
    template_name = 'restaurant/templates/add_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(addBranchView, self).get_context_data(**kwargs)
        context['title'] = 'Add Branch'
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