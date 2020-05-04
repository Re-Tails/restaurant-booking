from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addItem', views.addItemView.as_view(), name='addItem'),
    path('addCategory', views.addCategoryView.as_view(), name='addCategory'),
    path('addBranch', views.addBranchView.as_view(), name='addBranch'),
    path('addTable', views.addTableView.as_view(), name='addTable'),
]