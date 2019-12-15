from django.urls import path, include
from . import views

#Rutiranje za posts aplikaciju
urlpatterns = [
    path('', views.board, name = 'posts-board'),
    path('profile/', views.profile, name = 'posts-profile'),
    path('new_post/', views.new_post, name = 'posts-new_post'),
    path('logout/', views.logout, name = 'posts-logout'),
]
