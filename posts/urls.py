from django.urls import path, include
from . import views
from .views import (PostListView, PostCreateView)

#Rutiranje za posts aplikaciju
urlpatterns = [
    path('', PostListView.as_view(), name = 'posts-board'),
    path('profile/', views.profile, name = 'posts-profile'),
    path('new_post/', PostCreateView.as_view(), name = 'posts-new_post'),
    path('logout/', views.logout, name = 'posts-logout'),
]
