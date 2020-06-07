
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=200, null=True)
    create_at = models.DateTimeField(null=True)

    photo = models.ImageField(upload_to='media', null=True)
    text = models.TextField(null=True)

    class Meta:
        ordering = ['create_at']
        db_table = 'post_table'

    def __str__(self):
        return self.title