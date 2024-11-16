from django.db.models import Sum
from django.contrib import admin
from api.models import LubeLiveStock

class LubeLiveStockAdmin(admin.ModelAdmin):
    list_display = [
        "product_name",
        "remaining_stock",
        "price_per_item",
        "custom_total_value",
    ]
    search_fields = ["product_name"]
    list_filter = ["product_name"]

    def custom_total_value(self, obj):
        return f"₹ {obj.total_value}"

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        total_lube_asset = LubeLiveStock.objects.aggregate(Sum("total_value"))[
            "total_value__sum"
        ]
        if total_lube_asset is None:
            total_lube_asset = 0
        extra_context = extra_context or {}
        extra_context["total_lube_asset"] = total_lube_asset

        return super().changelist_view(request, extra_context)


admin.site.register(LubeLiveStock, LubeLiveStockAdmin)