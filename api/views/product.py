from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# from rest_framework import viewsets

from rest_framework.generics import ListAPIView
from api.models import Product
from api.serializers import ProductSerializer


class ProductViewSet(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
