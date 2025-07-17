from django.db import models
from django.db import migrations, models
# from django.utils import timezone
# from blog.models import Category

# Create your models here.
class Category(models.Model):
    Post=models.ForeignKey('Post', models.CASCADE, related_name='categories')
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=256)
    author=models.CharField(max_length=128)
    created_at=models.DateTimeField(auto_now_add=True)
    bio=models.TextField()
    slug=models.SlugField(max_length=256, unique=True)
    # uid=models.UUIDField()
    
    # created_at = models.DateTimeField(default=timezone.now,auto_now_add=True)

def __str__(self):
    return self.title