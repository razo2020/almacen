from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('kardex/', Dashboard.as_view(), name='kardex'),
    path('add-kardex/', AddKardex.as_view(), name='add-kardex'),
    path('edit-kardex/<int:pk>', EditKardex.as_view(), name='edit-kardex'),
    path('materiales/', ReporteMateriales.as_view(), name='materiales'),
    path('add-material/', AddMaterial.as_view(), name='add-material'),
    path('edit-material/<str:pk>', EditMaterial.as_view(), name='edit-material'),
    path('inventario/', Invetario.as_view(), name='inventario'),
    path('delete-item/<int:pk>', DeleteItem.as_view(), name='delete-item'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='inventory/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='inventory/logout.html'), name='logout'),
]