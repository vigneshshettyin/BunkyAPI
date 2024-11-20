from django.contrib import admin
from api.models import StockInventory

class StockInventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'date', 'updated_at')
    list_display_links = ('product',)
    search_fields = ('product__name', 'quantity')
    list_per_page = 25

admin.site.register(StockInventory, StockInventoryAdmin)