
from django.db.models import Count
from blog.models import Category

def common(request):
    context = {
        'categories': Category.objects.annotate(num_posts=Count('post')),
    }
    return context