from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDo #Cause models is in the same folder
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def home(request):
   context = {
      'posts': Post.objects.all()
   }
   return render(request, 'blog/home.html', context)

def about(request):
   return render(request, 'blog/about.html', {'name': "James"})

class PostListView(ListView):
   model = Post
   template_name = 'blog/home.html'
   context_object_name = 'posts'
   ordering = ['-date']

class PostDetailView(DetailView):
   model = ToDo

class PostCreateView(LoginRequiredMixin, CreateView):
   model = Post
   fields = ['title', 'text']

   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)


class ToDoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
   model = ToDo
   fields = ['todotitle', 'todotext', 'status']
   
   def form_valid(self, form):
      form.instance.author = self.request.user
      return super().form_valid(form)

   def test_func(self):
      ToDo = self.get_object()
      if(self.request.user) == ToDo.author:
         return True
      else:
         return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Post
   success_url = '/' #where to go when deleted the post

   def test_func(self): # Mixin uses this function to test if the user is the author
      post = self.get_object()
      if(self.request.user) == post.author:
         return True
      else:
         return False


# <app>/<model>_<view>.html


