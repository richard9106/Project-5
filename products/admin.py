"""Register model to admin"""
from django.contrib import admin
from .models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    """ List of fields to display"""
    list_display = (
        'sku',
        'name',
        'description',
        'price',
        'has_size',
        'rating',
        'image',
    )
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """ List of fields to display"""
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
