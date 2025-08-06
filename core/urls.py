from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('error/', views.error_view, name='error'),
]
