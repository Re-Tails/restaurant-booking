from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Hello, world. You're at the index page.")
    return render(request, 'index.html')
# Create your views here.

def view_menu(request):
    return render(request, 'view_menu.html')
