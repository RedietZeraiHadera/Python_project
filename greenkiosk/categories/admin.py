from django.contrib import admin

# Register your models here.
from .models import Categories

class Product_Category(admin.ModelAdmin):
    list_display = ["category_name"]

admin.site.register(Categories,Product_Category)    
