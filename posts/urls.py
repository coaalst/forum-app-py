from django.urls import path, include
from . import views

#Rutiranje za posts aplikaciju

urlpatterns = [
    path('', views.auth, name = 'posts-auth'),
    path('board/', views.board, name = 'posts-board'),
    path('profile/', views.profile, name = 'posts-profile'),
    path('new_post/', views.new_post, name = 'posts-new_post'),
]
