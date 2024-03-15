from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from api.serializers.user import UserLoginSerializer


class LoginViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for authenticating users and returning an auth token.

    """

    serializer_class = UserLoginSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.initial_data
        user = User.objects.filter(email=data["email"]).first()
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, "created": created})
