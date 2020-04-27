from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_menu', views.view_menu, name='view_menu'),
    # This url is a temporary url used for the development of the selecting dishes
    path('select_dish', views.select_dish, name='view_menu'),
]
