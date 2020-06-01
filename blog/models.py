
from django.db import models

class Post(models.Model):

    title = models.CharField(max_length=200, null=True, blank=True)
    create_at = models.DateTimeField(null=True, blank=True)

    photo = models.ImageField(upload_to='images', null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['create_at']
        db_table = 'post_table'

    def __str__(self):
        return self.title