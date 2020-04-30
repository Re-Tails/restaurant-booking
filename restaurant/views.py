from django.shortcuts import render
from django.http import HttpResponse
from restaurant.models import Item

def index(request):
    #return HttpResponse("Hello, world. You're at the index page.")
    return render(request, 'index.html')
# Create your views here.


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
