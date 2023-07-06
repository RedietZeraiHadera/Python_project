from django.contrib import admin

# Register your models here.
from .models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ("vendor_name","shop_name","phone_number")

admin.site.register(Vendor,VendorAdmin)
