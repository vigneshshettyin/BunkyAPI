from rest_framework import serializers
from api.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("name", "email", "address", "phone_number", "date_created", "date_modified")