from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('view_menu', views.view_menu, name='view_menu'),
    # This url is a temporary url used for the development of the selecting dishes
    path('select_dish', views.select_dish, name='view_menu'),
    path('item/add', views.addItemView.as_view(), name='addItem'),
    path('item/<int:pk>/update', views.updateItemView.as_view(), name='updateItem'),
    path('item/<int:pk>/delete', views.deleteItemView.as_view(), name='deleteItem'),
    path('category/add', views.addCategoryView.as_view(), name='addCategory'),
    path('category/<int:pk>/update', views.updateCategoryView.as_view(), name='updateCategory'),
    path('category/<int:pk>/delete', views.deleteCategoryView.as_view(), name='deleteCategory'),
    path('branch/add', views.addBranchView.as_view(), name='addBranch'),
    path('branch/<int:pk>/update', views.updateBranchView.as_view(), name='updateBranch'),
    path('branch/<int:pk>/delete', views.deleteBranchView.as_view(), name='deleteBranch'),
    path('table/add', views.addTableView.as_view(), name='addTable'),
    path('table/<int:pk>/update', views.updateTableView.as_view(), name='updateTable'),
    path('branch/<int:pk>/delete', views.deleteBranchView.as_view(), name='deleteBranch'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('logout/', LogoutView.as_view(), name='logout_url'),
    path('register/', views.registerView, name='register_url'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('addOrder', views.addOrder, name='addOrder'),
    path('<int:pk>/addOrderItemEntree', views.addOrderItemEntree, name='addOrderItem'),
    path('<int:pk>/addOrderItemMain', views.addOrderItemMain, name='addOrderItemMain'),
    path('<int:pk>/addOrderItemDessert', views.addOrderItemDessert, name='addOrderItemDessert'),
    path('change_password/', views.change_password, name='change_password'),
    path('viewOrder', views.viewOrder, name='viewOrder'),
    path('order/<int:pk>/delete', views.deleteOrder, name='deleteOrder'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
