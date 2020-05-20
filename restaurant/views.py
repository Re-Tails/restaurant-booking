from django.shortcuts import render
from django.http import HttpResponse
from restaurant.models import Item

def index(request):
    #return HttpResponse("Hello, world. You're at the index page.")
    return render(request, 'index.html')
# Create your views here.

#IT_CA = 1 = Breakfast
#IT_CA = 2 = Lunch
#IT_CA = 3 = Dinner
#IT_CA = 4 = Drinks
#IT_CA = 5 = Clear filter

def view_menu(request):
  
    if(request.GET.get('mybtn1')):
        data = Item.objects.filter(IT_CA = 1)
        context = {
        'items': data
        }
        return render(request, 'view_menu.html', context)

    elif(request.GET.get('mybtn2')):
        data = Item.objects.filter(IT_CA = 2)
        context = {
        'items': data
        }
        return render(request, 'view_menu.html', context)
    elif(request.GET.get('mybtn3')):
        data = Item.objects.filter(IT_CA = 3)
        context = {
        'items': data
        }
        return render(request, 'view_menu.html', context)

    elif(request.GET.get('mybtn4')):
        data = Item.objects.filter(IT_CA = 4)
        context = {
        'items': data
        }
        return render(request, 'view_menu.html', context)

    data = Item.objects.all()
    context = {
        'items': data
        }
    return render(request, 'view_menu.html', context)

