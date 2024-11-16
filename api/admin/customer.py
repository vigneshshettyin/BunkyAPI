from django.contrib import admin
from api.models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "phone_number",
        "created_at",
        "updated_at",
        "user",
        "is_active",
    )
    list_filter = ("created_at", "updated_at", "is_active")
    search_fields = ["name", "address", "phone_number"]
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Customer, CustomerAdmin)
