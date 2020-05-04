from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(), name='logout_url'),
    path('register/', views.registerView, name='register_url'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
]
