from django.contrib import admin
from api.models import DailyLubeSales

class DailyLubeSalesAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "quantity",
        "product_price",
        "total_price",
        "created_at",
        "updated_at",
    )
    list_filter = ("product__code", "created_at", "updated_at")
    search_fields = ["product__code"]

    def total_price(self, obj):
        return f"₹{obj.quantity * obj.product.price}"
    
    def product_price(self, obj):
        return f"₹{obj.product.price}"

admin.site.register(DailyLubeSales, DailyLubeSalesAdmin)