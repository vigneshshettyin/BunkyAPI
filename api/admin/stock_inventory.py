from django.contrib import admin
from api.models import StockInventory, Product

class StockInventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'date', 'updated_at')
    list_display_links = ('product',)
    search_fields = ('product__name', 'quantity')
    list_per_page = 25

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "product":
            kwargs["queryset"] = Product.objects.filter(is_fuel=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(StockInventory, StockInventoryAdmin)
