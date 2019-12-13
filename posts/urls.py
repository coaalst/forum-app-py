from django.urls import path, include
from . import views

#Rutiranje za posts aplikaciju

urlpatterns = [
    path('', views.home, name = 'posts-home'),
]
