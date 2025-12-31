from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_page, name='auth'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
