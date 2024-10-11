from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.theme_list, name='theme_list'),
    path('create/', views.theme_create, name='theme_create'),
    path('activities/', views.activity_management, name='activity_management'),
]