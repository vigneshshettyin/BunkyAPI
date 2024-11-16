from django.contrib import admin
from api.models import Product, Customer, CreditTransaction, StockInventory, DailyLubeSales

class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'price', 'created_at', 'updated_at', 'user')
    search_fields = ['code']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'created_at', 'updated_at', 'user', 'is_active')
    list_filter = ('created_at', 'updated_at', 'is_active')
    search_fields = ['name', 'address', 'phone_number']
    readonly_fields = ('created_at', 'updated_at')


class CreditTransactionAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'vehicle_number', 'volume', 'price_per_litre', 'total_price', 'created_at', 'updated_at')
    list_filter = ('customer__name', 'product__code', 'created_at', 'updated_at')
    search_fields = ['customer__name', 'vehicle_number']
    readonly_fields = ('total_price', 'price_per_litre')

admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CreditTransaction, CreditTransactionAdmin)

# Yet to define the admin classes for StockInventory and DailyLubeSales
admin.site.register(StockInventory)
admin.site.register(DailyLubeSales)