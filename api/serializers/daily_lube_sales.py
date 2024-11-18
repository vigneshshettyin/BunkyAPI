from rest_framework import serializers
from api.models import DailyLubeSales


class DailyLubeSalesSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source="product.name", read_only=True)
    product_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, source="product.price", read_only=True
    )
    total_price = serializers.SerializerMethodField(read_only=True)

    def get_total_price(self, obj):
        return obj.product.price * obj.quantity

    class Meta:
        model = DailyLubeSales
        fields = (
            "id",
            "product",
            "product_name",
            "product_price",
            "quantity",
            "total_price",
            "date",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")
