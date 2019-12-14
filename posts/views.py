from django.shortcuts import render
from django.http import HttpResponse


def auth(request):
    return render(request, 'posts/auth.html', {'login': 'Uloguj se', 'register': 'Registruj se'})


def board(request):
    return render(request, 'posts/board.html')


def profile(request):
    return render(request, 'posts/profile.html')


def new_post(request):
    return render(request, 'posts/new_post.html')
