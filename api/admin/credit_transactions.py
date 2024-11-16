from django.contrib import admin
from api.models import CreditTransaction


class CreditTransactionAdmin(admin.ModelAdmin):
    list_display = (
        "customer",
        "product",
        "vehicle_number",
        "volume",
        "price_per_litre",
        "total_price",
        "created_at",
        "updated_at",
    )
    list_filter = ("customer__name", "product__code", "created_at", "updated_at")
    search_fields = ["customer__name", "vehicle_number"]
    readonly_fields = ("total_price", "price_per_litre")


admin.site.register(CreditTransaction, CreditTransactionAdmin)