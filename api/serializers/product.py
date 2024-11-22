from rest_framework import serializers
from api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "code", "name", "price", "updated_at"]
        read_only_fields = ["id", "updated_at"]
