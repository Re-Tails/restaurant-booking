from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view_menu', views.view_menu, name='view_menu'),
]
