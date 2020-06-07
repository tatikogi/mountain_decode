
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/<str:category_slug>/', views.CategoryPostView.as_view(), name='category_post'),
    path('about/', views.AboutView.as_view(), name='about'),
]