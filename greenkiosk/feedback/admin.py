from django.contrib import admin

# Register your models here.
from .models import Reviews
class Reviews_admin(admin.ModelAdmin):
    list_display = ("user_name","comment")

admin.site.register(Reviews,Reviews_admin)    