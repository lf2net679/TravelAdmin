from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_home, name='forum_home'),
    path('articles/', views.forum_article_list, name='forum_article_list'),
    path('articles/create/', views.forum_article_create, name='forum_article_create'),
    path('categories/', views.forum_category_list, name='forum_category_list'),
    path('comments/', views.forum_comment_list, name='forum_comment_list'),
]