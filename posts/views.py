from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView, CreateView)
from django.urls import reverse_lazy
from .models import Post

class PostListView(ListView):
	model = Post
	template_name = 'posts/board.html'
	context_object_name = 'posts'

class PostCreateView(CreateView):
	model = Post
	fields = ['post_title', 'post_tweet']

	def form_valid(self, form):
		form.instance.post_user_id = self.request.user
		return super().form_valid(form)

	success_url = reverse_lazy('posts-board')

# Profile page
@login_required
def profile(request):
	context = {'posts': Post.objects.all()}
	return render(request, 'posts/profile.html', context)

# New posts
@login_required
def new_post(request):
    return render(request, 'posts/new_post.html')

# Logout
def logout(request):
    return render(request, 'posts/auth.html')