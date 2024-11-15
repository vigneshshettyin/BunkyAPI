from rest_framework import serializers
from api.models import CreditTransaction


class CreditSerializer(serializers.ModelSerializer):
    
    product_code = serializers.CharField(source="product.code", read_only=True)
    customer_name = serializers.CharField(source="customer.name",read_only=True)

    class Meta:
        model = CreditTransaction
        fields = (
            "product",
            "product_code",
            "customer",
            "customer_name",
            "vehicle_number",
            "volume",
            "price_per_litre",
            "total_price",
            "date_created",
            "date_modified",
        )