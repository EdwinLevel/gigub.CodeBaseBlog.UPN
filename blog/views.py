#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Post
from django.urls import reverse_lazy

class BlogListView(ListView):
        model = Post
        template_name = 'home.html'

class BlogDetailView(DetailView):
        model = Post
        template_name = 'post_detail.html'
        
class BlogCreateView(CreateView):
        model = Post
        template_name = 'post_new.html'
        fields = ['titulo', 'servidor', 'nombre_autor', 'ingredientes', 'pasos']

class BlogDeleteView(DeleteView):
        model = Post
        template_name = 'post_delete.html'
        fields = ['titulo']
        success_url = reverse_lazy('home')

class BlogUpdateView(UpdateView):
        model = Post
        template_name = 'post_new.html'
        fields = ['titulo', 'servidor', 'nombre_autor', 'ingredientes', 'pasos']
        
# Create your views here.
