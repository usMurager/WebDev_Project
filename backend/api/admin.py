from django.contrib import admin
from .models import Category,Dish,Comment,Order

admin.site.register((Category,Dish,Comment,Order))
# Register your models here.
