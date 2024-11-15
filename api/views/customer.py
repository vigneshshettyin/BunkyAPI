from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets

from rest_framework.generics import ListAPIView
from api.models import Customer
from api.serializers import CustomerSerializer


class CustomerViewSet(ListAPIView, viewsets.ViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
