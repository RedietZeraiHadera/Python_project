from django.contrib import admin

# Register your models here.
from .models import Promotion


class PromotionAdmin(admin.ModelAdmin):
    list_display = ("product_name","description","start_date","end_date")
    
admin.site.register(Promotion,PromotionAdmin)

    
