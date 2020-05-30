
from django.views.generic import ListView, DetailView
from .models import Post

class IndexView(ListView):
    template_name = 'blog/index.html'
    model = Post

class DetailView(DetailView):
    template_name = 'blog/detail.html'
    model = Post