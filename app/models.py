from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category (models.Model):
    name = models.CharField(max_length=225, db_index=True)
    slug = models.SlugField(max_length=225, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('category_list', args=[self.slug])

    def __str__(self):
        return self.name

class Poster(models.Model):
    category = models.ForeignKey(Category, related_name='poster', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='poster_creator')
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    desc = models.TextField(blank=True)
    image = models.FileField(blank=True)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    trending = models.BooleanField(default=False)
    new_arrivals = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Posters'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('poster_detail', args=[self.slug])

    def __str__(self):
        return self.title

class PosterImage(models.Model):
    poster = models.ForeignKey(Poster, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'media/')
    
    def __str__(self):
        return self.poster.title

