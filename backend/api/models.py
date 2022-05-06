from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'Categories'


class Dish(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    cost = models.FloatField(default=0)
    description = models.TextField(default='')
    img = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=None)
    class Meta:
        verbose_name_plural = 'Dishes'

class Comment(models.Model):
    info = models.TextField(default='')
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='comments')
    date = models.DateTimeField(default=timezone.now)

class Order(models.Model):
    cost = models.FloatField(default = 0)
    ordered_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='orders')
    date = models.DateTimeField(default=timezone.now)


