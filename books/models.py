from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(unique=True, max_length=255)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ImageField(upload_to='avatars/', null=True, blank=True)
    def __str__(self):
        return self.name   
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(decimal_places=2, default=0, null=True, blank=True, max_digits=10)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name='books' )
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    
    