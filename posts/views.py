from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Main board
def board(request):
	context = {'posts': Post.objects.all()}
	return render(request, 'posts/board.html', context)

# Profile page
def profile(request):
    return render(request, 'posts/profile.html')

# New posts
def new_post(request):
    return render(request, 'posts/new_post.html')

# Logout
def logout(request):
    return render(request, 'posts/auth.html', {'login': 'Uloguj se', 'register': 'Registruj se'})