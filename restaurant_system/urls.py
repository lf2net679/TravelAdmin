from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.restaurant_list, name='restaurant_list'),
    path('create/', views.restaurant_create, name='restaurant_create'),
    path('category/', views.restaurant_category, name='restaurant_category'),
]