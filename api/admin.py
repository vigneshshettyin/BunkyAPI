from django.contrib import admin
from api.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'price', 'date_created', 'date_modified', 'user')
    search_fields = ['code']

admin.site.register(Product, ProductAdmin)
