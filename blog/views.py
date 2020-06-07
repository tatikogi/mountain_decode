
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, Category
from django.shortcuts import get_object_or_404
from django.db.models import Count


class IndexView(ListView):
    template_name = 'blog/index.html'
    model = Post
    paginate_by = 10

class DetailView(DetailView):
    template_name = 'blog/detail.html'
    model = Post

class AboutView(TemplateView):
    template_name = 'blog/about.html'



class CategoryListView(ListView):
    template_name = 'blog/category_list.html'
    queryset = Category.objects.annotate(num_posts=Count('post'))


class CategoryPostView(ListView):
    model = Post
    template_name = 'blog/category_post.html'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, slug=category_slug)
        qs = super().get_queryset().filter(category=self.category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
