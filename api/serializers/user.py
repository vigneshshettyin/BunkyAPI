from django.contrib.auth.models import User
from rest_framework import serializers


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True, write_only=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ("email", "password")

    def validate(self, data):
        user = User.objects.filter(email=data["email"]).first()
        if user is None:
            raise serializers.ValidationError("Invalid email")
        if not user.check_password(data["password"]):
            raise serializers.ValidationError("Invalid password")
        return data
