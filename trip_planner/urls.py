from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.trip_list, name='trip_list'),
    path('create/', views.trip_create, name='trip_create'),
    path('category/', views.trip_category, name='trip_category'),
]