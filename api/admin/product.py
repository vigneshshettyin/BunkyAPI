from django.contrib import admin
from api.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("code", "price", "created_at", "updated_at", "user")
    search_fields = ["code"]

admin.site.register(Product, ProductAdmin)