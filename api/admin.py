from django.contrib import admin
from api.models import Product, Customer, CreditTransaction

class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'price', 'date_created', 'date_modified', 'user')
    search_fields = ['code']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'date_created', 'date_modified', 'user', 'is_active')
    list_filter = ('date_created', 'date_modified', 'is_active')
    search_fields = ['name', 'address', 'phone_number']
    readonly_fields = ('date_created', 'date_modified')


class CreditTransactionAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'vehicle_number', 'volume', 'price_per_litre', 'total_price', 'date_created', 'date_modified')
    list_filter = ('customer__name', 'product__code', 'date_created', 'date_modified')
    search_fields = ['customer__name', 'vehicle_number']
    readonly_fields = ('total_price', 'price_per_litre')

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CreditTransaction, CreditTransactionAdmin)
