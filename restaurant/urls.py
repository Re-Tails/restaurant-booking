from django.urls import path
from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/add', views.addItemView.as_view(), name='addItem'),
    path('item/<int:pk>/update', views.updateItemView.as_view(), name='updateItem'),
    path('category/add', views.addCategoryView.as_view(), name='addCategory'),
    path('category/<int:pk>/update', views.updateCategoryView.as_view(), name='updateCategory'),
    path('branch/add', views.addBranchView.as_view(), name='addBranch'),
    path('branch/<int:pk>/update', views.updateBranchView.as_view(), name='updateBranch'),
    path('table/add', views.addTableView.as_view(), name='addTable'),
    path('table/<int:pk>/update', views.updateTableView.as_view(), name='updateTable'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(), name='logout_url'),
    path('register/', views.registerView, name='register_url'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
]