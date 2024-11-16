from rest_framework import serializers
from api.models import DailyLubeSales


class DailyLubeSalesSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source="product.name", read_only=True)

    class Meta:
        model = DailyLubeSales
        fields = (
            "id",
            "user",
            "product",
            "product_name",
            "quantity",
            "date",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")
