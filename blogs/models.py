from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title =models.CharField(max_length=100)
    Blog_body = models.TextField
