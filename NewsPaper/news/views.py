from django.shortcuts import render
from django.views.generic import ListView, DetailView
from datetime import datetime
# Create your views here.
from .models import Post

class NewsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'