from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_workout, name='add_workout'),
    path('edit/<int:id>/', views.edit_workout, name='edit_workout'),
]
