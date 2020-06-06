
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post

class IndexView(ListView):
    template_name = 'blog/index.html'
    model = Post
    paginate_by = 10

class DetailView(DetailView):
    template_name = 'blog/detail.html'
    model = Post

class AboutView(TemplateView):
    template_name = 'blog/about.html'