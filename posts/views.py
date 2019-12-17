from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Post


# Prikaz glavne stranice sa svim postovima
class PostListView(LoginRequiredMixin, ListView):
	model = Post
	template_name = 'posts/board.html'
	context_object_name = 'posts'

# Prikaz stranice za dodavanje postova
class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Post
	fields = ['post_title', 'post_tweet']

	def form_valid(self, form):
		form.instance.post_user_id = self.request.user
		return super().form_valid(form)

	success_url = reverse_lazy('posts-board')

# Prikaz stranice za update postova
class PostUpdateView(LoginRequiredMixin, UpdateView):
	model = Post
	fields = ['post_title', 'post_tweet']
	template_name = 'posts/edit_post.html'

	def form_valid(self, form):
		form.instance.post_user_id = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.post_user_id:
			return True
		return False

	success_url = reverse_lazy('posts-board')

# Prikaz profila sa postovima
class PostProfileView(ListView):
	model = Post
	template_name = 'posts/prfile.html'

	def get_queryset(self):
		queryset = super(PostProfileView, self).get_queryset()
		queryset = queryset.filter(post_user_id = self.request.user)
		return queryset

	context_object_name = 'posts'

# Brisanje posta
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.post_user_id:
			return True
		return False

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