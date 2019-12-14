from django.shortcuts import render
from django.http import HttpResponse

# Login
def auth(request):
    return render(request, 'posts/auth.html', {'login': 'Uloguj se', 'register': 'Registruj se'})

# Main board
def board(request):
    return render(request, 'posts/board.html')

# Profile page
def profile(request):
    return render(request, 'posts/profile.html')

# New posts
def new_post(request):
    return render(request, 'posts/new_post.html')

# Logout
def logout(request):
    return render(request, 'posts/auth.html', {'login': 'Uloguj se', 'register': 'Registruj se'})