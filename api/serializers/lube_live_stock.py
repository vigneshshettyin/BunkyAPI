from rest_framework import serializers
from api.models import LubeLiveStock

class LubeLiveStockSerializer(serializers.ModelSerializer):

    class Meta:
        model = LubeLiveStock
        fields = (
            "product_id",
            "product_name",
            "remaining_stock",
            "price_per_item",
            "total_value",
        )
        read_only_fields = ("product_id", "product_name", "remaining_stock", "price_per_item", "total_value")