from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category", "description"]
    list_filter = ["category"]
    list_editable = ["price"]

admin.site.register(Product, ProductAdmin)